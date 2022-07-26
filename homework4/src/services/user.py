import uuid
from datetime import datetime
from typing import Optional, NoReturn

from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from functools import lru_cache
from redis import Redis

from fastapi import Depends, HTTPException, Security
from sqlmodel import Session
from starlette import status

from src.api.v1.schemas import UserCreate, Token
from src.core.config import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_ACCESS_EXPIRE_SECONDS,
    JWT_REFRESH_EXPIRE_SECONDS,
)
from src.db import (
    AbstractCache,
    get_session,
    get_cache,
    get_blocked_access_cache,
    get_active_refresh_cache,
)
from src.models import User
from src.services import ServiceMixin

__all__ = ("UserService", "get_user_service", "get_token")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


class UserService(ServiceMixin):
    def __init__(
        self,
        cache: AbstractCache,
        access_cash: Redis,
        refresh_cash: Redis,
        session: Session,
    ):
        super().__init__(cache=cache, session=session)
        self.blocked_access_token: Redis = access_cash
        self.active_refresh_token: Redis = refresh_cash

    def get_user_or_none_by_username(self, username: str) -> Optional[User]:
        user = self.session.query(User).filter(User.username == username).first()
        return user

    def get_user_or_none_by_uuid(self, user_uuid: str) -> Optional[User]:
        user = self.session.query(User).filter(User.uuid == user_uuid).first()
        return user

    def get_current_user(self, token) -> User:
        payload = self.decode_token(token)
        jti = payload.get("jti", None)
        user_uuid: str = payload.get("user_uuid", None)
        if jti is None or user_uuid is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect payload"
            )
        if self.check_jti_in_blocked(jti):
            raise HTTPException(
                status_code=status.HTTP_410_GONE, detail="Token in block list"
            )
        user: User = self.get_user_or_none_by_uuid(user_uuid)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Can't find user by token's payload",
            )
        return user

    def check_jti_in_blocked(self, jti: str) -> bool:
        if self.blocked_access_token.get(jti):
            return True
        return False

    def block_access_token(self, jti: str) -> NoReturn:
        self.blocked_access_token.set(jti, "blocked")

    @classmethod
    def verify_password(cls, plain_password: str, hash_password: str) -> bool:
        return bcrypt.verify(plain_password, hash_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    def register_new_user(self, user_data: UserCreate) -> User:
        if self.get_user_or_none_by_username(user_data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username is already taken",
            )
        user = User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def authenticate_user(
        self,
        username: str,
        password: str,
    ) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        user = self.session.query(User).filter(User.username == username).first()
        if not user or not self.verify_password(password, user.password_hash):
            raise exception
        return user

    def update_user(self, user: User, user_data: dict, token: str) -> User:
        for key, value in user_data.items():
            setattr(user, key, value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        jti: str = self.get_token_jti(token)
        self.block_access_token(jti)
        return user

    @staticmethod
    def decode_token(token: str) -> dict:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except JWTError:
            raise exception from None
        return payload

    def get_token_jti(self, token: str) -> str:
        payload = self.decode_token(token)
        jti = payload.get("jti", None)
        if not jti:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect payload"
            )
        return jti

    @staticmethod
    def create_token_str(sub: dict, token_type: str, exp: int) -> str:
        payload = sub.copy()
        now = datetime.utcnow().timestamp()
        payload.update(
            {
                "iat": int(now),
                "nbf": int(now),
                "jti": str(uuid.uuid4()),
                "exp": int(now + exp),
                "type": token_type,
            }
        )
        return jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM)

    def create_token_by_user(self, user: User) -> Token:
        user_uuid = str(user.dict().get("uuid"))
        refresh_token: str = self.create_token_str(
            sub={"user_uuid": user_uuid},
            token_type="refresh",
            exp=JWT_REFRESH_EXPIRE_SECONDS,
        )
        refresh_jti: str = self.get_token_jti(refresh_token)
        access_token: str = self.create_token_str(
            sub={"user_uuid": user_uuid, "refresh_jti": refresh_jti},
            token_type="access",
            exp=JWT_ACCESS_EXPIRE_SECONDS,
        )
        self.active_refresh_token.lpush(user_uuid, refresh_jti)
        return Token(access_token=access_token, refresh_token=refresh_token)

    def refresh_token(self, token: str) -> Token:
        payload = self.decode_token(token)
        user_uuid: str = payload.get("user_uuid", None)
        jti: str = payload.get("jti", None)
        user: User = self.get_user_or_none_by_uuid(user_uuid)
        if not user or not jti:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect payload"
            )
        self.active_refresh_token.lrem(user_uuid, 0, jti)
        return self.create_token_by_user(user)

    def logout(self, token: str) -> NoReturn:
        payload = self.decode_token(token)
        jti: str = payload.get("jti", None)
        refresh_jti: str = payload.get("refresh_jti", None)
        user_uuid: str = payload.get("user_uuid", None)
        if not jti or not refresh_jti or not user_uuid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect payload"
            )
        self.active_refresh_token.lrem(user_uuid, 0, refresh_jti)
        self.block_access_token(jti)

    def logout_all(self, token: str) -> NoReturn:
        payload = self.decode_token(token)
        jti: str = payload.get("jti", None)
        user_uuid: str = payload.get("user_uuid", None)
        if not jti or not user_uuid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect payload"
            )
        self.block_access_token(token)
        self.active_refresh_token.delete(user_uuid)


@lru_cache
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    access_cache: Redis = Depends(get_blocked_access_cache),
    refresh_cache: Redis = Depends(get_active_refresh_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(
        cache=cache,
        refresh_cash=refresh_cache,
        access_cash=access_cache,
        session=session,
    )


def get_token(token: str = Security(oauth2_scheme)):
    return token

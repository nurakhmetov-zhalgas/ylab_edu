from fastapi import APIRouter, status, Depends

from src.api.v1.schemas import UserCreate, Token, UserModel, UserLogin, UserUpdate
from src.core.config import JWT_ACCESS_EXPIRE_SECONDS
from src.models import User
from src.services.user import UserService, get_user_service, get_token

router = APIRouter(tags=["auth"])


@router.post(path="/signup", status_code=status.HTTP_201_CREATED, summary="Регистрация")
def signup(
    user_data: UserCreate, user_service: UserService = Depends(get_user_service)
) -> dict:
    try:
        user = user_service.register_new_user(user_data=user_data)
    except ValueError as error:
        raise {"error": str(error)}
    response = {"msg": "User created", "user": UserModel(**user.dict())}
    return response


@router.post(path="/login", response_model=Token, summary="Вход")
def login(
    user: UserLogin,
    user_service: UserService = Depends(get_user_service),
) -> Token:
    user: User = user_service.authenticate_user(user.username, user.password)
    token: Token = user_service.create_token_by_user(user)
    return token


@router.get(path="/users/me", summary="Профиль")
def get_user(
    user_service: UserService = Depends(get_user_service),
    token: str = Depends(get_token),
) -> dict:
    user = user_service.get_current_user(token)
    response = {"user": dict(UserModel(**user.dict()))}
    return response


@router.patch(path="/users/me", summary="Обновить информацию о себе")
def update_user(
    user_data: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    token: str = Depends(get_token),
):
    user: User = user_service.get_current_user(token)
    user: User = user_service.update_user(
        user, user_data.dict(exclude_unset=True), token
    )
    access_token: str = user_service.create_token_str(
        str(user.uuid), "access", JWT_ACCESS_EXPIRE_SECONDS
    )
    response = {
        "msg": "Update is successful. Please use new access token.",
        "user": UserModel(**user.dict()),
        "access_token": access_token,
    }
    return response


@router.post(path="/refresh", response_model=Token, summary="Обновить токен")
def refresh_token(
    user_service: UserService = Depends(get_user_service),
    token: str = Depends(get_token),
) -> Token:
    return user_service.refresh_token(token)


@router.post(path="/logout", summary="Выйти")
def logout(
    user_service: UserService = Depends(get_user_service),
    token: str = Depends(get_token),
) -> dict:
    user_service.logout(token)
    return {"msg": "You have been logged out."}


@router.post(path="/logout_all", summary="Выйти со всех устройств")
def logout_all(
    user_service: UserService = Depends(get_user_service),
    token: str = Depends(get_token),
) -> dict:
    user_service.logout_all(token)
    return {"msg": "You have been logged out from all devices."}

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4

__all__ = (
    "Token",
    "UserBase",
    "UserLogin",
    "UserUpdate",
    "UserCreate",
    "UserModel",
)


class Token(BaseModel):
    access_token: str
    refresh_token: str


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: EmailStr


class UserLogin(UserBase):
    password: str


class UserModel(UserBase):
    uuid: UUID4
    created_at: datetime
    is_superuser: bool
    is_active: bool
    email: EmailStr

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

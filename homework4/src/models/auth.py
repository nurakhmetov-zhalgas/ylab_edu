from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel, UniqueConstraint

__all__ = ("User",)


class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("username"), UniqueConstraint("email"))

    uuid: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    username: str = Field(nullable=False)
    email: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    is_superuser: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

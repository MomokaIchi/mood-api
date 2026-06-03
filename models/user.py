from __future__ import annotations
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .follow import Follow

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str
    hashed_password: str

    # Users this user is following
    following: list["Follow"] = Relationship(back_populates="follower_user")

    # Users who follow this user
    followers: list["Follow"] = Relationship(back_populates="following_user")

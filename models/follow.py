from __future__ import annotations
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import UniqueConstraint

if TYPE_CHECKING:
    from .user import User

class Follow(SQLModel, table=True):
    __tablename__ = "follows"

    id: int | None = Field(default=None, primary_key=True)

    follower_id: int = Field(foreign_key="users.id")
    following_id: int = Field(foreign_key="users.id")

    follower_user: User = Relationship(back_populates="following")
    following_user: User = Relationship(back_populates="followers")

    __table_args__ = (
        UniqueConstraint("follower_id", "following_id", name="unique_follow"),
    )

from sqlmodel import SQLModel, Field
from sqlalchemy.orm import relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    hashed_password: str

follows = relationship(
    "Follow",
    foreign_keys="Follow.follower_id",
    backref="follower"
)

followers = relationship(
    "Follow",
    foreign_keys="Follow.following_id",
    backref="following"
)
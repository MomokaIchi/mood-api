from sqlmodel import SQLModel, Field, Relationship

class Follow(SQLModel, table=True):
    __tablename__ = "follows"

    id: int | None = Field(default=None, primary_key=True)

    follower_id: int = Field(foreign_key="users.id")
    following_id: int = Field(foreign_key="users.id")

    # Prevent duplicate follows
    __table_args__ = (
        UniqueConstraint("follower_id", "following_id", name="unique_follow"),
    )

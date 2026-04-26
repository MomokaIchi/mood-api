from sqlmodel import SQLModel

class FollowCreate(SQLModel):
    following_id: int

class FollowRead(SQLModel):
    id: int
    follower_id: int
    following_id: int

class FollowingUser(SQLModel):
    id: int
    username: str

class FollowerUser(SQLModel):
    id: int
    username: str

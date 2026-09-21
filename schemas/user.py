from sqlmodel import SQLModel

class UserCreate(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    username: str

class UserUpdate(SQLModel):
    username: str

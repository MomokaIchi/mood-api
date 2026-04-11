from sqlmodel import SQLModel

class UserCreate(SQLModel):
    name: str

class UserRead(SQLModel):
    id: int
    name: str

class UserUpdate(SQLModel):
    name: str

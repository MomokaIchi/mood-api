from sqlmodel import SQLModel
from datetime import datetime

class PostCreate(SQLModel):
    mood: str
    mood_score: int

class PostRead(SQLModel):
    id: int
    mood: str
    mood_score: int
    created_at: datetime

class PostUpdate(SQLModel):
    mood: str
    mood_score: int

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mood: str
    mood_score: int
    created_at: datetime = Field(default_factory=datetime.utcnow)


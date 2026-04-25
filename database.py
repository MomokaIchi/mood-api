from __future__ import annotations
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

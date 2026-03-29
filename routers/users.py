from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import engine
from models.user import User

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/users")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/users")
def list_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import engine
from models.user import User
from fastapi import HTTPException

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

@router.put("/users/{user_id}")
def update_user(user_id: int, new_data: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = new_data.name

    session.add(user)
    session.commit()
    session.refresh(user)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()

    return {"message": "User deleted successfully"}
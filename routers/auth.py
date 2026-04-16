# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from core.security import verify_password, create_access_token
from core.config import settings
from models.user import User
from database import get_session
from core.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)):
    statement = select(User).where(User.username == form_data.username)
    user = session.exec(statement).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"sub": str(user.id)},   # MUST be string
        settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user

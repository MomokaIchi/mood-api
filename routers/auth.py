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

@router.post("/signup")
def signup(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session = Depends(get_session)
):
    # 1. Check if username already exists
    statement = select(User).where(User.username == form_data.username)
    existing_user = session.exec(statement).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # 2. Hash password
    from core.security import hash_password
    hashed = hash_password(form_data.password)

    # 3. Create user
    new_user = User(
        username=form_data.username,
        hashed_password=hashed
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {
        "id": new_user.id,
        "username": new_user.username
    }

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

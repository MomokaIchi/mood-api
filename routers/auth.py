from fastapi import APIRouter, Depends
from core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    token = create_access_token({"sub": "momo"})
    return {"access_token": token, "token_type": "bearer"}

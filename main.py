from fastapi import FastAPI
from database import create_db_and_tables

from routers.users import router as users_router
from routers.posts import router as posts_router
from routers.auth import router as auth_router
from routers.follows import router as follows_router


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Routers
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(auth_router)
app.include_router(follows_router)


# http://127.0.0.1:8000/docs
# python -m uvicorn main:app --reload

from fastapi import FastAPI
from database import create_db_and_tables
from routers.users import router as users_router
# from routers.posts import router as posts_router
# from routers.auth import router as auth_router
# from models.user import User
# from models.post import Post

# declaration
app = FastAPI()

# to ensure existing a database (mainly for the first time)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users_router)
# app.include_router(posts_router)
# app.include_router(auth_router)

# http://127.0.0.1:8000


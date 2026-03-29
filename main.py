from fastapi import FastAPI
from database import create_db_and_tables
from routers.users import router as users_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users_router)

# http://127.0.0.1:8000


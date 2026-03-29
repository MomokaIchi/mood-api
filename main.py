from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello Mood API"}

@app.get("/Hello")
def hello():
    return {"message": "Hello"}

@app.get("/User")
def get_user():
    return {"name": "Momo",
            "mood": "bad"}

# http://127.0.0.1:8000


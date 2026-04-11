from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import engine
from models.post import Post
from schemas.post import PostCreate, PostRead, PostUpdate
from fastapi import HTTPException

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

# Create
@router.post("/posts", response_model=PostRead)
def create_post(post: PostCreate, session: Session = Depends(get_session)):
    new_post = Post(**post.dict())
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post

# Read
@router.get("/posts")
def list_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Post)).all()
    return posts

# Update
@router.put("/posts/{post_id}")
def update_post(post_id: int, new_data: PostUpdate, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.mood = new_data.mood
    post.mood_score = new_data.mood_score
    session.add(post)
    session.commit()
    session.refresh(post)

    return post

# Delete
@router.delete("/posts/{post_id}")
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(post)
    session.commit()

    return {"message": "Post deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import engine
from models.post import Post

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/posts")
def create_post(post: Post, session: Session = Depends(get_session)):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

@router.get("/posts")
def list_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Post)).all()
    return posts

@router.put("/posts/{post_id}")
def update_post(post_id: int, new_data: Post, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.content = new_data.content  # adjust field name to your model

    session.add(post)
    session.commit()
    session.refresh(post)

    return post

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(post)
    session.commit()

    return {"message": "Post deleted successfully"}

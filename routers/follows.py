from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.follow import Follow
from models.user import User
from auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Follow"]
)

@router.post("/{target_id}/follow")
def follow_user(target_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    # Cannot follow yourself
    if target_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    # Check target user exists
    target_user = db.query(User).filter(User.id == target_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Target user not found")

    # Check if already following
    existing = db.query(Follow).filter(
        Follow.follower_id == current_user.id,
        Follow.following_id == target_id
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Already following this user")

    # Create follow relationship
    follow = Follow(
        follower_id=current_user.id,
        following_id=target_id
    )
    db.add(follow)
    db.commit()

    return {"message": "Followed successfully"}


@router.delete("/{target_id}/follow")
def unfollow_user(target_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    follow = db.query(Follow).filter(
        Follow.follower_id == current_user.id,
        Follow.following_id == target_id
    ).first()

    if not follow:
        raise HTTPException(status_code=404, detail="You are not following this user")

    db.delete(follow)
    db.commit()

    return {"message": "Unfollowed successfully"}

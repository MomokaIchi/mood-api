from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models.follow import Follow
from models.user import User
from routers.auth import get_current_user
from schemas.follow import FollowingUser, FollowerUser


router = APIRouter(
    prefix="/users",
    tags=["Follow"]
)

@router.post("/{target_id}/follow")
def follow_user(
    target_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    # Cannot follow yourself
    if target_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    # Check target user exists
    target_user = session.exec(
        select(User).where(User.id == target_id)
    ).first()

    if not target_user:
        raise HTTPException(status_code=404, detail="Target user not found")

    # Check if already following
    existing = session.exec(
        select(Follow).where(
            Follow.follower_id == current_user.id,
            Follow.following_id == target_id
        )
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Already following this user")

    # Create follow relationship
    follow = Follow(
        follower_id=current_user.id,
        following_id=target_id
    )
    session.add(follow)
    session.commit()

    return {"message": "Followed successfully"}


@router.delete("/{target_id}/follow")
def unfollow_user(
    target_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):

    follow = session.exec(
        select(Follow).where(
            Follow.follower_id == current_user.id,
            Follow.following_id == target_id
        )
    ).first()

    if not follow:
        raise HTTPException(status_code=404, detail="You are not following this user")

    session.delete(follow)
    session.commit()

    return {"message": "Unfollowed successfully"}


@router.get("/{user_id}/following", response_model=list[FollowingUser])
def get_following(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # user.following → list[Follow]
    return [
        FollowingUser(
            id=f.following_user.id,
            username=f.following_user.username
        )
        for f in user.following
    ]


@router.get("/{user_id}/followers", response_model=list[FollowerUser])
def get_followers(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # user.followers → list[Follow]
    return [
        FollowerUser(
            id=f.follower_user.id,
            username=f.follower_user.username
        )
        for f in user.followers
    ]

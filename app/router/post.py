import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
import database, models
# from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import oauth2

router = APIRouter(
    tags = ['Posts']
)

###############################################################################
## Post

@router.post('/posts/', response_model=models.PostRead)
def create_post(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    post: models.PostCreate
):
    # new_post = models.Post(title=request.title, body=request.body, author_id=request.author_id)
    db_post = models.Post.from_orm(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return post

@router.get('/posts', response_model=List[models.PostRead])
def read_posts(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    # posts = session.exec(select(models.Post).offset(offset).limit(limit)).all()
    if current_user is None:
        raise HTTPException(status_code=401, detail="User not authenticated")

    posts = session.query(models.Post).filter(models.Post.author_id == current_user.id).offset(offset).limit(limit).all()
    return posts
    # posts = session.exec(session.query(models.Post).filter(models.Post.author_id == current_user.id)).all()
    # return posts

@router.get('/posts/{post_id}', response_model=models.PostReadWithUser)
def read_post(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    post_id: int
):
    post = session.get(models.Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} is not available")
    return post

@router.patch('/posts/{post_id}', response_model=models.PostRead)
def update_post(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    post_id: int,
    post: models.PostUpdate
):
    db_post = session.get(models.Post, post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@router.delete('/posts/{post_id}')
def delete_post(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    post_id: int,
):
    post = session.get(models.Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    session.delete(post)
    session.commit()
    return {'detail': f"Post with id {post_id} was deleted"}


###############################################################################

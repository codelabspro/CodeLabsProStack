import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
from sqlalchemy.orm import Session


###############################################################################
## Post Repository

def get_all(db: Session):
    posts = db.query(models.Post).all()
    return posts

def create(request: models.PostCreate, db: Session):
    new_post = models.Post(title=request.title, body=request.body, author_id=request.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def destroy(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': f"Post with id {id} was deleted"}

def update(id: int, request: models.PostCreate, db:Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.update({'title': request.title, 'body': request.body})
    db.commit()
    return {'detail': f"Post with id {id} was updated"}

def show(id: int, response: Response, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not available")
    return post

###############################################################################

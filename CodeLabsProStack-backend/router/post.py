import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response

import schemas, database, models
from sqlalchemy.orm import Session
from repository import post

router = APIRouter(
    tags = ['Posts']
)

###############################################################################
## Post

@router.get('/posts', response_model=List[schemas.ShowPost])
def all(db: Session = Depends(database.get_db)):
    return post.get_all(db)

@router.post('/post', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Post, db: Session = Depends(database.get_db)):
    return post.create(request, db)

@router.delete('/blogpost/{id}', status_code=200)
def destroy(id, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': f"Post with id {id} was deleted"}

@router.put('/blogpost/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Post, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.update({'title': request.title, 'body': request.body})
    db.commit()
    return {'detail': f"Post with id {id} was updated"}



@router.get('/blogpost/{id}', status_code=200, response_model=schemas.ShowPost)
def read_post(id, response: Response, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not available")
    return post

###############################################################################

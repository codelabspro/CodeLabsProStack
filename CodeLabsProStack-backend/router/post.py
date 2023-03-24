import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
import schemas, database, models
from sqlalchemy.orm import Session
from repository import postRepository

router = APIRouter(
    tags = ['Posts']
)

###############################################################################
## Post

@router.get('/posts', response_model=List[schemas.ShowPost])
def all(db: Session = Depends(database.get_db)):
    return postRepository.get_all(db)

@router.post('/post', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Post, db: Session = Depends(database.get_db)):
    return postRepository.create(request, db)

@router.delete('/post/{id}', status_code=200)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return postRepository.destroy(id, db)

@router.put('/post/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Post, db: Session = Depends(database.get_db)):
    return postRepository.update(id, request, db)

@router.get('/post/{id}', status_code=200, response_model=schemas.ShowPost)
def show(id: int, response: Response, db: Session = Depends(database.get_db)):
    return postRepository.show(id, response, db)

###############################################################################

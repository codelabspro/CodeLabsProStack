import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
from sqlalchemy.orm import Session
from repository import postRepository
import oauth2

router = APIRouter(
    tags = ['Posts']
)

###############################################################################
## Post

@router.get('/posts', response_model=List[models.PostRead])
def all(db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return postRepository.get_all(db)

@router.post('/post', status_code=status.HTTP_201_CREATED)
def create(request: models.PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return postRepository.create(request, db)

@router.delete('/post/{id}', status_code=200)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return postRepository.destroy(id, db)

@router.put('/post/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: models.PostBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return postRepository.update(id, request, db)

@router.get('/post/{id}', status_code=200, response_model=models.PostRead)
def show(id: int, response: Response, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return postRepository.show(id, response, db)

###############################################################################

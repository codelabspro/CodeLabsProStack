import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response

import database, models
from sqlalchemy.orm import Session
from repository import userRepository

router = APIRouter(
    tags = ['Users']
)

###############################################################################
## User

@router.post('/user', response_model=models.UserRead)
def create_user(request: models.UserCreate, db: Session = Depends(database.get_db)):
    return userRepository.create(request, db)

@router.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: models.UserCreate, db: Session = Depends(database.get_db)):
    return userRepository.update(id, request, db)

@router.get('/users', response_model=List[models.UserRead])
def get_users(db: Session = Depends(database.get_db)):
    return userRepository.get_all(db)

@router.get('/user/{id}', response_model=models.UserRead)
def get_user(id:int, db: Session = Depends(database.get_db)):
    return userRepository.show(id, db)

###############################################################################

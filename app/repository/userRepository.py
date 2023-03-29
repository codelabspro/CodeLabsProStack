import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import APIRouter, Depends, status, HTTPException, Response
import models
from hashing import Hash
from sqlalchemy.orm import Session

###############################################################################
## User Repository

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def create(request: models.UserCreate, db: Session):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update(id: int, request: models.UserCreate, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    user.update({'name': request.name, 'email': request.email, 'password': request.password})
    db.commit()
    return {'detail': f"User with id {id} was updated"}

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user

###############################################################################

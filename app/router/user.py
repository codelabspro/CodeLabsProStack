import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

import database, models
from sqlalchemy.orm import Session
from hashing import Hash

router = APIRouter(
    tags = ['Users']
)

###############################################################################
## User

@router.post('/users/', response_model=models.UserRead)
def create_user(
    *,
    session: Session = Depends(database.get_session),
    user: models.UserCreate
):
    db_user = models.User(name = user.name, email = user.email, password = Hash.bcrypt(user.password))
    # db_user = models.User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get('/users/', response_model=List[models.UserRead])
def read_users(
    *,
    session: Session = Depends(database.get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(models.User).offset(offset).limit(limit)).all()
    return users

@router.get('/users/{user_id}', response_model=models.UserReadWithPosts)
def read_user(
    *,
    user_id:int,
    session: Session = Depends(database.get_session)
):
    user = session.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user


@router.patch('/users/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(
    *,
    session: Session = Depends(database.get_session),
    user_id: int,
    user: models.UserUpdate,
):
    db_user = session.get(models.User, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    db_user = models.UserBase(name = user.name, email = user.email, password = Hash.bcrypt(user.password))
    # user_data = user.dict(exclude_unset=True)
    #for key, value in user_data.items():
    #    setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.delete('/users/{user_id}')
def delete_user(
    *,
    session: Session = Depends(database.get_session),
    user_id: int
):
    user = session.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    session.delete(user)
    session.commit()
    return {"ok": True}



###############################################################################

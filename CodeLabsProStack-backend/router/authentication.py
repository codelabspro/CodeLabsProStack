import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, status, HTTPException, Response
import schemas, models, database
from hashing import Hash
from sqlalchemy.orm import Session
import accesstoken



router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")

    # generate jwt token and return
    access_token = accesstoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}



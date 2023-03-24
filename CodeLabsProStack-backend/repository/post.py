import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy.orm import Session
import schemas, database, models

def get_all(db: Session):
    posts = db.query(models.Post).all()
    return posts


def create(request: schemas.Post, db: Session):
    new_post = models.Post(title=request.title, body=request.body, author_id=request.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

from fastapi import HTTPException

from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
import datetime
from fastapi import HTTPException,status
from database.models import DbPost

def create(db: Session, request: PostBase):
    new_post=DbPost(
        title=request.title,
        content=request.content,
        timestamp=datetime.datetime.now(),
        creator=request.creator,
        image_url=request.image_url
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db:Session):
    return db.query(DbPost).all()

def delete_post(db:Session, id:int):
    post=db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(post)
    db.commit()
    return "ok"
def delete_all_post(db:Session):
    db.query(DbPost).delete()
    db.commit()
    return "ok"

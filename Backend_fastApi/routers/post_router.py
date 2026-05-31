import shutil

from fastapi import APIRouter, Depends, UploadFile,File
from sqlalchemy.orm import Session
from database import db_post
from database.database import get_db
from database.models import DbPost
from routers.schemas import PostBase,PostDisplay
import string
import random
router = APIRouter(prefix="/post",tags=["post"])

@router.post("",response_model=PostDisplay)

def create(request:PostBase,db :Session=Depends(get_db)):
    return db_post.create(db,request)

@router.get("/all",response_model=list[PostDisplay])
def get(db :Session=Depends(get_db)):

    return db_post.get_all(db)

@router.delete("/all")
def delete_all(db :Session=Depends(get_db)):
    return db_post.delete_all_post(db)

@router.delete("/{id}")
def delete(id:int,db :Session=Depends(get_db)):
    return db_post.delete_post(db,id)




@router.post("/image")
def upload_image(image:UploadFile=File(...)):
    letter=string.ascii_letters
    rand_str=''.join(random.choice(letter) for _ in range(10))
    new=f"{rand_str}."
    filename=new.join(image.filename.rsplit('.',1))
    path=f"images/{filename}"
    with open(path,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)

    return {"filename":path}

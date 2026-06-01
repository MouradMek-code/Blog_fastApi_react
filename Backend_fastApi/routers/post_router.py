import shutil

from fastapi import APIRouter, Depends, UploadFile,File
from sqlalchemy.orm import Session
from database import db_post
from database.database import get_db
from routers.schemas import PostBase,PostDisplay
import cloudinary.uploader
import cloudinary
import os
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)
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

    result = cloudinary.uploader.upload(image.file)

    return {
        "filename": result["secure_url"]
    }
@router.get("/health")
async def health():
    return {"status": "ok"}

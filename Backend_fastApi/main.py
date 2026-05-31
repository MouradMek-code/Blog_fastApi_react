from fastapi import FastAPI
from database import models
from database.database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
from routers import post_router

app.include_router(post_router.router)



models.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")
origins=[
    "http://localhost:3000", "https://blog-fast-api-react-de1sxsl01-mek-mourad-s-projects.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)
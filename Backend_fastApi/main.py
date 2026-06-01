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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.api_route("/post/health", methods=["GET", "HEAD"])
async def health():
    return {"status": "ok"}
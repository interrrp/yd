from fastapi import FastAPI

from yd.routers import video_router

app = FastAPI()

app.include_router(video_router)

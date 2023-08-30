from fastapi import FastAPI

from yd.routers import video_router, audio_router

app = FastAPI()

app.include_router(video_router)
app.include_router(audio_router)

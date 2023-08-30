from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from pytube.exceptions import VideoUnavailable

from yd.core import download_video
from yd.settings import Settings, get_settings

router = APIRouter(prefix="/video")


@router.get("/{video_id}")
async def video(
    video_id: str, settings: Annotated[Settings, Depends(get_settings)]
) -> FileResponse:
    out_path = settings.downloads_dir / f"{video_id}.mp4"

    try:
        await download_video(video_id, out_path)
    except VideoUnavailable:
        raise HTTPException(
            status_code=404,
            detail="Video is unavailable, are you sure you have the correct video ID?",
        )

    return FileResponse(out_path)

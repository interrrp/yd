from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from yd.core import download_video
from yd.settings import Settings, get_settings

router = APIRouter(prefix="/video")


@router.get("/{video_id}")
async def video(
    video_id: str, settings: Annotated[Settings, Depends(get_settings)]
) -> FileResponse:
    out_path = settings.downloads_dir / f"{video_id}.mp4"
    await download_video(video_id, out_path)
    return FileResponse(out_path)

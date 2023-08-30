from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from yd.core import download_audio
from yd.settings import Settings, get_settings

router = APIRouter(prefix="/audio")


@router.get("/{video_id}")
async def audio(
    video_id: str, settings: Annotated[Settings, Depends(get_settings)]
) -> FileResponse:
    out_path = settings.downloads_dir / f"{video_id}.mp3"
    await download_audio(video_id, out_path)
    return FileResponse(out_path)

from pathlib import Path

from pytube import YouTube


async def download_audio(video_id: str, out_path: Path) -> None:
    (
        YouTube(f"https://www.youtube.com/watch?v={video_id}")
        .streams.get_audio_only()
        .download(filename=out_path)
    )

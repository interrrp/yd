from pytube import YouTube


async def download_video(video_id: str, out_path: str) -> None:
    (
        YouTube(f"https://www.youtube.com/watch?v={video_id}")
        .streams.order_by("resolution")
        .first()
        .download(filename=out_path)
    )

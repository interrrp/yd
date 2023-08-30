from pytube import YouTube


async def download_audio(video_id: str, out_path: str) -> None:
    (
        YouTube(f"https://www.youtube.com/watch?v={video_id}")
        .streams.get_audio_only()
        .download(filename=out_path)
    )

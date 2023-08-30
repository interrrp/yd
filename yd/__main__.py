import uvicorn

from yd.app import app
from yd.settings import Settings


def main() -> None:
    settings = Settings()

    if not settings.downloads_dir.exists():
        settings.downloads_dir.mkdir()

    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    main()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8080

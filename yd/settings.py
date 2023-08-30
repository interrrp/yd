from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8080

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

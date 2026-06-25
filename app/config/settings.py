from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    DISCORD_TOKEN: Optional[str] = None

    DISCORD_GUILD_ID: Optional[int] = None

    REDIS_URL: str

    LOG_LEVEL: str = "INFO"

    ENV: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

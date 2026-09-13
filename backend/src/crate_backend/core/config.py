from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CRATE_", env_file=".env")

    app_name: str = "Crate API"
    environment: str = "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()

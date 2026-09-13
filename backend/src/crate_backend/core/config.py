from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CRATE_", env_file=".env")

    app_name: str = "Crate API"
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://crate:crate_dev_password@localhost:5432/crate"

    # Signs auth JWTs and password-reset/verification tokens. Override with a
    # long random value outside development.
    auth_secret: str = "insecure-dev-secret-change-me-before-deploying-anywhere"
    access_token_lifetime_seconds: int = 3600
    cookie_secure: bool = False

    # Origins allowed to send credentialed (cookie-based) requests, e.g. the
    # frontend's dev server.
    allowed_origins: list[str] = ["http://localhost:3000"]


@lru_cache
def get_settings() -> Settings:
    return Settings()

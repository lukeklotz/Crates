from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/src/crate_backend/core/config.py -> repo root is four parents up.
_REPO_ROOT = Path(__file__).resolve().parents[4]


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

    # MusicBrainz ingestion pipeline (Phase 2).
    musicbrainz_dump_dir: str = str(_REPO_ROOT / "MusicBrainz")
    musicbrainz_target_catalog_size: int = 25000

    # Last.fm popularity signal (Phase 3). Free key from
    # https://www.last.fm/api/account/create; the form's homepage/callback
    # URLs are unused by the read-only endpoints called here.
    lastfm_api_key: str = ""

    # Wikidata/Wikipedia text (Phase 4). Wikimedia's User-Agent policy asks
    # API clients for a contact address; it is sent in every request header.
    wikimedia_contact_email: str = ""

    # TF-IDF recommender model file (Phase 4), written by
    # scripts/build_tfidf_model.py and read by the API on first use.
    tfidf_model_path: str = str(_REPO_ROOT / "models" / "tfidf.joblib")

    # Sound-phrase TF-IDF model file, written by
    # scripts/build_tfidf_model.py --sound-phrases and read by the API on
    # first use for approach "phrases".
    tfidf_phrases_model_path: str = str(_REPO_ROOT / "models" / "tfidf-phrases.joblib")

    # Sentence-embedding recommender model file (Phase 5a), written by
    # scripts/build_embedding_model.py and read by the API on first use.
    embeddings_model_path: str = str(_REPO_ROOT / "models" / "embeddings.joblib")

    # Evaluation answer key (Phase 4, Milestone 3): seeds, judgments and
    # dated reports, committed to the repo.
    eval_dir: str = str(_REPO_ROOT / "eval")


@lru_cache
def get_settings() -> Settings:
    return Settings()

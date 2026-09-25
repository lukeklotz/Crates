from crate_backend.core.config import Settings


def test_lastfm_api_key_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_LASTFM_API_KEY", "test-key-value")
    settings = Settings(_env_file=None)
    assert settings.lastfm_api_key == "test-key-value"

from crate_backend.core.config import Settings


def test_lastfm_api_key_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_LASTFM_API_KEY", "test-key-value")
    settings = Settings(_env_file=None)
    assert settings.lastfm_api_key == "test-key-value"


def test_tfidf_model_path_defaults_to_repo_models_dir():
    settings = Settings(_env_file=None)
    assert settings.tfidf_model_path.endswith("/models/tfidf.joblib")


def test_tfidf_model_path_reads_from_env(monkeypatch):
    monkeypatch.setenv("CRATE_TFIDF_MODEL_PATH", "/tmp/elsewhere.joblib")
    settings = Settings(_env_file=None)
    assert settings.tfidf_model_path == "/tmp/elsewhere.joblib"


def test_eval_dir_defaults_to_repo_eval_folder():
    settings = Settings(_env_file=None)
    assert settings.eval_dir.endswith("/eval")

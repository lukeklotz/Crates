import pytest

from crate_backend.scenes.config import (
    TIERS,
    SceneConfigError,
    load_scene_config,
    parse_scene_config,
)
from tests.scene_fixtures import MINIMAL


def test_load_normalizes_terms():
    config = parse_scene_config(MINIMAL)
    assert config.scene("a").terms == frozenset({"shibuya kei"})
    assert config.nondescriptive_terms == frozenset({"seen live"})
    assert config.deprioritized_terms == frozenset({"indie rock"})


def test_one_element_years_are_open_ended():
    assert parse_scene_config(MINIMAL).scene("b").years == (2005, None)


def test_neighbors_follow_adjacent_path_steps():
    config = parse_scene_config(MINIMAL)
    assert config.neighbors("b") == frozenset({"a", "c"})
    assert config.neighbors("a") == frozenset({"b", "d"})
    assert config.neighbors("c") == frozenset({"b"})


def test_settings_are_read():
    settings = parse_scene_config(MINIMAL).settings
    assert settings.broad_weight == 0.3
    assert settings.artist_free_albums == 3
    assert settings.deep_cut_max_votes == 6


def test_unknown_scene_in_path_is_an_error():
    with pytest.raises(SceneConfigError, match="missing"):
        parse_scene_config(MINIMAL.replace('"a", "b", "c"', '"a", "missing"'))


def test_duplicate_scene_id_is_an_error():
    with pytest.raises(SceneConfigError, match="duplicate scene id 'c'"):
        parse_scene_config(MINIMAL.replace('id = "b"', 'id = "c"'))


def test_backwards_years_are_an_error():
    with pytest.raises(SceneConfigError, match="'a'"):
        parse_scene_config(MINIMAL.replace("[1994, 2006]", "[2006, 1994]"))


def test_unknown_tier_is_an_error():
    with pytest.raises(SceneConfigError, match="tier"):
        parse_scene_config(MINIMAL.replace('tier = "center"', 'tier = "core"'))


def test_unknown_scene_lookup_is_an_error():
    with pytest.raises(SceneConfigError, match="nope"):
        parse_scene_config(MINIMAL).scene("nope")


def test_repository_scenes_file_loads():
    config = load_scene_config()
    assert len(config.scenes) == 21
    assert sum(s.share for s in config.scenes) == 100
    assert {s.tier for s in config.scenes} == set(TIERS)


@pytest.mark.parametrize(
    ("old", "new", "message"),
    [
        ("deep_cut_share = 0.15", "deep_cut_share = 0.9", "add up"),
        ("live_share = 0.05", "live_share = -0.1", "live_share"),
        ("broad_only_halfway = 200", "broad_only_halfway = 0", "broad_only_halfway"),
        ("artist_decay = 0.75", "artist_decay = 0", "artist_decay"),
        ("artist_decay = 0.75", "artist_decay = 1.5", "artist_decay"),
    ],
)
def test_settings_are_validated(old, new, message):
    with pytest.raises(SceneConfigError, match=message):
        parse_scene_config(MINIMAL.replace(old, new))

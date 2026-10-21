import uuid

from crate_backend.scenes.catalog import CatalogAlbum
from crate_backend.scenes.config import parse_scene_config
from crate_backend.scenes.pool import to_pool_album
from crate_backend.scenes.select import scene_budgets, select_batch

_SETTINGS = {
    "live_share": 0.0,
    "connector_share": 0.0,
    "deep_cut_share": 0.0,
    "broad_weight": 0.3,
    "artist_free_albums": 3,
    "artist_decay": 0.5,
    "broad_only_halfway": 1_000_000,
    "deprioritized_factor": 0.4,
    "deep_cut_max_votes": 6,
    "deep_cut_min_terms": 4,
    "deep_cut_min_scene_terms": 2,
}

_SCENE_A = """
[[scene]]
id = "a"
name = "A"
tier = "center"
years = [1990, 2010]
share = {share_a}
terms = ["alpha", "alpha two"]
broad_terms = ["rock"]
"""

_SCENE_B = """
[[scene]]
id = "b"
name = "B"
tier = "wider"
years = [1990, 2010]
share = {share_b}
terms = ["beta"]

[[path]]
name = "a to b"
scenes = ["a", "b"]
"""


def make_config(*, two_scenes=False, share_a=7, share_b=3, **settings):
    values = {**_SETTINGS, **settings}
    lines = ["[settings]", *(f"{k} = {v}" for k, v in values.items())]
    lines.append("nondescriptive_terms = []")
    lines.append('deprioritized_terms = ["indie rock"]')
    text = "\n".join(lines) + _SCENE_A.format(share_a=share_a)
    if two_scenes:
        text += _SCENE_B.format(share_b=share_b)
    return parse_scene_config(text)


def album(mbid, terms, *, artist="art-x", year=2000, live=False, config):
    credit = [{"name": artist, "artist": {"id": artist, "name": artist}}] if artist else []
    record = {
        "id": mbid,
        "title": mbid,
        "primary-type": "Album",
        "secondary-types": ["Live"] if live else [],
        "first-release-date": f"{year}-01-01",
        "genres": [],
        "tags": [{"name": name, "count": votes} for name, votes in terms.items()],
        "artist-credit": credit,
    }
    pool_album = to_pool_album(record, config)
    assert pool_album is not None and pool_album.match is not None, mbid
    return pool_album


def catalog_album(mbid, artist):
    return CatalogAlbum(
        album_id=uuid.uuid4(),
        musicbrainz_id=mbid,
        title=mbid,
        artist_name=artist,
        primary_artist_id=artist,
        year=2000,
        terms={},
        match=None,
        has_text=False,
        popularity=None,
    )


def picked(result):
    return [p.musicbrainz_id for p in result.picks]


def test_scene_budgets_largest_remainder():
    config = make_config(two_scenes=True, share_a=2, share_b=1)
    assert scene_budgets(config, 10) == {"a": 7, "b": 3}
    assert scene_budgets(config, 4, ["b"]) == {"b": 4}


def test_select_never_picks_catalog_albums():
    config = make_config()
    pool = [
        album("in-cat", {"alpha": 15}, config=config),
        album("new", {"alpha": 1}, config=config),
    ]
    result = select_batch(pool, [catalog_album("in-cat", "someone")], config, 5)
    assert picked(result) == ["new"]


def test_artist_decay_is_soft():
    config = make_config()
    pool = [album(f"x{i}", {"alpha": 15}, artist="art-x", config=config) for i in range(5)]
    pool += [album(f"y{i}", {"alpha": 7}, artist="art-y", config=config) for i in range(3)]
    result = select_batch(pool, [], config, 4)
    assert picked(result) == ["x0", "x1", "x2", "y0"]

    catalog = [catalog_album(f"old-x{i}", "art-x") for i in range(3)]
    assert picked(select_batch(pool, catalog, config, 1)) == ["y0"]


def test_albums_without_artist_are_not_decayed():
    config = make_config()
    pool = [album(f"n{i}", {"alpha": 3}, artist=None, config=config) for i in range(5)]
    pool.append(album("z", {"alpha": 2}, artist="art-z", config=config))
    assert sorted(picked(select_batch(pool, [], config, 5))) == [f"n{i}" for i in range(5)]


def test_broad_only_rewards_diminish():
    config = make_config(broad_only_halfway=1)
    pool = [album(f"broad{i}", {"rock": 15}, artist=f"art-{i}", config=config) for i in range(3)]
    pool.append(album("specific", {"alpha": 1}, artist="art-s", config=config))
    assert picked(select_batch(pool, [], config, 2)) == ["broad0", "specific"]


def test_deprioritized_top_term_is_penalized():
    config = make_config()
    pool = [
        album("indie", {"alpha": 3, "indie rock": 20}, artist="art-1", config=config),
        album("plain", {"alpha": 1}, artist="art-2", config=config),
    ]
    assert picked(select_batch(pool, [], config, 1)) == ["plain"]


def test_live_albums_only_fill_the_live_slice():
    config = make_config(live_share=0.2)
    pool = [
        album(f"live{i:02}", {"alpha": 15}, artist=f"l{i}", live=True, config=config)
        for i in range(20)
    ]
    pool += [album(f"studio{i:02}", {"alpha": 1}, artist=f"s{i}", config=config) for i in range(20)]
    result = select_batch(pool, [], config, 10)
    live = [p for p in result.picks if p.musicbrainz_id.startswith("live")]
    assert len(result.picks) == 10
    assert len(live) == 2
    assert {p.slice for p in live} == {"live"}


def test_connector_slice_reserved():
    config = make_config(two_scenes=True, connector_share=0.5)
    pool = [
        album(f"conn{i}", {"alpha": 1, "beta": 1}, artist=f"c{i}", config=config) for i in range(2)
    ]
    pool += [
        album(f"strong{i:02}", {"alpha": 15}, artist=f"s{i}", config=config) for i in range(10)
    ]
    result = select_batch(pool, [], config, 10)
    connectors = [p for p in result.picks if p.musicbrainz_id.startswith("conn")]
    assert len(connectors) == 2
    assert {p.slice for p in connectors} == {"connector"}


def test_unused_reserved_slice_goes_to_open():
    config = make_config(connector_share=0.5)
    pool = [album(f"o{i}", {"alpha": 3}, artist=f"a{i}", config=config) for i in range(6)]
    result = select_batch(pool, [], config, 4)
    assert len(result.picks) == 4
    assert {p.slice for p in result.picks} == {"open"}


def test_deep_cut_slice_reserved():
    config = make_config(deep_cut_share=0.5)
    deep_terms = {"alpha": 1, "alpha two": 1, "noise": 1, "lo fi": 1}
    pool = [album("deep", deep_terms, artist="d", config=config)]
    pool += [album(f"strong{i}", {"alpha": 15}, artist=f"s{i}", config=config) for i in range(4)]
    result = select_batch(pool, [], config, 2)
    assert [(p.musicbrainz_id, p.slice) for p in result.picks] == [
        ("deep", "deep"),
        ("strong0", "open"),
    ]


def test_shortfall_moves_to_scenes_with_candidates():
    config = make_config(two_scenes=True)
    pool = [album(f"a{i}", {"alpha": 3}, artist=f"aa{i}", config=config) for i in range(2)]
    pool += [album(f"b{i:02}", {"beta": 3}, artist=f"bb{i}", config=config) for i in range(20)]
    result = select_batch(pool, [], config, 10)
    assert len(result.picks) == 10
    assert result.budgets == {"a": 7, "b": 3}
    assert result.shortfalls == {"a": 5}
    assert sum(p.scene == "b" for p in result.picks) == 8


def test_exhausted_pool_returns_fewer_than_target():
    config = make_config()
    pool = [album(f"e{i:02}", {"alpha": 3}, artist=f"a{i}", config=config) for i in range(12)]
    result = select_batch(pool, [], config, 100)
    assert len(result.picks) == 12
    assert result.shortfalls == {"a": 88}


def test_selection_is_deterministic():
    config = make_config()
    pool = [album(m, {"alpha": 3}, artist=f"art-{m}", config=config) for m in ("c", "a", "b")]
    first = select_batch(pool, [], config, 3)
    assert picked(first) == ["a", "b", "c"]
    assert select_batch(list(reversed(pool)), [], config, 3).picks == first.picks


def test_picks_record_gain_and_evidence():
    config = make_config()
    result = select_batch([album("one", {"alpha": 3}, config=config)], [], config, 1)
    pick = result.picks[0]
    assert (pick.scene, pick.slice, pick.evidence, pick.gain) == ("a", "open", 2.0, 2.0)


def test_exhausted_names_scenes_that_ran_dry_after_redistribution():
    config = make_config(two_scenes=True)
    pool = [album(f"a{i}", {"alpha": 3}, artist=f"aa{i}", config=config) for i in range(2)]
    pool += [album(f"b{i}", {"beta": 3}, artist=f"bb{i}", config=config) for i in range(4)]
    result = select_batch(pool, [], config, 10)
    assert len(result.picks) == 6
    assert result.shortfalls == {"a": 5}
    assert result.exhausted == ["a", "b"]


def test_exhausted_is_empty_when_candidates_remain():
    config = make_config()
    pool = [album(f"e{i}", {"alpha": 3}, artist=f"a{i}", config=config) for i in range(3)]
    assert select_batch(pool, [], config, 2).exhausted == []

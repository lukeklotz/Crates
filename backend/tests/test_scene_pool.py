import gzip
import json

from crate_backend.scenes.pool import read_pool, to_pool_album, write_pool
from crate_backend.scenes.select import is_deep_cut
from tests.scene_fixtures import MINIMAL, minimal_config

config = minimal_config()


def release_group(
    *,
    rg_id="test-rg-1",
    primary_type="Album",
    secondary_types=None,
    genres=None,
    tags=None,
    artist_credit=None,
    first_release_date="1991-11-04",
):
    return {
        "id": rg_id,
        "title": "Test Album",
        "primary-type": primary_type,
        "secondary-types": secondary_types or [],
        "genres": genres or [],
        "tags": [{"name": "shoegaze", "count": 3}] if tags is None else tags,
        "artist-credit": [
            {
                "name": "Test Artist",
                "joinphrase": "",
                "artist": {"id": "test-artist-1", "name": "Test Artist"},
            }
        ]
        if artist_credit is None
        else artist_credit,
        "first-release-date": first_release_date,
    }


def test_pool_album_none_for_single_compilation_or_no_descriptive_terms():
    assert to_pool_album(release_group(primary_type="Single"), config) is None
    assert to_pool_album(release_group(secondary_types=["Compilation"]), config) is None
    assert to_pool_album(release_group(tags=[{"name": "seen live", "count": 5}]), config) is None
    assert to_pool_album(release_group(tags=[]), config) is None


def test_pool_album_fields():
    album = to_pool_album(release_group(), config)
    assert album.musicbrainz_id == "test-rg-1"
    assert album.year == 1991
    assert album.is_live is False
    assert album.terms == {"shoegaze": 3}
    assert album.match.home == "d"
    assert album.artist_name == "Test Artist"
    assert album.total_votes == 3
    assert album.n_terms == 1


def test_pool_album_marks_live():
    assert to_pool_album(release_group(secondary_types=["Live"]), config).is_live is True


def test_pool_album_without_year_has_no_match():
    album = to_pool_album(release_group(first_release_date=""), config)
    assert album.year is None
    assert album.match is None


def test_primary_artist_is_first_credit():
    credits = [
        {"name": "First", "joinphrase": " & ", "artist": {"id": "artist-first", "name": "First"}},
        {"name": "Second", "joinphrase": "", "artist": {"id": "artist-second", "name": "Second"}},
    ]
    album = to_pool_album(release_group(artist_credit=credits), config)
    assert album.primary_artist_id == "artist-first"
    assert album.artist_name == "First & Second"
    assert to_pool_album(release_group(artist_credit=[]), config).primary_artist_id is None


def test_pool_round_trip_reclassifies_with_new_config(tmp_path):
    path = tmp_path / "pool.jsonl.gz"
    assert write_pool([release_group()], path) == 1
    assert [a.match.home for a in read_pool(path, config)] == ["d"]
    without_shoegaze = minimal_config(
        MINIMAL.replace('terms = ["shoegaze", "dream pop"]', 'terms = ["dream pop"]')
    )
    assert [a.match for a in read_pool(path, without_shoegaze)] == [None]


def test_write_pool_keeps_only_pool_fields(tmp_path):
    path = tmp_path / "pool.jsonl.gz"
    record = release_group()
    record["relations"] = [{"type": "wikidata"}]
    write_pool([record], path)
    with gzip.open(path, "rt") as lines:
        stored = json.loads(lines.readline())
    assert "relations" not in stored
    assert stored["id"] == "test-rg-1"


def _deep_cut_album(tags):
    return to_pool_album(release_group(tags=tags), config)


def test_is_deep_cut():
    settings = config.settings
    well_described = [
        {"name": "shoegaze", "count": 1},
        {"name": "dream pop", "count": 1},
        {"name": "noise", "count": 1},
        {"name": "lo fi", "count": 1},
    ]
    assert is_deep_cut(_deep_cut_album(well_described), settings) is True
    famous = [dict(t) for t in well_described]
    famous[0]["count"] = 5
    assert is_deep_cut(_deep_cut_album(famous), settings) is False
    assert is_deep_cut(_deep_cut_album(well_described[:3]), settings) is False
    one_scene_term = [
        well_described[0],
        *({"name": n, "count": 1} for n in ("noise", "lo fi", "loud")),
    ]
    assert is_deep_cut(_deep_cut_album(one_scene_term), settings) is False


def test_is_deep_cut_false_without_scene():
    album = to_pool_album(release_group(first_release_date=None), config)
    assert is_deep_cut(album, config.settings) is False

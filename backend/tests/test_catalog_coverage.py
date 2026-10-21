import uuid

import pytest

from crate_backend.scenes.catalog import CatalogAlbum
from crate_backend.scenes.coverage import edge_coverage, render_coverage, scene_coverage
from crate_backend.scenes.matching import classify
from tests.scene_fixtures import minimal_config

config = minimal_config()


def catalog_album(mbid, terms, year, *, artist="art", has_text=False, popularity=None):
    return CatalogAlbum(
        album_id=uuid.uuid4(),
        musicbrainz_id=mbid,
        title=mbid,
        artist_name=artist,
        primary_artist_id=artist,
        year=year,
        terms=terms,
        match=classify(terms, year, config),
        has_text=has_text,
        popularity=popularity,
    )


def _by_scene(rows):
    return {row.scene: row for row in rows}


def test_entry_point_coverage_is_share_of_top_pool_albums_in_catalog():
    catalog = [catalog_album(f"d{i}", {"shoegaze": 3}, 1991, artist=f"a{i}") for i in range(3)]
    rows = scene_coverage(catalog, {"d": {"d0", "d1", "d2", "d-missing"}}, set(), {}, config)
    assert _by_scene(rows)["d"].entry_point_coverage == 0.75
    assert _by_scene(rows)["a"].entry_point_coverage == 0.0


def test_scene_coverage_counts():
    catalog = [
        catalog_album("d0", {"shoegaze": 3}, 1991, artist="x", has_text=True, popularity=0.9),
        catalog_album("d1", {"shoegaze": 3}, 1992, artist="x", popularity=0.1),
        catalog_album("d2", {"shoegaze": 1, "dream pop": 1, "noise": 1, "lo fi": 1}, 1993, artist="y"),
        catalog_album("none", {"polka": 2}, 1991),
    ]
    rows = scene_coverage(catalog, {}, {"d1"}, {"batch-1": {"d2"}}, config)
    d = _by_scene(rows)["d"]
    assert d.albums == 3
    assert d.live == 1
    assert d.by_batch == {"original": 2, "batch-1": 1}
    assert d.artists == 2
    assert d.max_per_artist == 2
    assert d.deep_cuts == 1
    assert d.with_text == 1 / 3
    assert d.quartiles == {"top": 1, "bottom": 1, "unknown": 1}


def test_edge_coverage_counts_both_directions():
    catalog = [
        catalog_album("d-to-a", {"shoegaze": 5, "shibuya kei": 1}, 1996),
        catalog_album("a-to-d", {"shoegaze": 1, "shibuya kei": 5}, 1996),
        catalog_album("plain", {"shoegaze": 5}, 1996),
    ]
    edges = {(e.a, e.b): e for e in edge_coverage(catalog, config)}
    assert edges[("d", "a")].connectors == 2
    assert edges[("a", "b")].connectors == 0


def test_render_lists_every_scene_and_edge():
    catalog = [catalog_album("d0", {"shoegaze": 3}, 1991)]
    text = render_coverage(
        scene_coverage(catalog, {}, set(), {}, config),
        edge_coverage(catalog, config),
        total=1,
        in_no_scene=0,
        label="baseline-25k",
    )
    assert "baseline-25k" in text
    for scene in config.scenes:
        assert f"| {scene.id} |" in text
    assert "| a to c | a | b |" in text
    assert "| d to a | d | a |" in text


@pytest.mark.asyncio
async def test_write_coverage_script(monkeypatch, tmp_path, db_session):
    from crate_backend.scenes.batches import write_batch
    from crate_backend.scenes.pool import write_pool
    from crate_backend.scripts import catalog_coverage
    from tests.test_ingest_musicbrainz_script import _SessionFactory
    from tests.test_scene_pool import release_group

    pool = tmp_path / "pool.jsonl.gz"
    write_pool([release_group(rg_id="d0"), release_group(rg_id="d-live", secondary_types=["Live"])], pool)
    catalog_dir = tmp_path / "catalog"
    write_batch([{"musicbrainz_id": "d0"}], catalog_dir / "batches" / "batch-1.jsonl")
    catalog = [catalog_album("d0", {"shoegaze": 3}, 1991)]

    async def fake_catalog(session, cfg):
        return catalog

    monkeypatch.setattr(catalog_coverage, "load_scene_config", lambda: config)
    monkeypatch.setattr(catalog_coverage, "load_catalog_albums", fake_catalog)
    monkeypatch.setattr(catalog_coverage, "async_session_factory", _SessionFactory(db_session))

    path = await catalog_coverage.write_coverage("after-batch-1", catalog_dir=catalog_dir, pool_path=pool)
    text = path.read_text()
    assert path.name.endswith("-after-batch-1.md")
    assert "| d | 1 | 0 | 0 | 1 |" in text  # albums, live, original, batch-1
    assert "| 50% |" in text  # d0 of {d0, d-live}

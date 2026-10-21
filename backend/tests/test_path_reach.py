import json
import uuid

import pytest

from crate_backend.evaluation import path_reach
from crate_backend.evaluation.path_reach import pick_path_seeds, reach_rows, render_reach
from crate_backend.scenes.catalog import CatalogAlbum
from crate_backend.scenes.matching import classify
from tests.scene_fixtures import minimal_config
from tests.test_ingest_musicbrainz_script import _SessionFactory

config = minimal_config()


def catalog_album(name, terms, year, artist):
    return CatalogAlbum(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, name),
        musicbrainz_id=name,
        title=name,
        artist_name=artist,
        primary_artist_id=artist,
        year=year,
        terms=terms,
        match=classify(terms, year, config),
        has_text=False,
        popularity=None,
    )


def test_pick_path_seeds_one_per_artist_and_highest_evidence_first():
    catalog = [
        catalog_album("strong", {"shoegaze": 15}, 1991, "x"),
        catalog_album("strong-same-artist", {"shoegaze": 14}, 1992, "x"),
        catalog_album("middle", {"shoegaze": 7}, 1991, "y"),
        catalog_album("weak", {"shoegaze": 1}, 1991, "z"),
        catalog_album("krautrock", {"krautrock": 3}, 1972, "k"),
    ]
    seeds = pick_path_seeds(catalog, config, per_scene=2)
    by_id = {a.album_id: a.title for a in catalog}
    assert [by_id[i] for i in seeds["d"]] == ["strong", "middle"]
    assert [by_id[i] for i in seeds["c"]] == ["krautrock"]
    assert seeds["a"] == []


def test_reach_rows_shares():
    seed = catalog_album("seed", {"shoegaze": 3}, 1991, "s")
    same = [catalog_album(f"same{i}", {"shoegaze": 3}, 1991, f"a{i}") for i in range(2)]
    neighbor = catalog_album("neighbor", {"shibuya kei": 3}, 1996, "n")
    nowhere = catalog_album("nowhere", {"polka": 3}, 1991, "a0")
    index = {a.album_id: a for a in [seed, *same, neighbor, nowhere]}
    runs = {
        "tfidf-tags": {
            seed.album_id: [same[0].album_id, same[1].album_id, neighbor.album_id, nowhere.album_id]
        }
    }

    [row] = reach_rows(runs, {seed.album_id: "d"}, index, config)

    assert (row.variant, row.scene, row.seeds) == ("tfidf-tags", "d", 1)
    assert row.same_scene == 0.5
    assert row.neighbor_scene == 0.25
    assert row.no_scene == 0.25
    assert row.artists == 3


def test_render_reach_says_it_is_coverage_not_quality():
    seed = catalog_album("seed", {"shoegaze": 3}, 1991, "s")
    rows = reach_rows(
        {"overlap": {seed.album_id: []}}, {seed.album_id: "d"}, {seed.album_id: seed}, config
    )
    text = render_reach(rows, label="baseline-25k")
    assert "coverage, not quality" in text
    assert "baseline-25k" in text


@pytest.mark.asyncio
async def test_frozen_seeds_are_reused(monkeypatch, tmp_path, db_session):
    catalog = [catalog_album("strong", {"shoegaze": 15}, 1991, "x")]

    async def fake_catalog(session, cfg):
        return catalog

    async def fake_runs(variants, session, seeds, k):
        return {v.name: {s.album_id: [] for s in seeds} for v in variants}

    monkeypatch.setattr(path_reach, "load_scene_config", lambda: config)
    monkeypatch.setattr(path_reach, "load_catalog_albums", fake_catalog)
    monkeypatch.setattr(path_reach, "run_variants", fake_runs)
    monkeypatch.setattr(path_reach, "async_session_factory", _SessionFactory(db_session))

    first = await path_reach.write_path_reach(
        "baseline", variant_names="overlap", eval_folder=tmp_path
    )
    frozen = json.loads((tmp_path / "path-reach-seeds.json").read_text())
    assert frozen["d"] == [str(catalog[0].album_id)]

    def must_not_run(*args, **kwargs):
        raise AssertionError("seeds were re-picked")

    monkeypatch.setattr(path_reach, "pick_path_seeds", must_not_run)
    second = await path_reach.write_path_reach(
        "after", variant_names="overlap", eval_folder=tmp_path
    )
    assert first.parent == second.parent == tmp_path / "results"
    assert "after" in second.name

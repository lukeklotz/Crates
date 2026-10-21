import json

import pytest

from crate_backend.scripts import select_catalog_batch
from tests.scene_fixtures import minimal_config
from tests.test_ingest_musicbrainz_script import _SessionFactory
from tests.test_scene_pool import release_group

pytestmark = pytest.mark.asyncio

config = minimal_config()


@pytest.fixture
def script(monkeypatch, db_session, tmp_path):
    from crate_backend.scenes.pool import write_pool

    pool = tmp_path / "pool.jsonl.gz"
    write_pool(
        [
            release_group(rg_id=f"rg-{i}", artist_credit=[
                {"name": f"Artist {i}", "artist": {"id": f"artist-{i}", "name": f"Artist {i}"}}
            ])
            for i in range(6)
        ],
        pool,
    )
    monkeypatch.setattr(select_catalog_batch, "load_scene_config", lambda: config)
    monkeypatch.setattr(select_catalog_batch, "async_session_factory", _SessionFactory(db_session))

    async def no_catalog(session, cfg):
        return []

    monkeypatch.setattr(select_catalog_batch, "load_catalog_albums", no_catalog)
    return select_catalog_batch, pool, tmp_path / "catalog"


async def test_select_writes_batch_and_summary(script):
    module, pool, catalog_dir = script
    path = await module.select("batch-1", 4, force=False, catalog_dir=catalog_dir, pool_path=pool)
    lines = [json.loads(line) for line in path.read_text().splitlines()]
    assert len(lines) == 4
    assert set(lines[0]) == {
        "musicbrainz_id", "title", "artist_name", "year", "scene", "slice", "gain", "live",
    }
    assert lines[0]["scene"] == "d"
    summary = (catalog_dir / "batches" / "batch-1.md").read_text()
    for scene in config.scenes:
        assert scene.id in summary
    assert "Target: 4" in summary


async def test_select_refuses_to_overwrite_without_force(script):
    module, pool, catalog_dir = script
    await module.select("batch-1", 2, force=False, catalog_dir=catalog_dir, pool_path=pool)
    with pytest.raises(SystemExit):
        await module.select("batch-1", 2, force=False, catalog_dir=catalog_dir, pool_path=pool)
    path = await module.select("batch-1", 3, force=True, catalog_dir=catalog_dir, pool_path=pool)
    assert len(path.read_text().splitlines()) == 3


async def test_read_batch_ids_round_trip(script):
    module, pool, catalog_dir = script
    path = await module.select("batch-1", 3, force=False, catalog_dir=catalog_dir, pool_path=pool)
    ids = module.read_batch_ids(path)
    assert len(ids) == 3
    assert all(i.startswith("rg-") for i in ids)

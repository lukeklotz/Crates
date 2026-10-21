from pathlib import Path

import pytest

from crate_backend.scenes.pool import read_raw_pool
from crate_backend.scripts import profile_catalog_pool
from tests.scene_fixtures import minimal_config
from tests.test_scene_pool import release_group

pytestmark = pytest.mark.asyncio

_RECORDS = [
    release_group(rg_id="in-scene"),
    release_group(rg_id="single", primary_type="Single"),
    release_group(rg_id="untagged", tags=[]),
]


@pytest.fixture
def script(monkeypatch):
    monkeypatch.setattr(profile_catalog_pool, "load_scene_config", minimal_config)
    monkeypatch.setattr(
        profile_catalog_pool,
        "read_dump_metadata",
        lambda archive: {"TIMESTAMP": "2026-10-18 00:00:46.123+00"},
    )
    monkeypatch.setattr(
        profile_catalog_pool, "stream_jsonl_from_tar", lambda archive, member: iter(_RECORDS)
    )

    async def catalog_ids():
        return {"in-scene"}

    async def catalog_size():
        return 25000

    monkeypatch.setattr(profile_catalog_pool, "_catalog_ids", catalog_ids)
    monkeypatch.setattr(profile_catalog_pool, "_catalog_size", catalog_size)
    return profile_catalog_pool


async def test_profile_dump_writes_pool_and_report(script, tmp_path):
    pool = tmp_path / "pool.jsonl.gz"
    report = await script.profile_dump(Path("/unused"), pool, tmp_path / "reports")
    assert report.name == "profile-2026-10-18.md"
    assert [r["id"] for r in read_raw_pool(pool)] == ["in-scene"]
    text = report.read_text()
    assert "| All release groups | 3 |" in text
    assert "| In a scene and already in the catalog | 1 |" in text


async def test_profile_pool_does_not_read_the_dump(script, tmp_path, monkeypatch):
    pool = tmp_path / "pool.jsonl.gz"
    await script.profile_dump(Path("/unused"), pool, tmp_path / "reports")

    def no_dump(*args):
        raise AssertionError("read the dump")

    monkeypatch.setattr(script, "stream_jsonl_from_tar", no_dump)
    report = await script.profile_pool(pool, tmp_path / "again")
    assert report.name == "profile-2026-10-18.md"
    assert "| In a scene | 1 |" in report.read_text()

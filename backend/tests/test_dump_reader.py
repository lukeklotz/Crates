import json
import tarfile
from pathlib import Path

import pytest

from crate_backend.musicbrainz.dump_reader import read_dump_metadata, stream_jsonl_from_tar


@pytest.fixture
def sample_archive(tmp_path: Path) -> Path:
    """A tiny .tar.xz laid out like a real MusicBrainz dump: small metadata
    files first, then mbdump/<entity> as JSON-lines."""
    files = {
        "TIMESTAMP": "2026-09-23 01:13:07.898407+00\n",
        "REPLICATION_SEQUENCE": "31\n",
        "SCHEMA_SEQUENCE": "189205\n",
        "mbdump/sample": "\n".join(
            json.dumps(r)
            for r in [{"id": "test-1", "name": "Alice"}, {"id": "test-2", "name": "Bob"}]
        )
        + "\n\n",
    }
    archive_path = tmp_path / "sample.tar.xz"
    with tarfile.open(archive_path, mode="w:xz") as tf:
        for arcname, content in files.items():
            source = tmp_path / arcname.replace("/", "_")
            source.write_text(content)
            tf.add(source, arcname=arcname)
    return archive_path


def test_stream_jsonl_from_tar_yields_all_records(sample_archive: Path):
    records = list(stream_jsonl_from_tar(sample_archive, "mbdump/sample"))
    assert [r["name"] for r in records] == ["Alice", "Bob"]


def test_stream_jsonl_from_tar_on_missing_member_yields_nothing(sample_archive: Path):
    assert list(stream_jsonl_from_tar(sample_archive, "mbdump/does-not-exist")) == []


def test_read_dump_metadata(sample_archive: Path):
    metadata = read_dump_metadata(sample_archive)
    assert metadata == {
        "TIMESTAMP": "2026-09-23 01:13:07.898407+00",
        "REPLICATION_SEQUENCE": "31",
        "SCHEMA_SEQUENCE": "189205",
    }

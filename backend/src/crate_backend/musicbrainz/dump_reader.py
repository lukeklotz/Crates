"""Streaming access to MusicBrainz JSON Data Dump archives (.tar.xz holding
mbdump/<entity> as JSON-lines plus small provenance files)."""

import json
import tarfile
from collections.abc import Iterator
from pathlib import Path
from typing import Any

_METADATA_FILES = frozenset({"TIMESTAMP", "SCHEMA_SEQUENCE", "REPLICATION_SEQUENCE"})


def stream_jsonl_from_tar(archive_path: Path, member_name: str) -> Iterator[dict[str, Any]]:
    """Yield one parsed JSON object per line of `member_name`, decompressing
    in a single streaming pass without extracting anything to disk."""
    with tarfile.open(archive_path, mode="r|xz") as tf:
        for member in tf:
            if member.name != member_name:
                continue
            extracted = tf.extractfile(member)
            if extracted is None:
                return
            for raw_line in extracted:
                line = raw_line.strip()
                if line:
                    yield json.loads(line)
            return


def read_dump_metadata(archive_path: Path) -> dict[str, str]:
    """Read TIMESTAMP/SCHEMA_SEQUENCE/REPLICATION_SEQUENCE. These precede the
    multi-GB data member in real dumps, so this stops early."""
    found: dict[str, str] = {}
    with tarfile.open(archive_path, mode="r|xz") as tf:
        for member in tf:
            if member.name in _METADATA_FILES:
                extracted = tf.extractfile(member)
                if extracted is not None:
                    found[member.name] = extracted.read().decode("utf-8").strip()
                if len(found) == len(_METADATA_FILES):
                    break
    return found

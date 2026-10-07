"""Files of the evaluation answer key (Phase 4, Milestone 3).

eval/seeds.json and eval/judgments.jsonl are committed; eval/pool.jsonl is
a working file. Judgments are keyed by (seed, candidate), never by
variant, so every present and future variant reuses them.

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
"""

import json
import os
import uuid
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from crate_backend.core.config import get_settings

# (seed album id, candidate album id)
Pair = tuple[uuid.UUID, uuid.UUID]

QUARTILES = ("top", "upper-mid", "lower-mid", "bottom")
GRADES = (0, 1, 2)


@dataclass(frozen=True)
class Seed:
    album_id: uuid.UUID
    title: str
    artist_name: str | None
    popularity_quartile: str


def eval_dir() -> Path:
    return Path(get_settings().eval_dir)


def popularity_quartile(popularity: float) -> str:
    """Album.popularity is a 0–1 Last.fm listener percentile."""
    if popularity >= 0.75:
        return "top"
    if popularity >= 0.5:
        return "upper-mid"
    if popularity >= 0.25:
        return "lower-mid"
    return "bottom"


def load_seeds(path: Path) -> list[Seed]:
    return [
        Seed(
            album_id=uuid.UUID(row["album_id"]),
            title=row["title"],
            artist_name=row["artist_name"],
            popularity_quartile=row["popularity_quartile"],
        )
        for row in json.loads(path.read_text())
    ]


def save_seeds(seeds: Iterable[Seed], path: Path) -> None:
    rows = [{**asdict(seed), "album_id": str(seed.album_id)} for seed in seeds]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")


def load_judgments(path: Path) -> dict[Pair, int]:
    """Grade per (seed, candidate). Later lines win, so a grade can be
    corrected by appending a new line."""
    grades: dict[Pair, int] = {}
    if not path.exists():
        return grades
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path} line {number}: not valid JSON ({error})") from error
        if row["grade"] not in GRADES:
            raise ValueError(f"{path} line {number}: grade must be 0, 1 or 2")
        grades[(uuid.UUID(row["seed_id"]), uuid.UUID(row["candidate_id"]))] = row["grade"]
    return grades


def judgment_line(
    seed_id: uuid.UUID, candidate_id: uuid.UUID, grade: int, graded_at: datetime | None = None
) -> str:
    return json.dumps(
        {
            "seed_id": str(seed_id),
            "candidate_id": str(candidate_id),
            "grade": grade,
            "graded_at": (graded_at or datetime.now(UTC)).isoformat(timespec="seconds"),
        }
    )


def append_line(path: Path, line: str) -> None:
    """Append one line. A file hand-edited without a final newline gets one
    first, so the new line never joins onto the last."""
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_newline = path.exists() and path.stat().st_size > 0 and not _ends_with_newline(path)
    with path.open("a") as file:
        file.write(("\n" if needs_newline else "") + line + "\n")


def _ends_with_newline(path: Path) -> bool:
    with path.open("rb") as file:
        file.seek(-1, os.SEEK_END)
        return file.read(1) == b"\n"


def remove_line(path: Path, line: str) -> bool:
    """Remove the last exact copy of `line` (the grader's undo). False if
    absent. Written to a temp file and renamed, so a crash mid-write never
    leaves the judgments file empty or cut short."""
    lines = path.read_text().splitlines()
    for index in range(len(lines) - 1, -1, -1):
        if lines[index] == line:
            del lines[index]
            temp = path.with_suffix(path.suffix + ".tmp")
            temp.write_text("".join(kept + "\n" for kept in lines))
            os.replace(temp, path)
            return True
    return False


def load_pool(path: Path) -> list[Pair]:
    pairs = []
    for line in path.read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            pairs.append((uuid.UUID(row["seed_id"]), uuid.UUID(row["candidate_id"])))
    return pairs


def save_pool(pairs: Iterable[Pair], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps({"seed_id": str(seed), "candidate_id": str(candidate)}) + "\n"
            for seed, candidate in pairs
        )
    )

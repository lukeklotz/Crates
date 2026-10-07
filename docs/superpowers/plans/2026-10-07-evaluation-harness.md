# Evaluation Harness (Phase 4, Milestone 3) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a hand-graded answer key and the tools around it (seed selection, pooling, a terminal grader, a scorer), so the overlap baseline and the TF-IDF variants can be compared on NDCG@10 and pooled Recall@10, overall and per popularity quartile.

**Architecture:** A new package `backend/src/crate_backend/evaluation/`. `store.py` reads and writes the committed answer-key files in top-level `eval/`. `seeds.py` proposes and swaps seed albums. `variants.py` names each recommender configuration and returns its top 10 for a seed. `pool.py` lists the (seed, candidate) pairs nobody has graded. `grade.py` is the terminal grader. `score.py` computes the metrics and writes a dated Markdown report. Database access is confined to small `load_*` functions; everything else is pure and tested without Postgres.

**Tech Stack:** Python 3.12+, SQLAlchemy 2 async + asyncpg, scikit-learn model files from Milestone 2 (`recommend/tfidf.py`), pytest + pytest-asyncio (auto mode), uv. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md`, section "Milestone 3 — Evaluation harness". Milestone 2's plan (`docs/superpowers/plans/2026-10-06-tfidf-recommender.md`) describes the model this harness evaluates.

## Deviations from the spec (each small; listed so a reviewer doesn't flag them)

1. **`evaluation/store.py` added** beside the spec's five modules. Seeds, judgments and the pool are read by several modules; one file owns their formats.
2. **New setting `eval_dir`** (env `CRATE_EVAL_DIR`, default `<repo>/eval`), mirroring `tfidf_model_path`, so the CLIs find `eval/` from any working directory.
3. **Broad-genre rules are written out** (`seeds.broad_genre`). The spec says "by the album's highest-voted genre" without a mapping. Rules match whole words of the normalized genre name, first rule wins (so "folk rock" is rock, "trip hop" is electronic, "contemporary r&b" is soul/R&B). Albums whose top genre maps to nothing ("experimental", "comedy", "christmas music") are not proposed. A scan on 2026-10-07 showed ambient (2,446), electronic (2,216) and rock (1,676) dominate top genres, so without buckets the proposal would be mostly ambient.
4. **Quotas 7/6/6/6** (top quartile gets the extra seed) and genres rotate across quartiles so each of the 10 genres gets 2 or 3 seeds. **No two seeds share an artist.** When a (quartile, genre) slot has no eligible album, the quartile fills from the other genres.
5. **Seeds with no candidate graded ≥ 1 are left out of NDCG@10 and Recall@10 averages** (both are undefined for them) and the report shows how many seeds were scored (`n/N`). The spec doesn't say.
6. **Judged@10's denominator is the number of results returned** (a variant can return fewer than 10). No results counts as fully judged.
7. **The grader reads one keypress without Enter** when stdin is a terminal (about 600 grades), and reads lines when input is piped. End of input quits. Ctrl-C quits too; every grade is already on disk.
8. **Stretch variants registered: α 0.4/0.8, no-reception, no-personnel, no-bigrams.** They need only model files built with existing flags. **SVD and MMR are not in this plan**: they need new model code, and the spec makes them optional after core grading. They get their own short plan if wanted.
9. **Popularity quartile labels** are `top` (≥ 0.75), `upper-mid` (≥ 0.5), `lower-mid` (≥ 0.25) and `bottom`, computed from `Album.popularity` (a 0–1 Last.fm listener percentile).
10. **Later judgment lines win.** A grade can be corrected by appending a new line by hand; the loader takes the last one for each pair.

## Global Constraints

- All backend commands run from `backend/` with `uv run ...`. Tests that touch Postgres use the `db_session` fixture, which rolls back. The dev database holds the real 25,000-album catalog: tests create their own albums (titles/terms prefixed `Zzfixture`) and assert only on those, passing `only=[...]` to loaders.
- Committed data in top-level `eval/`: `seeds.json` (list of `{album_id, title, artist_name, popularity_quartile}`, indented, UTF-8 not escaped), `judgments.jsonl` (one `{seed_id, candidate_id, grade, graded_at}` per line, `graded_at` UTC ISO 8601 to the second), `results/YYYY-MM-DD.md`. `eval/pool.jsonl` is a working file and gitignored.
- Judgments are keyed by (seed, candidate), never by variant.
- Rubric (exact): **2:** I'd recommend it to someone who loves the seed. **1:** Clearly related and plausible. **0:** Not relevant. Grade same-artist albums on their merits.
- Grader keys: `0`/`1`/`2` grade, `s` skip (stays in the pool), `u` undo the last grade made in this session, `q` quit. Candidates are shown per seed, in random order, with the producing variant hidden. Seed header: title, artist, year, top tags, first sentence of the Wikipedia lead. Candidate: title, artist, year, top 8 terms, first sentence of the lead.
- Seeds: 25, at least 5 normalized terms each (`merge_term_votes` count), non-null popularity, fixed random seed `2026`. Ten broad genres: jazz, rock, electronic, hip hop, metal, folk, pop, classical, soul/r&b, world.
- Core variants: `overlap`; `tfidf-tags` (α = 1.0); `tfidf-tags+text` (α = 0.6). Both TF-IDF variants read the default model file `settings.tfidf_model_path`; α is passed at scoring time.
- Metrics at K = 10: NDCG with gain `2^grade − 1`, ideal ranking from all graded pairs for the seed, ungraded results count 0. Pooled Recall = share of the seed's candidates graded ≥ 1 that are in the top 10. Judged@10 flagged (`⚠`) below 0.9. Median popularity of returned albums. Mean distinct artists in the top 10. Per-seed NDCG win/loss/tie for each pair of variants.
- The scorer only reports. Changing the API default is the owner's decision and its own commit.
- Ruff line length 100 (`uv run ruff check src tests`).
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Work directly on `main`; don't push.

## Review Focus

1. **Seeds edited after pooling** (the owner swaps a seed, then runs the grader on the old pool): pairs for seeds no longer in `seeds.json` must be skipped, not graded. Pinned in Task 5 (`test_pairs_for_seeds_no_longer_in_the_seeds_file_are_skipped`).
2. **A model rebuilt after grading** surfaces new, ungraded results: they must count as 0 and the row must carry the `⚠` flag, so a stale answer key can't quietly flatter or punish a variant. Pinned in Task 6 (`test_report_rows_overall_and_per_quartile_and_flags_unjudged_results`).
3. **Re-running `seeds propose` after the owner hand-edited `seeds.json`** must not overwrite their swaps without `--force`. Pinned in Task 2 (`test_write_proposal_refuses_to_overwrite_without_force`).
4. **Ctrl-C or end of input in the middle of grading:** every grade so far is kept and the next run resumes. Pinned in Task 5 (`test_ctrl_c_quits_and_keeps_grades`).
5. **A catalog thin in some genre/quartile slot** (e.g. no bottom-quartile classical album with 5 terms): the proposal still returns its quota from other genres instead of returning fewer seeds or crashing. Pinned in Task 2 (`test_fills_a_quartile_from_other_genres_when_one_runs_out`).

---

## File Structure

| File | Responsibility |
|---|---|
| `backend/src/crate_backend/core/config.py` (modify) | `eval_dir` setting |
| `backend/src/crate_backend/evaluation/__init__.py` (create) | empty package marker |
| `backend/src/crate_backend/evaluation/store.py` (create) | `Seed`, `Pair`, quartiles, seeds/judgments/pool file I/O |
| `backend/src/crate_backend/evaluation/seeds.py` (create) | `broad_genre`, `SeedCandidate`, `propose_seeds`, `load_seed_candidates`, `search_candidates`, `choose_and_swap`, CLI `propose` / `swap` |
| `backend/src/crate_backend/evaluation/variants.py` (create) | `Variant`, `VARIANTS`, `CORE_VARIANTS`, `parse_variant_names`, `top_k`, `run_variants`, `ModelNotBuilt` |
| `backend/src/crate_backend/evaluation/pool.py` (create) | `new_pairs`, CLI |
| `backend/src/crate_backend/evaluation/grade.py` (create) | `AlbumCard`, `first_sentence`, `load_cards`, `run_grader`, CLI |
| `backend/src/crate_backend/evaluation/score.py` (create) | metric functions, `AlbumFacts`, `build_report`, `load_facts`, CLI |
| `backend/tests/test_eval_store.py`, `test_eval_seeds.py`, `test_eval_variants_pool.py`, `test_eval_grade.py`, `test_eval_score.py` (create) | tests per module |
| `.gitignore` (modify) | ignore `/eval/pool.jsonl` |
| `eval/seeds.json`, `eval/judgments.jsonl`, `eval/results/*.md` (created by running the tools) | the answer key and reports |
| `docs/recommendation-systems.md` (modify) | how to run the harness; then real numbers |

---

### Task 1: Answer-key files and the `eval_dir` setting

**Files:**
- Create: `backend/src/crate_backend/evaluation/__init__.py`, `backend/src/crate_backend/evaluation/store.py`
- Modify: `backend/src/crate_backend/core/config.py`, `backend/tests/test_config.py`, `.gitignore`
- Test: `backend/tests/test_eval_store.py`

**Interfaces:**
- Consumes: `get_settings()`.
- Produces:
  - `Pair = tuple[uuid.UUID, uuid.UUID]` (seed id, candidate id)
  - `QUARTILES = ("top", "upper-mid", "lower-mid", "bottom")`
  - `@dataclass(frozen=True) Seed(album_id: uuid.UUID, title: str, artist_name: str | None, popularity_quartile: str)`
  - `eval_dir() -> Path`; `popularity_quartile(popularity: float) -> str`
  - `load_seeds(path) -> list[Seed]`; `save_seeds(seeds, path) -> None`
  - `load_judgments(path) -> dict[Pair, int]` (missing file → `{}`; later lines win; bad grade → `ValueError` naming the line)
  - `judgment_line(seed_id, candidate_id, grade, graded_at: datetime | None = None) -> str`
  - `append_line(path, line) -> None`; `remove_line(path, line) -> bool` (removes the last exact copy)
  - `load_pool(path) -> list[Pair]`; `save_pool(pairs, path) -> None`

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_eval_store.py`:

```python
import json
import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.evaluation.store import (
    Seed,
    append_line,
    judgment_line,
    load_judgments,
    load_pool,
    load_seeds,
    popularity_quartile,
    remove_line,
    save_pool,
    save_seeds,
)

A, B, C = (uuid.uuid5(uuid.NAMESPACE_URL, name) for name in ("a", "b", "c"))
AT = datetime(2026, 10, 7, 12, 0, tzinfo=UTC)


def test_seeds_round_trip_as_hand_editable_json(tmp_path):
    path = tmp_path / "eval" / "seeds.json"
    seeds = [Seed(A, "Kid A", "Radiohead", "top"), Seed(B, "Café Tacvba", None, "bottom")]

    save_seeds(seeds, path)

    assert load_seeds(path) == seeds
    assert json.loads(path.read_text())[0] == {
        "album_id": str(A),
        "title": "Kid A",
        "artist_name": "Radiohead",
        "popularity_quartile": "top",
    }
    assert "Café" in path.read_text()


@pytest.mark.parametrize(
    ("popularity", "quartile"),
    [
        (1.0, "top"),
        (0.75, "top"),
        (0.7499, "upper-mid"),
        (0.5, "upper-mid"),
        (0.25, "lower-mid"),
        (0.2499, "bottom"),
        (0.011, "bottom"),
    ],
)
def test_popularity_quartile(popularity, quartile):
    assert popularity_quartile(popularity) == quartile


def test_missing_judgments_file_means_no_judgments(tmp_path):
    assert load_judgments(tmp_path / "judgments.jsonl") == {}


def test_judgments_append_and_later_lines_win(tmp_path):
    path = tmp_path / "eval" / "judgments.jsonl"

    append_line(path, judgment_line(A, B, 2, AT))
    append_line(path, judgment_line(A, C, 0, AT))
    append_line(path, judgment_line(A, B, 1, AT))

    assert load_judgments(path) == {(A, B): 1, (A, C): 0}
    assert json.loads(path.read_text().splitlines()[0]) == {
        "seed_id": str(A),
        "candidate_id": str(B),
        "grade": 2,
        "graded_at": "2026-10-07T12:00:00+00:00",
    }


def test_judgments_skip_blank_lines_and_reject_bad_grades(tmp_path):
    path = tmp_path / "judgments.jsonl"
    path.write_text("\n" + judgment_line(A, B, 2, AT) + "\n\n")
    assert load_judgments(path) == {(A, B): 2}

    path.write_text(judgment_line(A, B, 3, AT) + "\n")
    with pytest.raises(ValueError, match="line 1"):
        load_judgments(path)


def test_remove_line_removes_only_the_last_exact_copy(tmp_path):
    path = tmp_path / "judgments.jsonl"
    first, other = judgment_line(A, B, 2, AT), judgment_line(A, C, 1, AT)
    for line in (first, other, first):
        append_line(path, line)

    assert remove_line(path, first)
    assert path.read_text().splitlines() == [first, other]
    assert not remove_line(path, judgment_line(B, C, 0, AT))
    assert path.read_text().splitlines() == [first, other]


def test_pool_round_trip(tmp_path):
    path = tmp_path / "eval" / "pool.jsonl"

    save_pool([(A, B), (A, C)], path)

    assert load_pool(path) == [(A, B), (A, C)]
```

Append to `backend/tests/test_config.py`:

```python
def test_eval_dir_defaults_to_repo_eval_folder():
    settings = Settings(_env_file=None)
    assert settings.eval_dir.endswith("/eval")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_store.py tests/test_config.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.evaluation'` and `AttributeError` on `eval_dir`.

- [ ] **Step 3: Implement**

In `backend/src/crate_backend/core/config.py`, after `tfidf_model_path`:

```python
    # Evaluation answer key (Phase 4, Milestone 3): seeds, judgments and
    # dated reports, committed to the repo.
    eval_dir: str = str(_REPO_ROOT / "eval")
```

Create an empty `backend/src/crate_backend/evaluation/__init__.py`.

`backend/src/crate_backend/evaluation/store.py`:

```python
"""Files of the evaluation answer key (Phase 4, Milestone 3).

eval/seeds.json and eval/judgments.jsonl are committed; eval/pool.jsonl is
a working file. Judgments are keyed by (seed, candidate), never by
variant, so every present and future variant reuses them.

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
"""

import json
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
        row = json.loads(line)
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
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as file:
        file.write(line + "\n")


def remove_line(path: Path, line: str) -> bool:
    """Remove the last exact copy of `line` (the grader's undo). False if absent."""
    lines = path.read_text().splitlines()
    for index in range(len(lines) - 1, -1, -1):
        if lines[index] == line:
            del lines[index]
            path.write_text("".join(kept + "\n" for kept in lines))
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
```

Append to `.gitignore`:

```
# Evaluation working file (rebuild with python -m crate_backend.evaluation.pool)
/eval/pool.jsonl
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_store.py tests/test_config.py -q && uv run ruff check src tests`
Expected: PASS, no lint errors.

- [ ] **Step 5: Commit**

```bash
git add .gitignore backend/src/crate_backend/core/config.py backend/src/crate_backend/evaluation backend/tests/test_eval_store.py backend/tests/test_config.py
git commit -m "feat: add evaluation answer-key files and eval_dir setting

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Seed proposal

**Files:**
- Create: `backend/src/crate_backend/evaluation/seeds.py`
- Test: `backend/tests/test_eval_seeds.py`

**Interfaces:**
- Consumes: `Seed`, `QUARTILES`, `popularity_quartile`, `save_seeds`, `eval_dir` (Task 1); `normalize_term`, `merge_term_votes` (`recommend/text_cleaning.py`); `async_session_factory`.
- Produces:
  - `GENRE_BUCKETS: tuple[str, ...]` (the 10 genres in rotation order); `MIN_TERMS = 5`; `RANDOM_SEED = 2026`; `QUOTAS = (("top", 7), ("upper-mid", 6), ("lower-mid", 6), ("bottom", 6))`
  - `broad_genre(name: str) -> str | None`
  - `@dataclass(frozen=True) SeedCandidate(album_id, title, artist_name: str | None, release_year: int | None, popularity: float | None, top_genre: str | None, n_terms: int)`
  - `is_eligible(candidate) -> bool` (popularity known and `n_terms >= MIN_TERMS`)
  - `seed_from(candidate) -> Seed`
  - `propose_seeds(candidates, *, quotas=QUOTAS, random_seed=RANDOM_SEED) -> list[Seed]`
  - `async load_seed_candidates(session, *, only: list[uuid.UUID] | None = None) -> list[SeedCandidate]` (ordered by album id)
  - `write_proposal(seeds, path, *, force: bool) -> None` (raises `FileExistsError` if `path` exists and not `force`)
  - CLI: `uv run python -m crate_backend.evaluation.seeds propose [--force]`

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_eval_seeds.py`:

```python
import uuid
from collections import Counter
from dataclasses import replace

import pytest

from crate_backend.evaluation.seeds import (
    GENRE_BUCKETS,
    SeedCandidate,
    broad_genre,
    load_seed_candidates,
    propose_seeds,
    write_proposal,
)
from crate_backend.evaluation.store import Seed
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag

POPULARITY = {"top": 0.9, "upper-mid": 0.6, "lower-mid": 0.3, "bottom": 0.1}
# One real-looking top genre per broad genre.
GENRE_NAMES = {
    "jazz": "Post-Bop",
    "rock": "Rock",
    "electronic": "Ambient",
    "hip hop": "Hip-Hop",
    "metal": "Black Metal",
    "folk": "Folk",
    "pop": "Pop",
    "classical": "Classical",
    "soul/r&b": "Soul",
    "world": "Reggae",
}


def cand(i: int, popularity: float | None, genre: str, *, n_terms=8, artist=None):
    key = f"{genre}-{popularity}-{i}"
    return SeedCandidate(
        album_id=uuid.uuid5(uuid.NAMESPACE_URL, key),
        title=f"Album {key}",
        artist_name=artist or f"Artist {key}",
        release_year=2000,
        popularity=popularity,
        top_genre=genre,
        n_terms=n_terms,
    )


def full_catalog() -> list[SeedCandidate]:
    return [
        cand(i, popularity, name)
        for popularity in POPULARITY.values()
        for name in GENRE_NAMES.values()
        for i in range(3)
    ]


@pytest.mark.parametrize(
    ("name", "bucket"),
    [
        ("Post-Bop", "jazz"),
        ("Avant-Garde Jazz", "jazz"),
        ("Heavy Metal", "metal"),
        ("Metalcore", "metal"),
        ("Trip Hop", "electronic"),
        ("Hip-Hop", "hip hop"),
        ("Gangsta Rap", "hip hop"),
        ("Dark Ambient", "electronic"),
        ("Dubstep", "electronic"),
        ("Contemporary R&B", "soul/r&b"),
        ("Blues", "soul/r&b"),
        ("Blues Rock", "rock"),
        ("Folk Rock", "rock"),
        ("Country", "folk"),
        ("Synth-Pop", "pop"),
        ("Dance-Pop", "pop"),
        ("K-Pop", "world"),
        ("Reggae", "world"),
        ("Modern Classical", "classical"),
        ("Post-Punk", "rock"),
        ("Experimental", None),
        ("Christmas Music", None),
    ],
)
def test_broad_genre(name, bucket):
    assert broad_genre(name) == bucket


def test_proposes_25_seeds_split_7_6_6_6_by_quartile():
    seeds = propose_seeds(full_catalog())

    assert len(seeds) == 25
    assert Counter(s.popularity_quartile for s in seeds) == {
        "top": 7,
        "upper-mid": 6,
        "lower-mid": 6,
        "bottom": 6,
    }


def test_spreads_seeds_across_all_ten_genres():
    by_id = {c.album_id: c for c in full_catalog()}

    counts = Counter(
        broad_genre(by_id[s.album_id].top_genre) for s in propose_seeds(full_catalog())
    )

    assert set(counts) == set(GENRE_BUCKETS)
    assert set(counts.values()) == {2, 3}


def test_proposal_is_deterministic_whatever_the_input_order():
    catalog = full_catalog()

    assert propose_seeds(catalog) == propose_seeds(list(reversed(catalog)))


def test_skips_few_terms_unknown_popularity_and_unmapped_genres():
    good = cand(0, 0.9, "Jazz")

    seeds = propose_seeds(
        [
            good,
            cand(1, 0.9, "Jazz", n_terms=4),
            replace(cand(2, 0.9, "Jazz"), popularity=None),
            cand(3, 0.9, "Experimental"),
            replace(cand(4, 0.9, "Jazz"), top_genre=None),
        ]
    )

    assert seeds == [Seed(good.album_id, good.title, good.artist_name, "top")]


def test_fills_a_quartile_from_other_genres_when_one_runs_out():
    catalog = [cand(i, 0.9, "Jazz") for i in range(10)] + [cand(0, 0.9, "Rock")]

    seeds = propose_seeds(catalog)

    assert len(seeds) == 7
    assert sum("Rock" in s.title for s in seeds) == 1


def test_never_picks_two_albums_by_the_same_artist():
    catalog = [cand(i, 0.9, "Jazz", artist="Same Artist") for i in range(5)]
    catalog += [cand(i, 0.9, "Rock", artist="same artist") for i in range(5)]
    catalog += [cand(i, 0.9, "Pop") for i in range(5)]

    seeds = propose_seeds(catalog)

    assert sum(s.artist_name.casefold() == "same artist" for s in seeds) == 1


def test_write_proposal_refuses_to_overwrite_without_force(tmp_path):
    path = tmp_path / "seeds.json"
    path.write_text("[]\n")
    seeds = propose_seeds(full_catalog())

    with pytest.raises(FileExistsError):
        write_proposal(seeds, path, force=False)
    assert path.read_text() == "[]\n"

    write_proposal(seeds, path, force=True)
    assert path.read_text() != "[]\n"


async def test_load_seed_candidates_merges_terms_and_picks_top_genre(db_session):
    album = Album(
        title="Zzfixture Seed Album", artist_name="Fixture Artist", popularity=0.8, release_year=1999
    )
    low = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Seed Low Genre")
    high = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Seed High Genre")
    same_as_high = Tag(name="zzfixture seed high genre")
    other = Tag(name="zzfixture seed other tag")
    db_session.add_all([album, low, high, same_as_high, other])
    await db_session.flush()
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=low.id, count=1),
            AlbumGenre(album_id=album.id, genre_id=high.id, count=4),
            AlbumTag(album_id=album.id, tag_id=same_as_high.id, count=9),
            AlbumTag(album_id=album.id, tag_id=other.id, count=2),
        ]
    )
    await db_session.flush()

    [candidate] = await load_seed_candidates(db_session, only=[album.id])

    assert candidate == SeedCandidate(
        album_id=album.id,
        title="Zzfixture Seed Album",
        artist_name="Fixture Artist",
        release_year=1999,
        popularity=0.8,
        top_genre="Zzfixture-Seed High Genre",
        n_terms=3,
    )
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_seeds.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.evaluation.seeds'`.

- [ ] **Step 3: Implement**

`backend/src/crate_backend/evaluation/seeds.py`:

```python
"""Seed albums for the evaluation answer key (Phase 4, Milestone 3).

`propose` picks 25 single-album seeds spread across popularity quartiles
and broad genres and writes eval/seeds.json. The owner then swaps any seed
they don't know well: grading is only as good as the grader's familiarity
with the seed.

Run with: uv run python -m crate_backend.evaluation.seeds propose [--force]
          uv run python -m crate_backend.evaluation.seeds swap N "title words" [--artist NAME]
"""

import argparse
import asyncio
import random
import re
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import (
    QUARTILES,
    Seed,
    eval_dir,
    popularity_quartile,
    save_seeds,
)
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.recommend.text_cleaning import merge_term_votes, normalize_term

GENRE_BUCKETS = (
    "jazz", "rock", "electronic", "hip hop", "metal",
    "folk", "pop", "classical", "soul/r&b", "world",
)  # fmt: skip
MIN_TERMS = 5
RANDOM_SEED = 2026
QUOTAS = (("top", 7), ("upper-mid", 6), ("lower-mid", 6), ("bottom", 6))

# Whole words of the normalized genre name; the first matching rule wins,
# so "folk rock" is rock and "trip hop" is electronic, not hip hop.
_GENRE_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("metal", ("metal", "metalcore", "grindcore", "deathcore")),
    ("electronic", ("trip hop",)),
    ("hip hop", ("hip hop", "rap", "trap", "boom bap", "grime", "drill")),
    ("jazz", ("jazz", "bop", "bebop", "big band")),
    ("classical", (
        "classical", "baroque", "opera", "symphony", "chamber music", "choral",
        "concerto", "romanticism", "minimalism",
    )),
    ("rock", ("rock",)),
    ("soul/r&b", (
        "soul", "r and b", "rhythm and blues", "funk", "disco", "gospel", "blues",
        "new jack swing", "motown",
    )),
    ("folk", ("folk", "country", "americana", "bluegrass", "singer songwriter")),
    ("world", (
        "reggae", "dub", "ska", "latin", "salsa", "cumbia", "samba", "bossa nova", "mpb",
        "afrobeat", "afrobeats", "highlife", "flamenco", "fado", "celtic", "world",
        "k pop", "j pop", "mandopop", "cantopop", "tango", "klezmer",
    )),
    ("electronic", (
        "electronic", "electronica", "ambient", "techno", "house", "electro", "electropop",
        "downtempo", "breakbeat", "breaks", "breakcore", "drum and bass", "jungle", "dubstep",
        "idm", "trance", "synthwave", "chillwave", "vaporwave", "industrial", "ebm",
        "chiptune", "drone", "glitch", "edm", "barber beats", "broken transmission",
    )),
    ("pop", ("pop",)),
    ("rock", (
        "punk", "emo", "grunge", "new wave", "no wave", "shoegaze", "indie", "garage",
        "psychedelic",
    )),
)  # fmt: skip
_GENRE_PATTERNS = tuple(
    (bucket, re.compile(r"\b(?:" + "|".join(re.escape(w) for w in words) + r")\b"))
    for bucket, words in _GENRE_RULES
)


@dataclass(frozen=True)
class SeedCandidate:
    album_id: uuid.UUID
    title: str
    artist_name: str | None
    release_year: int | None
    popularity: float | None
    # Highest-voted MusicBrainz genre name (ties by name); None without genres.
    top_genre: str | None
    # Distinct normalized genre/tag terms.
    n_terms: int


def broad_genre(name: str) -> str | None:
    normalized = normalize_term(name)
    for bucket, pattern in _GENRE_PATTERNS:
        if pattern.search(normalized):
            return bucket
    return None


def is_eligible(candidate: SeedCandidate) -> bool:
    return candidate.popularity is not None and candidate.n_terms >= MIN_TERMS


def seed_from(candidate: SeedCandidate) -> Seed:
    return Seed(
        album_id=candidate.album_id,
        title=candidate.title,
        artist_name=candidate.artist_name,
        popularity_quartile=popularity_quartile(candidate.popularity),
    )


def _artist_key(candidate: SeedCandidate) -> str:
    return (candidate.artist_name or "").casefold() or str(candidate.album_id)


def propose_seeds(
    candidates: list[SeedCandidate],
    *,
    quotas: tuple[tuple[str, int], ...] = QUOTAS,
    random_seed: int = RANDOM_SEED,
) -> list[Seed]:
    """Round-robin over genres within each quartile, one album per genre per
    turn. The genre order rotates between quartiles so each genre gets two
    or three seeds overall. No two seeds share an artist."""
    rng = random.Random(random_seed)
    pools: dict[tuple[str, str], list[SeedCandidate]] = {}
    for candidate in sorted(candidates, key=lambda c: str(c.album_id)):
        bucket = broad_genre(candidate.top_genre) if candidate.top_genre else None
        if bucket and is_eligible(candidate):
            key = (popularity_quartile(candidate.popularity), bucket)
            pools.setdefault(key, []).append(candidate)
    for pool in pools.values():
        rng.shuffle(pool)

    seeds: list[Seed] = []
    artists: set[str] = set()
    offset = 0
    for quartile, quota in quotas:
        order = GENRE_BUCKETS[offset:] + GENRE_BUCKETS[:offset]
        picked = 0
        progress = True
        while picked < quota and progress:
            progress = False
            for bucket in order:
                if picked == quota:
                    break
                pool = pools.get((quartile, bucket), [])
                while pool and _artist_key(pool[-1]) in artists:
                    pool.pop()
                if pool:
                    candidate = pool.pop()
                    artists.add(_artist_key(candidate))
                    seeds.append(seed_from(candidate))
                    picked += 1
                    progress = True
        offset = (offset + quota) % len(GENRE_BUCKETS)
    return seeds


async def load_seed_candidates(
    session: AsyncSession, *, only: list[uuid.UUID] | None = None
) -> list[SeedCandidate]:
    """Every album (or only those listed) with its term count and top genre,
    ordered by album id."""

    def restrict(query, album_id_column):
        return query if only is None else query.where(album_id_column.in_(only))

    albums = (
        await session.execute(
            restrict(
                select(
                    Album.id, Album.title, Album.artist_name, Album.release_year, Album.popularity
                ),
                Album.id,
            ).order_by(Album.id)
        )
    ).all()

    genre_votes: dict[uuid.UUID, list[tuple[str, int]]] = {}
    all_votes: dict[uuid.UUID, list[tuple[str, int]]] = {}
    genres = select(AlbumGenre.album_id, Genre.name, AlbumGenre.count).join(
        Genre, Genre.id == AlbumGenre.genre_id
    )
    for album_id, name, votes in await session.execute(restrict(genres, AlbumGenre.album_id)):
        genre_votes.setdefault(album_id, []).append((name, votes))
        all_votes.setdefault(album_id, []).append((name, votes))
    tags = select(AlbumTag.album_id, Tag.name, AlbumTag.count).join(Tag, Tag.id == AlbumTag.tag_id)
    for album_id, name, votes in await session.execute(restrict(tags, AlbumTag.album_id)):
        all_votes.setdefault(album_id, []).append((name, votes))

    def top_genre(album_id: uuid.UUID) -> str | None:
        votes = genre_votes.get(album_id)
        if not votes:
            return None
        return min(votes, key=lambda pair: (-pair[1], normalize_term(pair[0])))[0]

    return [
        SeedCandidate(
            album_id=album_id,
            title=title,
            artist_name=artist_name,
            release_year=release_year,
            popularity=popularity,
            top_genre=top_genre(album_id),
            n_terms=len(merge_term_votes(all_votes.get(album_id, []))),
        )
        for album_id, title, artist_name, release_year, popularity in albums
    ]


def write_proposal(seeds: list[Seed], path: Path, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"{path} already exists (it may hold your swaps). Use --force to replace it."
        )
    save_seeds(seeds, path)


def _print_seeds(seeds: list[Seed], write: Callable[[str], None] = print) -> None:
    for position, seed in enumerate(seeds, start=1):
        write(f"{position:2}. [{seed.popularity_quartile:9}] {seed.title} — {seed.artist_name}")


async def _propose(force: bool) -> None:
    async with async_session_factory() as session:
        candidates = await load_seed_candidates(session)
    seeds = propose_seeds(candidates)
    path = eval_dir() / "seeds.json"
    write_proposal(seeds, path, force=force)
    _print_seeds(seeds)
    per_quartile = {q: sum(s.popularity_quartile == q for s in seeds) for q in QUARTILES}
    print(f"\nWrote {len(seeds)} seeds to {path} ({per_quartile}).")
    print("Swap any you don't know well: ... seeds swap N \"title words\"")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Propose or swap evaluation seed albums.")
    commands = parser.add_subparsers(dest="command", required=True)
    propose = commands.add_parser("propose", help="write a fresh eval/seeds.json")
    propose.add_argument("--force", action="store_true", help="replace an existing seeds.json")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    if args.command == "propose":
        asyncio.run(_propose(args.force))


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_seeds.py -q && uv run ruff check src tests`
Expected: PASS. If `test_spreads_seeds_across_all_ten_genres` fails, check the rotation: offsets go 0 → 7 → 3 → 9, giving jazz, rock, electronic, hip hop and metal 3 seeds and the other five 2.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/evaluation/seeds.py backend/tests/test_eval_seeds.py
git commit -m "feat: propose evaluation seeds spread across popularity quartiles and genres

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Seed swap

**Files:**
- Modify: `backend/src/crate_backend/evaluation/seeds.py`
- Test: `backend/tests/test_eval_seeds.py` (append)

**Interfaces:**
- Consumes: everything in Task 2; `load_seeds`, `save_seeds`.
- Produces:
  - `async search_candidates(session, query: str, *, artist: str | None = None, limit: int = 20) -> list[SeedCandidate]` (title contains `query`, case-insensitive, optional artist filter; most popular first)
  - `choose_and_swap(seeds, position: int, matches, *, read_line: Callable[[str], str], write: Callable[[str], None]) -> list[Seed] | None` (1-based position; `None` means nothing changed)
  - CLI: `uv run python -m crate_backend.evaluation.seeds swap N "title words" [--artist NAME]`

- [ ] **Step 1: Write the failing tests**

Append to `backend/tests/test_eval_seeds.py` (add `choose_and_swap, search_candidates` to the import from `crate_backend.evaluation.seeds`):

```python
OLD = Seed(uuid.uuid5(uuid.NAMESPACE_URL, "old"), "Old Seed", "Old Artist", "top")
KEEP = Seed(uuid.uuid5(uuid.NAMESPACE_URL, "keep"), "Kept Seed", "Kept Artist", "bottom")


def swap(matches, answer: str, position: int = 1):
    out: list[str] = []
    result = choose_and_swap(
        [OLD, KEEP], position, matches, read_line=lambda prompt: answer, write=out.append
    )
    return result, "\n".join(out)


def test_swap_replaces_the_position_with_the_chosen_match():
    first, second = cand(0, 0.3, "Jazz"), cand(1, 0.6, "Jazz")

    result, text = swap([first, second], "2")

    assert result == [Seed(second.album_id, second.title, second.artist_name, "upper-mid"), KEEP]
    assert "1. " in text and "2. " in text


def test_swap_cancelled_with_enter_changes_nothing():
    result, _ = swap([cand(0, 0.3, "Jazz")], "")

    assert result is None


def test_swap_hides_ineligible_matches_and_current_seeds():
    eligible = cand(0, 0.3, "Jazz")
    already_seed = replace(cand(1, 0.3, "Jazz"), album_id=KEEP.album_id)
    few_terms = cand(2, 0.3, "Jazz", n_terms=2)

    result, text = swap([already_seed, few_terms, eligible], "1")

    assert result[0].album_id == eligible.album_id
    assert "2 matches hidden" in text


def test_swap_with_no_eligible_match_says_so():
    result, text = swap([cand(0, None, "Jazz")], "1")

    assert result is None
    assert "No eligible matches" in text


@pytest.mark.parametrize("answer", ["0", "5", "x"])
def test_swap_with_an_invalid_choice_changes_nothing(answer):
    result, text = swap([cand(0, 0.3, "Jazz")], answer)

    assert result is None
    assert "Not a choice" in text


def test_swap_position_out_of_range_is_an_error():
    with pytest.raises(ValueError, match="between 1 and 2"):
        swap([cand(0, 0.3, "Jazz")], "1", position=3)


async def test_search_candidates_matches_title_words_and_artist(db_session):
    wanted = Album(title="Zzfixture Swap Album", artist_name="Zzfixture Swap Artist")
    other = Album(title="Zzfixture Swap Album", artist_name="Someone Else")
    db_session.add_all([wanted, other])
    await db_session.flush()

    by_title = await search_candidates(db_session, "zzfixture SWAP")
    by_artist = await search_candidates(db_session, "zzfixture swap", artist="swap artist")

    assert {c.album_id for c in by_title} == {wanted.id, other.id}
    assert [c.album_id for c in by_artist] == [wanted.id]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_seeds.py -q`
Expected: FAIL with `ImportError: cannot import name 'choose_and_swap'`.

- [ ] **Step 3: Implement**

Add `load_seeds` to the `crate_backend.evaluation.store` import in `seeds.py`, then add (below `write_proposal`):

```python
async def search_candidates(
    session: AsyncSession, query: str, *, artist: str | None = None, limit: int = 20
) -> list[SeedCandidate]:
    """Albums whose title contains `query` (and artist name contains
    `artist`), case-insensitive, most popular first."""
    statement = select(Album.id).where(Album.title.icontains(query, autoescape=True))
    if artist:
        statement = statement.where(Album.artist_name.icontains(artist, autoescape=True))
    statement = statement.order_by(Album.popularity.desc().nulls_last(), Album.title).limit(limit)
    ids = list((await session.scalars(statement)).all())
    found = {c.album_id: c for c in await load_seed_candidates(session, only=ids)}
    return [found[album_id] for album_id in ids]


def choose_and_swap(
    seeds: list[Seed],
    position: int,
    matches: list[SeedCandidate],
    *,
    read_line: Callable[[str], str],
    write: Callable[[str], None],
) -> list[Seed] | None:
    """Ask which match replaces seed `position` (1-based). Returns the new
    seed list, or None if nothing changed."""
    if not 1 <= position <= len(seeds):
        raise ValueError(f"Seed position must be between 1 and {len(seeds)}")
    current = {seed.album_id for seed in seeds}
    choices = [m for m in matches if is_eligible(m) and m.album_id not in current]
    hidden = len(matches) - len(choices)
    if hidden:
        write(f"({hidden} matches hidden: already a seed, unknown popularity or < {MIN_TERMS} terms)")
    if not choices:
        write("No eligible matches.")
        return None
    for number, match in enumerate(choices, start=1):
        write(
            f"{number:2}. {match.title} — {match.artist_name} ({match.release_year or '?'}) "
            f"[{popularity_quartile(match.popularity)}, {match.n_terms} terms]"
        )
    old = seeds[position - 1]
    answer = read_line(f"Replace #{position} '{old.title}' with (number, Enter to cancel): ")
    if not answer.strip():
        return None
    if not answer.strip().isdigit() or not 1 <= int(answer) <= len(choices):
        write("Not a choice; nothing changed.")
        return None
    updated = list(seeds)
    updated[position - 1] = seed_from(choices[int(answer) - 1])
    return updated


async def _swap(position: int, query: str, artist: str | None) -> None:
    path = eval_dir() / "seeds.json"
    seeds = load_seeds(path)
    async with async_session_factory() as session:
        matches = await search_candidates(session, query, artist=artist)
    updated = choose_and_swap(seeds, position, matches, read_line=input, write=print)
    if updated is None:
        print("Nothing changed.")
        return
    save_seeds(updated, path)
    print(f"Swapped #{position}: {seeds[position - 1].title} → {updated[position - 1].title}")
    print("Grades for the old seed stay in judgments.jsonl; the scorer ignores them.")
```

Extend `parse_args` and `main`:

```python
    swap = commands.add_parser("swap", help="replace one seed with a searched album")
    swap.add_argument("position", type=int, help="seed number as listed by propose (1-based)")
    swap.add_argument("query", help="words from the album title")
    swap.add_argument("--artist", default=None, help="words from the artist name")
```

```python
def main() -> None:
    args = parse_args()
    if args.command == "propose":
        asyncio.run(_propose(args.force))
    else:
        asyncio.run(_swap(args.position, args.query, args.artist))
```

Also add a `list` subcommand so the owner can see positions before swapping:

```python
    commands.add_parser("list", help="print the current seeds with their positions")
```

and in `main`: `elif args.command == "list": _print_seeds(load_seeds(eval_dir() / "seeds.json"))`. Put the `list` branch before the final `else`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_seeds.py -q && uv run ruff check src tests`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/evaluation/seeds.py backend/tests/test_eval_seeds.py
git commit -m "feat: swap and list evaluation seeds from the terminal

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Variants and pooling

**Files:**
- Create: `backend/src/crate_backend/evaluation/variants.py`, `backend/src/crate_backend/evaluation/pool.py`
- Test: `backend/tests/test_eval_variants_pool.py`

**Interfaces:**
- Consumes: `Seed`, `Pair`, `load_seeds`, `load_judgments`, `save_pool`, `eval_dir` (Task 1); `recommend_by_overlap` (`recommend/overlap.py`); `recommend`, `load_model`, `TfidfModel` (`recommend/tfidf.py`); `get_settings`.
- Produces:
  - `TOP_K = 10`
  - `@dataclass(frozen=True) Variant(name: str, approach: str, model_file: str | None = None, build_flags: tuple[str, ...] = (), alpha: float | None = None)` with `model_path() -> Path` (the default model path when `model_file` is None, else that file name next to it)
  - `VARIANTS: dict[str, Variant]`; `CORE_VARIANTS = ("overlap", "tfidf-tags", "tfidf-tags+text")`
  - `parse_variant_names(text: str | None) -> list[Variant]` (None → core; unknown → `ValueError` listing known names)
  - `class ModelNotBuilt(Exception)`; `tfidf_model(variant) -> TfidfModel`
  - `async top_k(variant, session, seed_id, k=TOP_K) -> list[uuid.UUID]`
  - `async run_variants(variants, session, seeds, k=TOP_K) -> dict[str, dict[uuid.UUID, list[uuid.UUID]]]` (variant name → seed id → ranked album ids)
  - `pool.new_pairs(seeds, runs, judged) -> list[Pair]`
  - CLI: `uv run python -m crate_backend.evaluation.pool [--variants a,b,c]`

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_eval_variants_pool.py`:

```python
import uuid

import pytest

from crate_backend.core.config import Settings
from crate_backend.evaluation import variants
from crate_backend.evaluation.pool import new_pairs
from crate_backend.evaluation.store import Seed
from crate_backend.evaluation.variants import (
    CORE_VARIANTS,
    VARIANTS,
    ModelNotBuilt,
    parse_variant_names,
    top_k,
)
from crate_backend.models.catalog import Album, AlbumTag, Tag
from crate_backend.recommend.tfidf import AlbumDoc, build_model, save_model


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, A, B, C, D = (uid(n) for n in ("s1", "s2", "a", "b", "c", "d"))


@pytest.fixture
def model_path(tmp_path, monkeypatch):
    path = tmp_path / "models" / "tfidf.joblib"
    monkeypatch.setattr(
        variants, "get_settings", lambda: Settings(_env_file=None, tfidf_model_path=str(path))
    )
    return path


def test_core_variants_use_the_spec_alphas():
    assert CORE_VARIANTS == ("overlap", "tfidf-tags", "tfidf-tags+text")
    assert VARIANTS["overlap"].approach == "overlap"
    assert VARIANTS["tfidf-tags"].alpha == 1.0
    assert VARIANTS["tfidf-tags+text"].alpha == 0.6


def test_parse_variant_names():
    assert [v.name for v in parse_variant_names(None)] == list(CORE_VARIANTS)
    assert [v.name for v in parse_variant_names("overlap, tfidf-a0.4")] == [
        "overlap",
        "tfidf-a0.4",
    ]
    with pytest.raises(ValueError, match="tfidf-tags\\+text"):
        parse_variant_names("overlap,nope")


def test_core_tfidf_variants_share_the_default_model_and_stretch_files_sit_beside_it(model_path):
    assert VARIANTS["tfidf-tags"].model_path() == model_path
    assert VARIANTS["tfidf-a0.8"].model_path() == model_path
    assert VARIANTS["tfidf-no-reception"].model_path() == model_path.with_name(
        "tfidf-no-reception.joblib"
    )


async def test_missing_model_names_the_build_command(model_path):
    with pytest.raises(ModelNotBuilt, match="--no-reception"):
        await top_k(VARIANTS["tfidf-no-reception"], None, S1)


async def test_tfidf_variants_apply_their_alpha(model_path):
    seed = AlbumDoc(S1, "Seed", {"rock": 1}, text="glacial saxophone")
    tag_twin = AlbumDoc(A, "Tag Twin", {"rock": 1}, text="loud guitars")
    text_twin = AlbumDoc(B, "Text Twin", {"polka": 1}, text="glacial saxophone")
    save_model(build_model([seed, tag_twin, text_twin], min_df=1, max_df=1.0), model_path)

    assert await top_k(VARIANTS["tfidf-tags"], None, S1) == [A]
    assert await top_k(VARIANTS["tfidf-tags+text"], None, S1) == [A, B]


async def test_overlap_variant_ranks_from_the_database(db_session):
    seed = Album(title="Zzfixture Pool Seed", artist_name="Fixture Artist")
    match = Album(title="Zzfixture Pool Match", artist_name="Fixture Artist")
    tag = Tag(name="zzfixture-pool-term")
    db_session.add_all([seed, match, tag])
    await db_session.flush()
    db_session.add_all([AlbumTag(album_id=a.id, tag_id=tag.id) for a in (seed, match)])
    await db_session.flush()

    assert await top_k(VARIANTS["overlap"], db_session, seed.id) == [match.id]


def test_new_pairs_dedupes_across_variants_and_skips_judged():
    seeds = [Seed(S1, "One", "X", "top"), Seed(S2, "Two", "Y", "bottom")]
    runs = {"a": {S1: [A, B], S2: [C]}, "b": {S1: [B, D], S2: []}}

    pairs = new_pairs(seeds, runs, judged={(S1, A): 2})

    assert pairs == [(S1, c) for c in sorted([B, D], key=str)] + [(S2, C)]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_variants_pool.py -q`
Expected: FAIL with `ImportError` on `crate_backend.evaluation.pool`.

- [ ] **Step 3: Implement**

`backend/src/crate_backend/evaluation/variants.py`:

```python
"""Named recommender configurations compared by the evaluation harness
(Phase 4, Milestone 3).

α is applied at scoring time, so tfidf-tags, tfidf-tags+text and the α
sweep share one model file. Variants that change the text block need
their own file, built with the flags in `build_flags`.
"""

import uuid
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.evaluation.store import Seed
from crate_backend.recommend.overlap import recommend_by_overlap
from crate_backend.recommend.tfidf import TfidfModel, load_model, recommend

TOP_K = 10


@dataclass(frozen=True)
class Variant:
    name: str
    approach: str  # "overlap" | "tfidf"
    # TF-IDF only. None means the default model file (settings.tfidf_model_path).
    model_file: str | None = None
    build_flags: tuple[str, ...] = ()
    alpha: float | None = None

    def model_path(self) -> Path:
        default = Path(get_settings().tfidf_model_path)
        return default if self.model_file is None else default.with_name(self.model_file)


def _file_variant(name: str, flag: str) -> Variant:
    return Variant(name, "tfidf", model_file=f"{name}.joblib", build_flags=(flag,), alpha=0.6)


VARIANTS = {
    v.name: v
    for v in (
        Variant("overlap", "overlap"),
        Variant("tfidf-tags", "tfidf", alpha=1.0),
        Variant("tfidf-tags+text", "tfidf", alpha=0.6),
        # Stretch variants (spec: grade only after the core is graded).
        Variant("tfidf-a0.4", "tfidf", alpha=0.4),
        Variant("tfidf-a0.8", "tfidf", alpha=0.8),
        _file_variant("tfidf-no-reception", "--no-reception"),
        _file_variant("tfidf-no-personnel", "--no-personnel"),
        _file_variant("tfidf-no-bigrams", "--no-bigrams"),
    )
}
CORE_VARIANTS = ("overlap", "tfidf-tags", "tfidf-tags+text")


def parse_variant_names(text: str | None) -> list[Variant]:
    names = CORE_VARIANTS if text is None else [n.strip() for n in text.split(",") if n.strip()]
    unknown = [name for name in names if name not in VARIANTS]
    if unknown:
        raise ValueError(f"Unknown variants {unknown}; known: {', '.join(VARIANTS)}")
    return [VARIANTS[name] for name in names]


class ModelNotBuilt(Exception):
    pass


_models: dict[Path, TfidfModel] = {}


def tfidf_model(variant: Variant) -> TfidfModel:
    path = variant.model_path()
    if path not in _models:
        if not path.exists():
            flags = " ".join(variant.build_flags)
            raise ModelNotBuilt(
                f"{variant.name}: no model at {path}. Build it with: uv run python -m "
                f"crate_backend.scripts.build_tfidf_model --out {path} {flags}".rstrip()
            )
        _models[path] = load_model(path)
    return _models[path]


async def top_k(
    variant: Variant, session: AsyncSession | None, seed_id: uuid.UUID, k: int = TOP_K
) -> list[uuid.UUID]:
    """The variant's top k album ids for a single-album seed. `session` is
    only used by overlap."""
    if variant.approach == "overlap":
        return [r.album_id for r in await recommend_by_overlap(session, [seed_id], k)]
    model = tfidf_model(variant)
    return [r.album_id for r in recommend(model, [seed_id], k, alpha=variant.alpha)]


async def run_variants(
    variants: Iterable[Variant], session: AsyncSession, seeds: list[Seed], k: int = TOP_K
) -> dict[str, dict[uuid.UUID, list[uuid.UUID]]]:
    runs: dict[str, dict[uuid.UUID, list[uuid.UUID]]] = {}
    for variant in variants:
        runs[variant.name] = {
            seed.album_id: await top_k(variant, session, seed.album_id, k) for seed in seeds
        }
    return runs
```

`backend/src/crate_backend/evaluation/pool.py`:

```python
"""List the (seed, candidate) pairs nobody has graded yet (Phase 4,
Milestone 3).

Run with: uv run python -m crate_backend.evaluation.pool [--variants a,b,c]

Takes each variant's top 10 for every seed, drops pairs already in
eval/judgments.jsonl and writes the rest to eval/pool.jsonl for the
grader. Defaults to the core variants.
"""

import argparse
import asyncio
import uuid
from collections.abc import Collection, Mapping

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import (
    Pair,
    Seed,
    eval_dir,
    load_judgments,
    load_seeds,
    save_pool,
)
from crate_backend.evaluation.variants import ModelNotBuilt, parse_variant_names, run_variants


def new_pairs(
    seeds: list[Seed],
    runs: Mapping[str, Mapping[uuid.UUID, list[uuid.UUID]]],
    judged: Collection[Pair],
) -> list[Pair]:
    """Each ungraded (seed, candidate) pair once, in seed order, then
    candidate id order."""
    pairs: list[Pair] = []
    for seed in seeds:
        candidates = {c for by_seed in runs.values() for c in by_seed.get(seed.album_id, [])}
        pairs += [
            (seed.album_id, candidate)
            for candidate in sorted(candidates, key=str)
            if (seed.album_id, candidate) not in judged
        ]
    return pairs


async def _pool(variant_names: str | None) -> None:
    variants = parse_variant_names(variant_names)
    folder = eval_dir()
    seeds = load_seeds(folder / "seeds.json")
    judged = load_judgments(folder / "judgments.jsonl")
    async with async_session_factory() as session:
        runs = await run_variants(variants, session, seeds)
    for name, by_seed in runs.items():
        empty = [s.title for s in seeds if not by_seed[s.album_id]]
        if empty:
            print(f"Warning: {name} returned nothing for {', '.join(empty)}")
    pairs = new_pairs(seeds, runs, judged)
    save_pool(pairs, folder / "pool.jsonl")
    print(
        f"{len(pairs)} new pairs to grade across "
        f"{len({seed for seed, _ in pairs})} of {len(seeds)} seeds "
        f"({', '.join(v.name for v in variants)})."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the ungraded pairs to eval/pool.jsonl.")
    parser.add_argument("--variants", default=None, help="comma-separated; default: core three")
    args = parser.parse_args()
    try:
        asyncio.run(_pool(args.variants))
    except (ModelNotBuilt, ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_variants_pool.py -q && uv run ruff check src tests`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/evaluation/variants.py backend/src/crate_backend/evaluation/pool.py backend/tests/test_eval_variants_pool.py
git commit -m "feat: name evaluation variants and pool their ungraded results

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Terminal grader

**Files:**
- Create: `backend/src/crate_backend/evaluation/grade.py`
- Test: `backend/tests/test_eval_grade.py`

**Interfaces:**
- Consumes: `Seed`, `Pair`, `load_seeds`, `load_pool`, `load_judgments`, `judgment_line`, `append_line`, `remove_line`, `eval_dir` (Task 1); `merge_term_votes`; models `Album`, `AlbumGenre`, `AlbumTag`, `Genre`, `Tag`, `AlbumText`, `WIKIPEDIA_SOURCE`.
- Produces:
  - `RUBRIC: str`
  - `@dataclass(frozen=True) AlbumCard(title: str, artist_name: str | None, release_year: int | None, terms: list[str], lead: str)` (terms highest-voted first)
  - `first_sentence(article: str | None, max_chars: int = 300) -> str`
  - `async load_cards(session, album_ids) -> dict[uuid.UUID, AlbumCard]`
  - `run_grader(pool, seeds, cards, judgments_path, *, read_key: Callable[[], str], write: Callable[[str], None], rng: random.Random) -> int` (grades written this session)
  - CLI: `uv run python -m crate_backend.evaluation.grade`

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_eval_grade.py`:

```python
import random
import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.evaluation.grade import AlbumCard, first_sentence, load_cards, run_grader
from crate_backend.evaluation.store import Seed, append_line, judgment_line, load_judgments
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, S3, A, B, C = (uid(n) for n in ("s1", "s2", "s3", "a", "b", "c"))
SEEDS = [Seed(S1, "Seed One", "Artist", "top"), Seed(S2, "Seed Two", "Artist", "bottom")]


def card(title: str) -> AlbumCard:
    return AlbumCard(title, "Someone", 1999, ["jazz", "post bop"], f"{title} is an album.")


CARDS = {
    S1: card("Seed One"),
    S2: card("Seed Two"),
    A: card("Alpha"),
    B: card("Beta"),
    C: card("Gamma"),
}


def grade(path, keys, pool, cards=CARDS):
    out: list[str] = []
    remaining = iter(keys)

    def read_key() -> str:
        key = next(remaining)
        if isinstance(key, BaseException):
            raise key
        return key

    count = run_grader(
        pool, SEEDS, cards, path, read_key=read_key, write=out.append, rng=random.Random(0)
    )
    return count, "\n".join(out)


def test_shows_the_rubric_and_writes_each_grade_immediately(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", "0"], [(S1, A), (S1, B)])

    assert count == 2
    assert "I'd recommend it to someone who loves the seed" in text
    assert set(load_judgments(path)) == {(S1, A), (S1, B)}
    assert sorted(load_judgments(path).values()) == [0, 2]


def test_rerun_resumes_with_only_ungraded_pairs(tmp_path):
    path = tmp_path / "judgments.jsonl"
    grade(path, ["1", "q"], [(S1, A), (S1, B)])
    [first] = load_judgments(path)

    count, _ = grade(path, ["2"], [(S1, A), (S1, B)])

    assert count == 1
    judged = load_judgments(path)
    assert len(judged) == 2 and judged[first] == 1


def test_skip_leaves_the_pair_for_next_time(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, _ = grade(path, ["s", "2"], [(S1, A), (S1, B)])
    assert count == 1
    count, _ = grade(path, ["0"], [(S1, A), (S1, B)])

    assert count == 1
    assert sorted(load_judgments(path).values()) == [0, 2]


def test_undo_removes_the_last_grade_and_asks_again(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", "u", "1", "0"], [(S1, A), (S1, B)])

    assert count == 2
    assert len(path.read_text().splitlines()) == 2
    assert sorted(load_judgments(path).values()) == [0, 1]
    assert "Undid" in text


def test_undo_never_touches_grades_from_earlier_sessions(tmp_path):
    path = tmp_path / "judgments.jsonl"
    earlier = judgment_line(S2, C, 2, datetime(2026, 10, 1, tzinfo=UTC))
    append_line(path, earlier)

    count, text = grade(path, ["u", "q"], [(S1, A)])

    assert count == 0
    assert "Nothing to undo" in text
    assert path.read_text().splitlines() == [earlier]


def test_quit_reports_progress(tmp_path):
    count, text = grade(tmp_path / "j.jsonl", ["q"], [(S1, A), (S1, B)])

    assert count == 0
    assert "0 graded this session; 2 left" in text


def test_ctrl_c_quits_and_keeps_grades(tmp_path):
    path = tmp_path / "judgments.jsonl"

    count, text = grade(path, ["2", KeyboardInterrupt()], [(S1, A), (S1, B)])

    assert count == 1
    assert len(load_judgments(path)) == 1
    assert "1 graded this session; 1 left" in text


def test_unrecognized_key_asks_again(tmp_path):
    count, text = grade(tmp_path / "j.jsonl", ["x", "2"], [(S1, A)])

    assert count == 1
    assert "Unrecognized key" in text


def test_seed_header_once_per_seed_and_variant_never_shown(tmp_path):
    _, text = grade(tmp_path / "j.jsonl", ["0", "0", "0"], [(S1, A), (S2, C), (S1, B)])

    assert text.count("=== Seed") == 2
    assert text.index("Gamma") > max(text.index("Alpha"), text.index("Beta"))
    assert "overlap" not in text and "tfidf" not in text


def test_pairs_for_seeds_no_longer_in_the_seeds_file_are_skipped(tmp_path):
    count, _ = grade(tmp_path / "j.jsonl", [], [(S3, A)])

    assert count == 0


def test_candidates_missing_from_the_catalog_are_skipped_with_a_note(tmp_path):
    cards = {k: v for k, v in CARDS.items() if k != B}

    count, text = grade(tmp_path / "j.jsonl", ["2"], [(S1, B), (S1, A)], cards=cards)

    assert count == 1
    assert "no longer in the catalog" in text


@pytest.mark.parametrize(
    ("article", "sentence"),
    [
        (None, ""),
        ("Kid A is the fourth album. It came out in 2000.\n\n== Background ==\nX.",
         "Kid A is the fourth album."),
        ("A lead that wraps\nonto a second line. More.", "A lead that wraps onto a second line."),
        ("A lead without a full stop", "A lead without a full stop"),
        ("== Background ==\nNo lead at all.", ""),
        ("A" * 400 + ".", "A" * 299 + "…"),
    ],
)  # fmt: skip
def test_first_sentence(article, sentence):
    assert first_sentence(article) == sentence


async def test_load_cards_lists_terms_by_votes_and_reads_the_lead(db_session):
    album = Album(title="Zzfixture Card Album", artist_name="Card Artist", release_year=1965)
    bare = Album(title="Zzfixture Bare Card", artist_name="Card Artist")
    genre = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Card Genre")
    tag = Tag(name="zzfixture card tag")
    db_session.add_all([album, bare, genre, tag])
    await db_session.flush()
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=genre.id, count=1),
            AlbumTag(album_id=album.id, tag_id=tag.id, count=7),
            AlbumText(
                album_id=album.id,
                source=WIKIPEDIA_SOURCE,
                text="Card Album is a record. Second.\n\n== Personnel ==\nX – drums",
                fetched_at=datetime.now(UTC),
            ),
        ]
    )
    await db_session.flush()

    cards = await load_cards(db_session, [album.id, bare.id])

    assert cards[album.id] == AlbumCard(
        "Zzfixture Card Album",
        "Card Artist",
        1965,
        ["zzfixture card tag", "zzfixture card genre"],
        "Card Album is a record.",
    )
    assert cards[bare.id].terms == [] and cards[bare.id].lead == ""
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_grade.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.evaluation.grade'`.

- [ ] **Step 3: Implement**

`backend/src/crate_backend/evaluation/grade.py`:

```python
"""Terminal grader for the evaluation answer key (Phase 4, Milestone 3).

Run with: uv run python -m crate_backend.evaluation.grade

Shows each ungraded pair from eval/pool.jsonl, grouped by seed, in random
order and without saying which variant produced it. Every grade is
appended to eval/judgments.jsonl at once, so quitting (q, Ctrl-C) loses
nothing and the next run resumes.
"""

import asyncio
import random
import re
import sys
import uuid
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import (
    Pair,
    Seed,
    append_line,
    eval_dir,
    judgment_line,
    load_judgments,
    load_pool,
    load_seeds,
    remove_line,
)
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.recommend.text_cleaning import merge_term_votes

RUBRIC = """Grades:
  2  I'd recommend it to someone who loves the seed.
  1  Clearly related and plausible.
  0  Not relevant.
Grade same-artist albums on their merits.
Keys: 0/1/2 grade, s skip (stays in the pool), u undo last grade, q quit."""
PROMPT = "grade [0/1/2, s, u, q] > "
SEED_TERMS = 8
CANDIDATE_TERMS = 8

_HEADING_LINE = re.compile(r"^==.*==\s*$", re.MULTILINE)
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")


@dataclass(frozen=True)
class AlbumCard:
    title: str
    artist_name: str | None
    release_year: int | None
    # Normalized genre/tag terms, highest-voted first.
    terms: list[str]
    # First sentence of the Wikipedia lead; empty without an article.
    lead: str


def first_sentence(article: str | None, max_chars: int = 300) -> str:
    """The first sentence of an article's lead (the text before the first
    heading). Naive about abbreviations: "St. Vincent" ends a sentence."""
    if not article:
        return ""
    match = _HEADING_LINE.search(article)
    lead = " ".join((article[: match.start()] if match else article).split())
    end = _SENTENCE_END.search(lead)
    sentence = lead[: end.end()] if end else lead
    return sentence if len(sentence) <= max_chars else sentence[: max_chars - 1] + "…"


async def load_cards(
    session: AsyncSession, album_ids: Iterable[uuid.UUID]
) -> dict[uuid.UUID, AlbumCard]:
    """Cards for the albums still in the catalog; missing ids are left out."""
    ids = list(set(album_ids))
    albums = (
        await session.execute(
            select(Album.id, Album.title, Album.artist_name, Album.release_year).where(
                Album.id.in_(ids)
            )
        )
    ).all()
    votes: dict[uuid.UUID, list[tuple[str, int]]] = {}
    genres = (
        select(AlbumGenre.album_id, Genre.name, AlbumGenre.count)
        .join(Genre, Genre.id == AlbumGenre.genre_id)
        .where(AlbumGenre.album_id.in_(ids))
    )
    tags = (
        select(AlbumTag.album_id, Tag.name, AlbumTag.count)
        .join(Tag, Tag.id == AlbumTag.tag_id)
        .where(AlbumTag.album_id.in_(ids))
    )
    for query in (genres, tags):
        for album_id, name, count in await session.execute(query):
            votes.setdefault(album_id, []).append((name, count))
    texts = dict(
        (
            await session.execute(
                select(AlbumText.album_id, AlbumText.text).where(
                    AlbumText.album_id.in_(ids), AlbumText.source == WIKIPEDIA_SOURCE
                )
            )
        ).all()
    )

    def ranked_terms(album_id: uuid.UUID) -> list[str]:
        merged = merge_term_votes(votes.get(album_id, []))
        return sorted(merged, key=lambda term: (-merged[term], term))

    return {
        album_id: AlbumCard(
            title=title,
            artist_name=artist_name,
            release_year=release_year,
            terms=ranked_terms(album_id),
            lead=first_sentence(texts.get(album_id)),
        )
        for album_id, title, artist_name, release_year in albums
    }


def _describe(card: AlbumCard, n_terms: int) -> list[str]:
    lines = [f"{card.title} — {card.artist_name or '?'} ({card.release_year or '?'})"]
    lines.append("  " + (", ".join(card.terms[:n_terms]) or "(no tags)"))
    if card.lead:
        lines.append("  " + card.lead)
    return lines


def _seed_card(seed: Seed, cards: dict[uuid.UUID, AlbumCard]) -> AlbumCard:
    return cards.get(seed.album_id) or AlbumCard(seed.title, seed.artist_name, None, [], "")


def _ordered(
    pool: list[Pair], seeds: list[Seed], judged: dict[Pair, int], rng: random.Random
) -> list[Pair]:
    """Ungraded pairs for current seeds, in seed order, shuffled within a seed."""
    queue: list[Pair] = []
    for seed in seeds:
        pairs = [p for p in dict.fromkeys(pool) if p[0] == seed.album_id and p not in judged]
        rng.shuffle(pairs)
        queue += pairs
    return queue


def _ask(read_key: Callable[[], str], write: Callable[[str], None]) -> str:
    while True:
        write(PROMPT)
        key = read_key().strip().lower()
        if key in {"0", "1", "2", "s", "u", "q"}:
            return key
        write(f"Unrecognized key {key!r}.")


def run_grader(
    pool: list[Pair],
    seeds: list[Seed],
    cards: dict[uuid.UUID, AlbumCard],
    judgments_path: Path,
    *,
    read_key: Callable[[], str],
    write: Callable[[str], None],
    rng: random.Random,
) -> int:
    """Grade the pool's ungraded pairs. Returns how many grades were written."""
    seeds_by_id = {seed.album_id: seed for seed in seeds}
    queue = _ordered(pool, seeds, load_judgments(judgments_path), rng)
    pending = set(queue)
    written: list[tuple[Pair, str]] = []
    shown_seed: uuid.UUID | None = None
    position = 0
    seed_numbers = {seed.album_id: n for n, seed in enumerate(seeds, start=1)}

    write(RUBRIC)
    try:
        while position < len(queue):
            seed_id, candidate_id = queue[position]
            if candidate_id not in cards:
                write(f"(skipping {candidate_id}: no longer in the catalog)")
                position += 1
                continue
            if seed_id != shown_seed:
                seed_card = _seed_card(seeds_by_id[seed_id], cards)
                write("")
                write(f"=== Seed {seed_numbers[seed_id]}/{len(seeds)} ===")
                for line in _describe(seed_card, SEED_TERMS):
                    write(line)
                shown_seed = seed_id
            write("")
            write(f"[{len(pending) - len(written)} left]")
            for line in _describe(cards[candidate_id], CANDIDATE_TERMS):
                write(line)

            key = _ask(read_key, write)
            if key in {"0", "1", "2"}:
                line = judgment_line(seed_id, candidate_id, int(key))
                append_line(judgments_path, line)
                written.append(((seed_id, candidate_id), line))
                position += 1
            elif key == "s":
                position += 1
            elif key == "u":
                if not written:
                    write("Nothing to undo in this session.")
                    continue
                pair, line = written.pop()
                remove_line(judgments_path, line)
                queue.insert(position, pair)
                shown_seed = None
                write(f"Undid the grade for {cards[pair[1]].title}.")
            else:
                break
    except KeyboardInterrupt:
        write("")
    write(f"{len(written)} graded this session; {len(pending) - len(written)} left in the pool.")
    return len(written)


def _read_terminal_key() -> str:
    """One keypress without Enter when stdin is a terminal; otherwise one
    line. End of input quits."""
    if not sys.stdin.isatty():
        line = sys.stdin.readline()
        return line.strip()[:1] if line else "q"
    import termios
    import tty

    fd = sys.stdin.fileno()
    saved = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, saved)
    print(key)
    return key


async def _load(seeds: list[Seed], pool: list[Pair]) -> dict[uuid.UUID, AlbumCard]:
    ids = [s.album_id for s in seeds] + [candidate for _, candidate in pool]
    async with async_session_factory() as session:
        return await load_cards(session, ids)


def main() -> None:
    folder = eval_dir()
    pool_path = folder / "pool.jsonl"
    if not pool_path.exists():
        raise SystemExit("No eval/pool.jsonl yet: run python -m crate_backend.evaluation.pool")
    seeds = load_seeds(folder / "seeds.json")
    pool = load_pool(pool_path)
    cards = asyncio.run(_load(seeds, pool))
    run_grader(
        pool,
        seeds,
        cards,
        folder / "judgments.jsonl",
        read_key=_read_terminal_key,
        write=print,
        rng=random.Random(),
    )


if __name__ == "__main__":
    main()
```

Note on `[N left]`: `pending` counts pairs at the start of the session; subtracting grades written gives what's left, and a skip doesn't reduce it (the pair stays in the pool).

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_grade.py -q && uv run ruff check src tests`
Expected: PASS.

- [ ] **Step 5: Try it by hand on a throwaway pool**

```bash
cd backend && export CRATE_EVAL_DIR="$(mktemp -d)" && uv run python - <<'EOF'
import asyncio
from sqlalchemy import select
from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import Seed, save_pool, save_seeds, eval_dir
from crate_backend.models.catalog import Album

async def main():
    async with async_session_factory() as s:
        albums = (await s.scalars(select(Album).where(Album.artist_name == "Radiohead").limit(4))).all()
    seed, *rest = albums
    save_seeds([Seed(seed.id, seed.title, seed.artist_name, "top")], eval_dir() / "seeds.json")
    save_pool([(seed.id, a.id) for a in rest], eval_dir() / "pool.jsonl")
asyncio.run(main())
EOF
uv run python -m crate_backend.evaluation.grade
```

Expected: rubric, one seed header, candidates one at a time; single keypresses work without Enter; `u` re-asks; `q` prints progress. Then `rm -r "$CRATE_EVAL_DIR" && unset CRATE_EVAL_DIR`.

- [ ] **Step 6: Commit**

```bash
git add backend/src/crate_backend/evaluation/grade.py backend/tests/test_eval_grade.py
git commit -m "feat: add terminal grader for the evaluation answer key

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Scorer and report

**Files:**
- Create: `backend/src/crate_backend/evaluation/score.py`
- Test: `backend/tests/test_eval_score.py`

**Interfaces:**
- Consumes: `Seed`, `Pair`, `QUARTILES`, `load_seeds`, `load_judgments`, `eval_dir` (Task 1); `TOP_K`, `parse_variant_names`, `run_variants`, `tfidf_model`, `ModelNotBuilt` (Task 4).
- Produces:
  - `ndcg_at_k(ranked, grades, k=TOP_K) -> float | None` (None when the seed has no candidate graded ≥ 1)
  - `pooled_recall_at_k(ranked, grades, k=TOP_K) -> float | None`
  - `judged_at_k(ranked, grades, k=TOP_K) -> float`
  - `@dataclass(frozen=True) AlbumFacts(popularity: float | None, artist: str)`
  - `build_report(seeds, runs, grades: dict[Pair, int], facts, *, model_versions: dict[str, str], today: date, k=TOP_K) -> str` (Markdown)
  - `async load_facts(session, album_ids) -> dict[uuid.UUID, AlbumFacts]`
  - CLI: `uv run python -m crate_backend.evaluation.score [--variants a,b,c]` (prints the report and writes `eval/results/YYYY-MM-DD.md`)

- [ ] **Step 1: Write the failing tests**

`backend/tests/test_eval_score.py`:

```python
import uuid
from datetime import date

import pytest

from crate_backend.evaluation.score import (
    AlbumFacts,
    build_report,
    judged_at_k,
    ndcg_at_k,
    pooled_recall_at_k,
)
from crate_backend.evaluation.store import Seed


def uid(name: str) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_URL, name)


S1, S2, A, B, C, D, X = (uid(n) for n in ("s1", "s2", "a", "b", "c", "d", "x"))


def test_ndcg_matches_a_hand_computed_example():
    # DCG = 3/log2(2) + 0 + 1/log2(4) = 3.5
    # IDCG from grades [2, 2, 1, 0] = 3 + 3/log2(3) + 1/log2(4) = 5.392789...
    grades = {A: 2, B: 0, C: 1, D: 2}

    assert ndcg_at_k([A, B, C], grades) == pytest.approx(0.649014792)


def test_ungraded_results_count_as_zero():
    # [X ungraded, A=2]: DCG = 3/log2(3); IDCG = 3.
    assert ndcg_at_k([X, A], {A: 2}) == pytest.approx(0.630929754)
    assert judged_at_k([X, A], {A: 2}) == 0.5


def test_perfect_ranking_scores_one_and_only_the_top_k_counts():
    grades = {A: 2, B: 1}

    assert ndcg_at_k([A, B], grades) == pytest.approx(1.0)
    assert ndcg_at_k([X, A], grades, k=1) == 0.0


def test_seed_with_no_relevant_candidate_is_undefined():
    assert ndcg_at_k([A, B], {A: 0, B: 0}) is None
    assert pooled_recall_at_k([A, B], {A: 0, B: 0}) is None
    assert ndcg_at_k([A], {}) is None


def test_pooled_recall_counts_grades_of_one_or_more():
    grades = {A: 2, B: 0, C: 1, D: 2}

    assert pooled_recall_at_k([A, B, C], grades) == pytest.approx(2 / 3)


def test_judged_at_k_of_no_results_is_one():
    assert judged_at_k([], {A: 2}) == 1.0


def test_report_rows_overall_and_per_quartile_and_flags_unjudged_results():
    seeds = [Seed(S1, "One", "X", "top"), Seed(S2, "Two", "Y", "bottom")]
    runs = {"good": {S1: [A], S2: [C]}, "new": {S1: [B], S2: [C]}}
    grades = {(S1, A): 2, (S2, C): 1}
    facts = {
        A: AlbumFacts(0.9, "x"),
        B: AlbumFacts(0.5, "y"),
        C: AlbumFacts(0.1, "z"),
    }

    report = build_report(
        seeds,
        runs,
        grades,
        facts,
        model_versions={"new": "2026-10-06T00:00:00+00:00"},
        today=date(2026, 10, 8),
    )

    assert "| good | all | 2/2 | 1.000 | 1.000 | 1.00 | 0.50 | 1.0 |" in report
    # B is ungraded: S1 scores 0, S2 scores 1.
    assert "| new | all | 2/2 | 0.500 | 0.500 | 0.50 ⚠ | 0.30 | 1.0 |" in report
    assert "| good | top | 1/1 | 1.000 |" in report
    assert "| new | bottom | 1/1 | 1.000 |" in report
    assert "| good | upper-mid | 0/0 | – | – | – | – | – |" in report
    assert "| good vs new | 1 | 0 | 1 |" in report
    assert "new: model 2026-10-06T00:00:00+00:00" in report
    assert report.startswith("# Evaluation results 2026-10-08")


def test_report_ignores_judgments_for_seeds_no_longer_in_the_seeds_file():
    seeds = [Seed(S1, "One", "X", "top")]
    runs = {"only": {S1: [A]}}
    grades = {(S1, A): 2, (S2, B): 2}

    report = build_report(seeds, runs, grades, {}, model_versions={}, today=date(2026, 10, 8))

    assert "Judgments: 1 for the current 1 seeds" in report
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_eval_score.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'crate_backend.evaluation.score'`.

- [ ] **Step 3: Implement**

`backend/src/crate_backend/evaluation/score.py`:

```python
"""Score recommender variants against the answer key (Phase 4, Milestone 3).

Run with: uv run python -m crate_backend.evaluation.score [--variants a,b,c]

Recomputes every variant's top 10 for every seed, so a rebuilt model is
scored as it is now; results nobody graded count as 0 and lower
Judged@10, which the report flags. Prints a Markdown report and writes it
to eval/results/YYYY-MM-DD.md. The scorer only reports; choosing the API
default is the owner's decision.
"""

import argparse
import asyncio
import math
import statistics
import uuid
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import date
from itertools import combinations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.store import (
    QUARTILES,
    Pair,
    Seed,
    eval_dir,
    load_judgments,
    load_seeds,
)
from crate_backend.evaluation.variants import (
    TOP_K,
    ModelNotBuilt,
    parse_variant_names,
    run_variants,
    tfidf_model,
)
from crate_backend.models.catalog import Album

JUDGED_FLAG = 0.9
Runs = Mapping[uuid.UUID, list[uuid.UUID]]  # seed id -> ranked album ids


@dataclass(frozen=True)
class AlbumFacts:
    popularity: float | None
    # Case-folded artist name, used to count distinct artists.
    artist: str


def _dcg(gains: Iterable[int]) -> float:
    return sum((2**grade - 1) / math.log2(rank + 2) for rank, grade in enumerate(gains))


def ndcg_at_k(
    ranked: list[uuid.UUID], grades: Mapping[uuid.UUID, int], k: int = TOP_K
) -> float | None:
    """Gain 2^grade − 1, so a 2 is worth three 1s. The ideal ranking uses
    every graded candidate for the seed, whichever variant found it.
    None when no candidate is graded ≥ 1."""
    ideal = _dcg(sorted(grades.values(), reverse=True)[:k])
    if ideal == 0:
        return None
    return _dcg(grades.get(album_id, 0) for album_id in ranked[:k]) / ideal


def pooled_recall_at_k(
    ranked: list[uuid.UUID], grades: Mapping[uuid.UUID, int], k: int = TOP_K
) -> float | None:
    relevant = {album_id for album_id, grade in grades.items() if grade >= 1}
    if not relevant:
        return None
    return len(relevant & set(ranked[:k])) / len(relevant)


def judged_at_k(ranked: list[uuid.UUID], grades: Mapping[uuid.UUID, int], k: int = TOP_K) -> float:
    top = ranked[:k]
    return 1.0 if not top else sum(album_id in grades for album_id in top) / len(top)


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _fmt(value: float | None, digits: int) -> str:
    return "–" if value is None else f"{value:.{digits}f}"


def _artist(facts: Mapping[uuid.UUID, AlbumFacts], album_id: uuid.UUID) -> str:
    fact = facts.get(album_id)
    return fact.artist if fact and fact.artist else str(album_id)


def _row(
    name: str,
    group: str,
    seeds: list[Seed],
    runs: Runs,
    grades_by_seed: Mapping[uuid.UUID, dict[uuid.UUID, int]],
    facts: Mapping[uuid.UUID, AlbumFacts],
    k: int,
) -> str:
    ndcgs, recalls, judged, artists, popularities = [], [], [], [], []
    for seed in seeds:
        ranked = runs[seed.album_id][:k]
        grades = grades_by_seed.get(seed.album_id, {})
        if (ndcg := ndcg_at_k(ranked, grades, k)) is not None:
            ndcgs.append(ndcg)
            recalls.append(pooled_recall_at_k(ranked, grades, k))
        judged.append(judged_at_k(ranked, grades, k))
        artists.append(len({_artist(facts, album_id) for album_id in ranked}))
        popularities += [
            facts[a].popularity for a in ranked if a in facts and facts[a].popularity is not None
        ]
    judged_mean = _mean(judged)
    flag = " ⚠" if judged_mean is not None and judged_mean < JUDGED_FLAG else ""
    median = statistics.median(popularities) if popularities else None
    return (
        f"| {name} | {group} | {len(ndcgs)}/{len(seeds)} | {_fmt(_mean(ndcgs), 3)} | "
        f"{_fmt(_mean(recalls), 3)} | {_fmt(judged_mean, 2)}{flag} | {_fmt(median, 2)} | "
        f"{_fmt(_mean(artists), 1)} |"
    )


def _win_loss_tie(
    a: Runs, b: Runs, seeds: list[Seed], grades_by_seed, k: int
) -> tuple[int, int, int]:
    wins = losses = ties = 0
    for seed in seeds:
        grades = grades_by_seed.get(seed.album_id, {})
        score_a = ndcg_at_k(a[seed.album_id], grades, k)
        score_b = ndcg_at_k(b[seed.album_id], grades, k)
        if score_a is None or score_b is None:
            continue
        if abs(score_a - score_b) < 1e-9:
            ties += 1
        elif score_a > score_b:
            wins += 1
        else:
            losses += 1
    return wins, losses, ties


def build_report(
    seeds: list[Seed],
    runs: Mapping[str, Runs],
    grades: Mapping[Pair, int],
    facts: Mapping[uuid.UUID, AlbumFacts],
    *,
    model_versions: Mapping[str, str],
    today: date,
    k: int = TOP_K,
) -> str:
    seed_ids = {seed.album_id for seed in seeds}
    grades_by_seed: dict[uuid.UUID, dict[uuid.UUID, int]] = {}
    for (seed_id, candidate_id), grade in grades.items():
        if seed_id in seed_ids:
            grades_by_seed.setdefault(seed_id, {})[candidate_id] = grade
    n_judgments = sum(len(by_candidate) for by_candidate in grades_by_seed.values())

    lines = [
        f"# Evaluation results {today.isoformat()}",
        "",
        f"Seeds: {len(seeds)}. Judgments: {n_judgments} for the current {len(seeds)} seeds.",
    ]
    lines += [f"- {name}: model {version}" for name, version in model_versions.items()]
    lines += [
        "",
        f"Scored = seeds with at least one candidate graded ≥ 1 (NDCG@{k} and Recall@{k} "
        f"average over these). Ungraded results count as 0; ⚠ marks Judged@{k} < "
        f"{JUDGED_FLAG}: run the pool and grader before trusting that row.",
        "",
        f"| Variant | Group | Scored | NDCG@{k} | Recall@{k} | Judged@{k} | Median pop. "
        f"| Artists in top {k} |",
        "|---|---|---|---|---|---|---|---|",
    ]
    groups = [("all", seeds)] + [
        (quartile, [s for s in seeds if s.popularity_quartile == quartile])
        for quartile in QUARTILES
    ]
    for group, group_seeds in groups:
        for name, by_seed in runs.items():
            lines.append(_row(name, group, group_seeds, by_seed, grades_by_seed, facts, k))

    lines += [
        "",
        f"Per-seed NDCG@{k}, first variant vs second:",
        "",
        "| Pair | Wins | Losses | Ties |",
        "|---|---|---|---|",
    ]
    for a, b in combinations(runs, 2):
        wins, losses, ties = _win_loss_tie(runs[a], runs[b], seeds, grades_by_seed, k)
        lines.append(f"| {a} vs {b} | {wins} | {losses} | {ties} |")
    return "\n".join(lines) + "\n"


async def load_facts(
    session: AsyncSession, album_ids: Iterable[uuid.UUID]
) -> dict[uuid.UUID, AlbumFacts]:
    rows = await session.execute(
        select(Album.id, Album.popularity, Album.artist_name).where(
            Album.id.in_(list(set(album_ids)))
        )
    )
    return {
        album_id: AlbumFacts(popularity, (artist_name or "").casefold())
        for album_id, popularity, artist_name in rows
    }


async def _score(variant_names: str | None) -> None:
    variants = parse_variant_names(variant_names)
    folder = eval_dir()
    seeds = load_seeds(folder / "seeds.json")
    grades = load_judgments(folder / "judgments.jsonl")
    async with async_session_factory() as session:
        runs = await run_variants(variants, session, seeds)
        returned = {a for by_seed in runs.values() for ranked in by_seed.values() for a in ranked}
        facts = await load_facts(session, returned)
    model_versions = {
        v.name: tfidf_model(v).metadata["model_version"] for v in variants if v.approach == "tfidf"
    }
    today = date.today()
    report = build_report(seeds, runs, grades, facts, model_versions=model_versions, today=today)
    path = folder / "results" / f"{today.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report)
    print(report)
    print(f"Wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score variants against eval/judgments.jsonl.")
    parser.add_argument("--variants", default=None, help="comma-separated; default: core three")
    args = parser.parse_args()
    try:
        asyncio.run(_score(args.variants))
    except (ModelNotBuilt, ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()
```

Check of the report test's expected numbers: `new`/all: S1 ranks only B (ungraded) → NDCG 0, recall 0, judged 0; S2 ranks C (graded 1) → NDCG 1, recall 1, judged 1. Means 0.500 / 0.500 / 0.50 (flagged). Popularities 0.5 and 0.1 → median 0.30. One artist per seed → 1.0. `good vs new`: S1 good 1.0 > 0.0 (win), S2 tie.

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_eval_score.py -q && uv run ruff check src tests`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add backend/src/crate_backend/evaluation/score.py backend/tests/test_eval_score.py
git commit -m "feat: score variants by NDCG@10 and pooled recall with a dated report

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Propose real seeds, document the workflow, checkpoint

**Files:**
- Create: `eval/seeds.json` (by running the tool)
- Modify: `docs/recommendation-systems.md`

**Interfaces:**
- Consumes: Tasks 1–6.
- Produces: a committed seed list the owner has approved; a "How to run" subsection in the docs.

- [ ] **Step 1: Full test suite and lint**

Run: `cd backend && uv run pytest -q && uv run ruff check src tests`
Expected: all pass.

- [ ] **Step 2: Propose seeds on the real catalog**

Run: `cd backend && uv run python -m crate_backend.evaluation.seeds propose`
Expected: 25 numbered seeds, 7/6/6/6 by quartile, written to `eval/seeds.json`. If fewer than 25, report which quartile came up short.

- [ ] **Step 3: Add "How to run" to the Evaluation section of `docs/recommendation-systems.md`**

Replace the paragraph starting "Both Recall@K and NDCG@K need an **answer key**" with:

1. One paragraph: the answer key lives in `eval/` (`seeds.json`, `judgments.jsonl`, `results/`); judgments are keyed by (seed, candidate) so every variant, including Phase 5's, reuses them; the rubric (2/1/0, exact wording from Global Constraints).
2. The workflow as a numbered list of commands (all from `backend/`): `seeds propose` → `seeds list` / `seeds swap N "title" [--artist ...]` → `pool [--variants ...]` → `grade` (keys) → `score [--variants ...]`.
3. Metric definitions as used here: NDCG@10 with gain 2^grade − 1; pooled Recall@10; Judged@10 and the ⚠ flag; median popularity; distinct artists; win/loss/tie. Note that seeds with no relevant candidate are left out of the averages.
4. Variants table: name, what it changes, model file, how to build it (from `VARIANTS`).
5. Keep "**No approach has been measured yet.**" until Task 8.

- [ ] **Step 4: Checkpoint with the owner: review the seeds**

Show the 25 seeds (`seeds list`). Ask the owner to swap any they don't know well enough to grade. Point out that the bottom quartile will likely be unfamiliar; for those seeds they can grade from the tags and lead sentence the grader shows, or swap toward bottom-quartile albums they do know (search with `seeds swap`). Run swaps the owner asks for. Wait for approval.

- [ ] **Step 5: Commit**

```bash
git add eval/seeds.json docs/recommendation-systems.md
git commit -m "docs: add evaluation workflow and the reviewed seed list

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

- [ ] **Step 6: Pool the core variants and hand over grading**

Run: `cd backend && uv run python -m crate_backend.evaluation.pool`
Expected: about 500–600 new pairs across 25 seeds (no `ModelNotBuilt`; `models/tfidf.joblib` exists from Milestone 2). Tell the owner the count and the command to run in their own terminal (`cd backend && uv run python -m crate_backend.evaluation.grade`); the grader needs single keypresses, so it must run in their terminal, not through the agent. About 1.5–2 hours, splittable. Stop here until the owner says grading is done.

---

### Task 8: Score, record results, decide the default (after grading)

**Files:**
- Create: `eval/results/YYYY-MM-DD.md` (by running the tool), `eval/judgments.jsonl` (written by the owner's grading)
- Modify: `docs/recommendation-systems.md`

- [ ] **Step 1: Confirm grading is complete**

Run: `cd backend && uv run python -m crate_backend.evaluation.pool`
Expected: `0 new pairs to grade`. If not, the owner finishes grading first.

- [ ] **Step 2: Score**

Run: `cd backend && uv run python -m crate_backend.evaluation.score`
Expected: no ⚠ flags; a table for `overlap`, `tfidf-tags`, `tfidf-tags+text` over all seeds and each quartile, plus win/loss/tie.

- [ ] **Step 3: Update `docs/recommendation-systems.md`**

1. Evaluation section: replace "No approach has been measured yet." with the dated overall and per-quartile tables (copy from the report), the win/loss/tie counts, and 3–5 sentences of plain-language reading: does TF-IDF beat Jaccard; does text help over tags alone; where (which quartiles); any sign of the text-vs-tag scale risk (median popularity of `tfidf-tags+text` vs `tfidf-tags`) or same-artist crowding (distinct artists).
2. Summary table: "Evaluated?" column for approaches 1 and 2 → "Yes, YYYY-MM-DD (NDCG@10 x.xx)".
3. Section 2 "Known limitations": replace "not yet evaluated" with the measured finding.

- [ ] **Step 4: Commit the answer key, report and docs**

```bash
git add eval/judgments.jsonl eval/results docs/recommendation-systems.md
git commit -m "docs: record the first evaluation of overlap vs TF-IDF

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

- [ ] **Step 5: Checkpoint: the owner decides the default**

Present the spec's suggested rule: make `tfidf` (with the winning α) the default if it beats `overlap` on NDCG@10 overall **and** doesn't lose in the bottom quartile. Give the numbers against that rule and a recommendation. If the owner says change it, that is a separate commit: change the `approach` default in `api/routes/recommendations.py` (and, if the winning α isn't 0.6, rebuild the model with `--alpha`), update the API test that asserts the default, and record the decision with its numbers in `docs/recommendation-systems.md`. Then ask whether to run any stretch variants (α 0.4/0.8, no-reception, no-personnel, no-bigrams: build files with the flags shown in the docs table, `pool --variants ...`, grade the new pairs, `score --variants ...`).

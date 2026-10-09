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
from datetime import date, datetime
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
    model_version,
    parse_variant_names,
    run_variants,
)
from crate_backend.models.catalog import Album

JUDGED_FLAG = 0.9
Runs = Mapping[uuid.UUID, list[uuid.UUID]]  # seed id -> ranked album ids
GradesBySeed = Mapping[uuid.UUID, Mapping[uuid.UUID, int]]


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
    grades_by_seed: GradesBySeed,
    facts: Mapping[uuid.UUID, AlbumFacts],
    k: int,
) -> str:
    ndcgs: list[float] = []
    recalls: list[float] = []
    judged: list[float] = []
    artists: list[float] = []
    popularities: list[float] = []
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
    # Flag on the worst seed, not the mean: ungraded results bunched in one
    # seed understate that seed's NDCG even when the row average looks fine.
    flag = " ⚠" if judged and min(judged) < JUDGED_FLAG else ""
    median = statistics.median(popularities) if popularities else None
    return (
        f"| {name} | {group} | {len(ndcgs)}/{len(seeds)} | {_fmt(_mean(ndcgs), 3)} | "
        f"{_fmt(_mean(recalls), 3)} | {_fmt(judged_mean, 2)}{flag} | {_fmt(median, 2)} | "
        f"{_fmt(_mean(artists), 1)} |"
    )


def _win_loss_tie(
    a: Runs, b: Runs, seeds: list[Seed], grades_by_seed: GradesBySeed, k: int
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
        (
            f"Scored = seeds with at least one candidate graded ≥ 1 (NDCG@{k} and Recall@{k} "
            f"average over these). Ungraded results count as 0; ⚠ marks a row where any seed's "
            f"Judged@{k} is below {JUDGED_FLAG}: run the pool and grader before trusting it."
        ),
        "",
        (
            f"| Variant | Group | Scored | NDCG@{k} | Recall@{k} | Judged@{k} | Median pop. "
            f"| Artists in top {k} |"
        ),
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
    model_versions = {v.name: version for v in variants if (version := model_version(v))}
    # The owner's local date names the report file.
    today = datetime.now().astimezone().date()
    report = build_report(seeds, runs, grades, facts, model_versions=model_versions, today=today)
    path = folder / "results" / f"{today.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report)
    print(report)
    print(f"Wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score variants against eval/judgments.jsonl.")
    parser.add_argument(
        "--variants", default=None, help="comma-separated; default: the five core variants"
    )
    args = parser.parse_args()
    try:
        asyncio.run(_score(args.variants))
    except (ModelNotBuilt, ValueError, FileNotFoundError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()

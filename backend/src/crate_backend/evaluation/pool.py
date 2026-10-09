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
    parser.add_argument(
        "--variants", default=None, help="comma-separated; default: the five core variants"
    )
    args = parser.parse_args()
    try:
        asyncio.run(_pool(args.variants))
    except (ModelNotBuilt, ValueError, FileNotFoundError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()

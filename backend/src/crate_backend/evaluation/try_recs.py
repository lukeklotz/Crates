"""Try a recommender by hand: pick a seed album, see its top matches.

Run with: uv run python -m crate_backend.evaluation.try_recs "heaven or las vegas" \
              [--artist NAME] [--approach overlap|tfidf|embeddings|all] [--limit 10]

Uses the same models and scoring the API serves (the model's own alpha), so
what you see here is what `POST /recommendations` returns. `--approach all`
prints the three lists one after another for comparison.
"""

import argparse
import asyncio
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.db.session import async_session_factory
from crate_backend.evaluation.seeds import SeedCandidate, search_candidates
from crate_backend.evaluation.variants import (
    ModelNotBuilt,
    Variant,
    embedding_model,
    model_version,
    tfidf_model,
)
from crate_backend.models.catalog import Album
from crate_backend.recommend import embeddings, tfidf
from crate_backend.recommend.overlap import recommend_by_overlap

APPROACHES = ("overlap", "tfidf", "embeddings")


def pick_seed(matches: list[SeedCandidate], query: str) -> SeedCandidate:
    if not matches:
        raise SystemExit(f"No album title contains '{query}'.")
    if len(matches) > 1:
        print("Several albums match; using the most popular. Narrow with --artist:")
        for match in matches[:5]:
            print(f"  {match.title} — {match.artist_name} ({match.release_year})")
        print()
    return matches[0]


async def ranked(
    approach: str, session: AsyncSession, seed_id: uuid.UUID, limit: int
) -> list[tuple[uuid.UUID, float, list[str], list[str]]]:
    """(album id, score, shared tags, shared article terms) per result."""
    variant = Variant(approach, approach)
    if approach == "overlap":
        return [
            (r.album_id, r.score, r.shared_terms, [])
            for r in await recommend_by_overlap(session, [seed_id], limit)
        ]
    if approach == "embeddings":
        model = embedding_model(variant)
        return [
            (r.album_id, r.score, r.shared_terms, [])
            for r in embeddings.recommend(model, [seed_id], limit)
        ]
    model = tfidf_model(variant)
    return [
        (r.album_id, r.score, r.shared_terms, r.shared_text_terms)
        for r in tfidf.recommend(model, [seed_id], limit)
    ]


async def show(approach: str, session: AsyncSession, seed: SeedCandidate, limit: int) -> None:
    version = model_version(Variant(approach, approach))
    print(f"== {approach}" + (f" (model built {version})" if version else ""))
    results = await ranked(approach, session, seed.album_id, limit)
    if not results:
        print("  no results (seed has no terms or is not in the model)\n")
        return
    albums = {
        a.id: a
        for a in await session.scalars(
            select(Album).where(Album.id.in_([album_id for album_id, *_ in results]))
        )
    }
    for position, (album_id, score, tags, text_terms) in enumerate(results, start=1):
        album = albums[album_id]
        print(f"{position:2}. {score:.3f}  {album.title} — {album.artist_name} ({album.release_year})")
        if tags:
            print(f"      tags: {', '.join(tags)}")
        if text_terms:
            print(f"      text: {', '.join(text_terms)}")
    print()


async def _run(query: str, artist: str | None, approach: str, limit: int) -> None:
    async with async_session_factory() as session:
        seed = pick_seed(await search_candidates(session, query, artist=artist), query)
        print(f"Seed: {seed.title} — {seed.artist_name} ({seed.release_year})\n")
        for name in APPROACHES if approach == "all" else (approach,):
            await show(name, session, seed, limit)


def main() -> None:
    parser = argparse.ArgumentParser(description="Show a seed album's recommendations.")
    parser.add_argument("query", help="words from the album title")
    parser.add_argument("--artist", default=None, help="words from the artist name")
    parser.add_argument("--approach", choices=(*APPROACHES, "all"), default="all")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    try:
        asyncio.run(_run(args.query, args.artist, args.approach, args.limit))
    except ModelNotBuilt as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()

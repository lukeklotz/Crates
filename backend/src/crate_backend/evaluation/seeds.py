"""Seed albums for the evaluation answer key (Phase 4, Milestone 3).

`propose` picks 25 single-album seeds spread across popularity quartiles
and broad genres and writes eval/seeds.json. The owner then swaps any seed
they don't know well: grading is only as good as the grader's familiarity
with the seed.

Run with: uv run python -m crate_backend.evaluation.seeds propose [--force]
          uv run python -m crate_backend.evaluation.seeds list
          uv run python -m crate_backend.evaluation.seeds swap N "title words" [--artist NAME]

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md
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
    load_seeds,
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
        write(
            f"({hidden} matches hidden: already a seed, unknown popularity or < {MIN_TERMS} terms)"
        )
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
    print('Swap any you don\'t know well: ... seeds swap N "title words"')


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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Propose or swap evaluation seed albums.")
    commands = parser.add_subparsers(dest="command", required=True)
    propose = commands.add_parser("propose", help="write a fresh eval/seeds.json")
    propose.add_argument("--force", action="store_true", help="replace an existing seeds.json")
    commands.add_parser("list", help="print the current seeds with their positions")
    swap = commands.add_parser("swap", help="replace one seed with a searched album")
    swap.add_argument("position", type=int, help="seed number as listed by `list` (1-based)")
    swap.add_argument("query", help="words from the album title")
    swap.add_argument("--artist", default=None, help="words from the artist name")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    try:
        if args.command == "propose":
            asyncio.run(_propose(args.force))
        elif args.command == "list":
            _print_seeds(load_seeds(eval_dir() / "seeds.json"))
        else:
            asyncio.run(_swap(args.position, args.query, args.artist))
    except (FileExistsError, FileNotFoundError, ValueError) as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()

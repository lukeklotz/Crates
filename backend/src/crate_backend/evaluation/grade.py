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
KEYS = {"0", "1", "2", "s", "u", "q"}

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
    unique = list(dict.fromkeys(pool))
    queue: list[Pair] = []
    for seed in seeds:
        pairs = [p for p in unique if p[0] == seed.album_id and p not in judged]
        rng.shuffle(pairs)
        queue += pairs
    return queue


def _ask(read_key: Callable[[], str], write: Callable[[str], None]) -> str:
    while True:
        write(PROMPT)
        key = read_key().strip().lower()
        if key in KEYS:
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
    seed_numbers = {seed.album_id: n for n, seed in enumerate(seeds, start=1)}
    queue = _ordered(pool, seeds, load_judgments(judgments_path), rng)
    n_pending = len(queue)
    written: list[tuple[Pair, str]] = []
    shown_seed: uuid.UUID | None = None
    position = 0

    def undo() -> None:
        nonlocal shown_seed
        pair, line = written.pop()
        remove_line(judgments_path, line)
        queue.insert(position, pair)
        shown_seed = None
        write(f"Undid the grade for {cards[pair[1]].title}.")

    write(RUBRIC)
    try:
        while True:
            if position >= len(queue):
                # One last chance to undo a mis-keyed final grade.
                if not written:
                    break
                write("")
                write("That was the last pair: u to undo the last grade, any other key to finish.")
                if read_key().strip().lower() != "u":
                    break
                undo()
                continue
            seed_id, candidate_id = queue[position]
            if candidate_id not in cards:
                write(f"(skipping {candidate_id}: no longer in the catalog)")
                position += 1
                continue
            if seed_id != shown_seed:
                write("")
                write(f"=== Seed {seed_numbers[seed_id]}/{len(seeds)} ===")
                for line in _describe(_seed_card(seeds_by_id[seed_id], cards), SEED_TERMS):
                    write(line)
                shown_seed = seed_id
            write("")
            write(f"[{n_pending - len(written)} left]")
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
                if written:
                    undo()
                else:
                    write("Nothing to undo in this session.")
            else:
                break
    except KeyboardInterrupt:
        write("")
    write(f"{len(written)} graded this session; {n_pending - len(written)} left in the pool.")
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
    try:
        load_judgments(folder / "judgments.jsonl")
    except ValueError as error:
        raise SystemExit(f"Fix this line before grading: {error}") from error
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

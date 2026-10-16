"""Build the TF-IDF recommender model file from the catalog (Phase 4,
Milestone 2).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md

Run with: uv run python -m crate_backend.scripts.build_tfidf_model
          [--alpha 0.6] [--no-bigrams] [--no-reception] [--no-personnel]
          [--max-features N] [--out PATH]
      or: uv run --group phrases python -m crate_backend.scripts.build_tfidf_model
          --sound-phrases [--alpha 0.6] [--no-reception] [--out PATH]

Reads every album's genre/tag votes and stored Wikipedia text, fits the
model and writes one joblib file (default: settings.tfidf_model_path). With
--sound-phrases the text block is the sound phrases spaCy extracts from each
article's prose instead of every word, written to
settings.tfidf_phrases_model_path for approach "phrases" (design:
docs/superpowers/specs/2026-10-15-sound-phrases-design.md). The API loads a
file on its first request and keeps it until restart, so restart the backend
after rebuilding. Evaluation variants are separate files built with --out.
"""

import argparse
import asyncio
import statistics
import time
import uuid
from collections import Counter
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.musicbrainz.dump_reader import read_dump_metadata
from crate_backend.recommend.sound_phrases import SPACY_MODEL, extract_all, prose_only
from crate_backend.recommend.text_cleaning import clean_article, merge_term_votes
from crate_backend.recommend.tfidf import (
    DEFAULT_ALPHA,
    AlbumDoc,
    TfidfModel,
    build_model,
    save_model,
)

# The spec's fallback: past this in-memory size, rebuild with
# --max-features 100000 and record the change.
_LARGE_MODEL_BYTES = 500 * 1024 * 1024


async def load_album_docs(
    session: AsyncSession,
    *,
    drop_reception: bool = False,
    drop_personnel: bool = False,
    only: list[uuid.UUID] | None = None,
) -> list[AlbumDoc]:
    """One AlbumDoc per album, ordered by id so builds are reproducible.
    `only` restricts loading to those albums (for tests)."""

    def restrict(query, album_id_column):
        return query if only is None else query.where(album_id_column.in_(only))

    albums = (
        await session.execute(restrict(select(Album.id, Album.title), Album.id).order_by(Album.id))
    ).all()

    pairs: dict[uuid.UUID, list[tuple[str, int]]] = {}
    genre_votes = select(AlbumGenre.album_id, Genre.name, AlbumGenre.count).join(
        Genre, Genre.id == AlbumGenre.genre_id
    )
    tag_votes = select(AlbumTag.album_id, Tag.name, AlbumTag.count).join(
        Tag, Tag.id == AlbumTag.tag_id
    )
    for query, column in ((genre_votes, AlbumGenre.album_id), (tag_votes, AlbumTag.album_id)):
        for album_id, name, votes in await session.execute(restrict(query, column)):
            pairs.setdefault(album_id, []).append((name, votes))

    texts = dict(
        (
            await session.execute(
                restrict(
                    select(AlbumText.album_id, AlbumText.text).where(
                        AlbumText.source == WIKIPEDIA_SOURCE, AlbumText.text.is_not(None)
                    ),
                    AlbumText.album_id,
                )
            )
        ).all()
    )

    return [
        AlbumDoc(
            album_id=album_id,
            title=title,
            term_votes=merge_term_votes(pairs.get(album_id, [])),
            text=clean_article(
                texts[album_id], drop_reception=drop_reception, drop_personnel=drop_personnel
            )
            if album_id in texts
            else "",
        )
        for album_id, title in albums
    ]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the TF-IDF recommender model file.")
    parser.add_argument(
        "--alpha", type=float, default=DEFAULT_ALPHA, help="tag weight in the blend, 0–1"
    )
    parser.add_argument("--no-bigrams", action="store_true", help="single words only")
    parser.add_argument(
        "--no-reception", action="store_true", help="drop Reception sections from articles"
    )
    parser.add_argument(
        "--no-personnel", action="store_true", help="drop Personnel/Credits sections"
    )
    parser.add_argument("--max-features", type=int, default=None, help="cap the text vocabulary")
    parser.add_argument(
        "--sound-phrases",
        action="store_true",
        help="text block from spaCy-extracted sound phrases (approach 'phrases')",
    )
    parser.add_argument("--out", type=Path, default=None, help="model file to write")
    args = parser.parse_args(argv)
    if not 0 <= args.alpha <= 1:
        parser.error("--alpha must be between 0 and 1")
    if args.sound_phrases and (args.no_bigrams or args.max_features is not None):
        parser.error("--no-bigrams and --max-features apply to article text, not --sound-phrases")
    return args


def _catalog_source() -> str:
    archive = Path(get_settings().musicbrainz_dump_dir) / "release-group.tar.xz"
    if not archive.exists():
        return "MusicBrainz dump (unknown date)"
    return f"MusicBrainz dump {read_dump_metadata(archive).get('TIMESTAMP', '(unknown date)')}"


def _megabytes(n_bytes: int) -> str:
    return f"{n_bytes / 1024 / 1024:.0f} MB"


def extract_phrases(docs: list[AlbumDoc]) -> tuple[list[list[str]], dict[str, str]]:
    """Each album's sound phrases from its article prose, and the parser's
    versions for the model metadata. Only this code path imports spaCy."""
    try:
        import spacy
    except ImportError as error:
        raise SystemExit("sound phrases need spaCy. Run: uv sync --group phrases") from error
    nlp = spacy.load(SPACY_MODEL)
    known_terms = frozenset(term for doc in docs for term in doc.term_votes)
    phrases = extract_all((prose_only(doc.text) for doc in docs), nlp, known_terms)
    metadata = {
        "spacy_version": str(spacy.__version__),
        "spacy_model": f"{nlp.meta['lang']}_{nlp.meta['name']}-{nlp.meta['version']}",
    }
    return phrases, metadata


async def build(args: argparse.Namespace) -> None:
    settings = get_settings()
    default_out = (
        settings.tfidf_phrases_model_path if args.sound_phrases else settings.tfidf_model_path
    )
    out = args.out or Path(default_out)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    phrases, phrase_metadata = extract_phrases(docs) if args.sound_phrases else (None, {})
    parsed = time.perf_counter()
    model = build_model(
        docs,
        alpha=args.alpha,
        ngram_range=(1, 1) if args.no_bigrams else (1, 2),
        max_features=args.max_features,
        phrases=phrases,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
            **phrase_metadata,
        },
    )
    fitted = time.perf_counter()
    save_model(model, out)
    saved = time.perf_counter()

    matrix_bytes = sum(
        m.data.nbytes + m.indices.nbytes + m.indptr.nbytes
        for m in (model.tag_matrix, model.text_matrix)
    )
    n_albums, n_text = model.metadata["n_albums"], model.metadata["n_with_text"]
    label = "phrases" if phrases is not None else "text"
    print(
        f"Albums:          {n_albums:,} ({n_text:,} with {label}, {100 * n_text / n_albums:.0f}%)"
    )
    print(f"Tag terms:       {len(model.tag_terms):,}")
    if phrases is not None:
        _print_phrase_summary(phrases, model)
    else:
        print(f"Text terms:      {len(model.text_terms):,}")
    print(f"Nonzeros:        {model.tag_matrix.nnz:,} tag, {model.text_matrix.nnz:,} {label}")
    print(f"Matrices:        {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, parse {parsed - loaded:.1f}s, "
        f"fit {fitted - parsed:.1f}s, save {saved - fitted:.1f}s"
    )
    print(f"Model version:   {model.metadata['model_version']}")
    if matrix_bytes > _LARGE_MODEL_BYTES and args.max_features is None and phrases is None:
        print("Model exceeds 500 MB: rebuild with --max-features 100000 and record the change.")


def _print_phrase_summary(phrases: list[list[str]], model: TfidfModel) -> None:
    """What the extraction found, so a build can be sanity-checked without
    opening the file."""
    per_album = [len(p) for p in phrases if p]
    median = statistics.median(per_album) if per_album else 0
    extracted = len({phrase for album in phrases for phrase in album})
    print(f"Phrases:         {extracted:,} distinct extracted, {len(model.text_terms):,} kept")
    print(f"Per album:       median {median:g} (albums with any phrase)")
    albums_per_term = Counter(
        dict(zip(model.text_terms, (model.text_matrix > 0).sum(axis=0).A1, strict=True))
    )
    print(
        "Most common:     "
        + "; ".join(f"{term} ({n})" for term, n in albums_per_term.most_common(25))
    )


def main() -> None:
    asyncio.run(build(parse_args()))


if __name__ == "__main__":
    main()

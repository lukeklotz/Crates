"""Build the TF-IDF recommender model file from the catalog (Phase 4,
Milestone 2).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md

Run with: uv run python -m crate_backend.scripts.build_tfidf_model
          [--alpha 0.6] [--no-bigrams] [--no-reception] [--no-personnel]
          [--max-features N] [--out PATH]

Reads every album's genre/tag votes and stored Wikipedia text, fits the
model and writes one joblib file (default: settings.tfidf_model_path). The
API loads that file on its first tfidf request and keeps it until restart,
so restart the backend after rebuilding. Evaluation variants are separate
files built with --out.
"""

import argparse
import asyncio
import time
import uuid
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.musicbrainz.dump_reader import read_dump_metadata
from crate_backend.recommend.text_cleaning import clean_article, merge_term_votes
from crate_backend.recommend.tfidf import DEFAULT_ALPHA, AlbumDoc, build_model, save_model

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
    parser.add_argument("--out", type=Path, default=None, help="model file to write")
    args = parser.parse_args(argv)
    if not 0 <= args.alpha <= 1:
        parser.error("--alpha must be between 0 and 1")
    return args


def _catalog_source() -> str:
    archive = Path(get_settings().musicbrainz_dump_dir) / "release-group.tar.xz"
    if not archive.exists():
        return "MusicBrainz dump (unknown date)"
    return f"MusicBrainz dump {read_dump_metadata(archive).get('TIMESTAMP', '(unknown date)')}"


def _megabytes(n_bytes: int) -> str:
    return f"{n_bytes / 1024 / 1024:.0f} MB"


async def build(args: argparse.Namespace) -> None:
    out = args.out or Path(get_settings().tfidf_model_path)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    model = build_model(
        docs,
        alpha=args.alpha,
        ngram_range=(1, 1) if args.no_bigrams else (1, 2),
        max_features=args.max_features,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
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
    print(f"Albums:          {n_albums:,} ({n_text:,} with text, {100 * n_text / n_albums:.0f}%)")
    print(f"Tag terms:       {len(model.tag_terms):,}")
    print(f"Text terms:      {len(model.text_terms):,}")
    print(f"Nonzeros:        {model.tag_matrix.nnz:,} tag, {model.text_matrix.nnz:,} text")
    print(f"Matrices:        {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, fit {fitted - loaded:.1f}s, "
        f"save {saved - fitted:.1f}s"
    )
    print(f"Model version:   {model.metadata['model_version']}")
    if matrix_bytes > _LARGE_MODEL_BYTES and args.max_features is None:
        print("Model exceeds 500 MB: rebuild with --max-features 100000 and record the change.")


def main() -> None:
    asyncio.run(build(parse_args()))


if __name__ == "__main__":
    main()

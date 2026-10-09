"""Build the sentence-embedding recommender model file (Phase 5a).

Design: docs/superpowers/specs/2026-10-08-embedding-recommender-design.md

Run with: uv run --group embeddings python -m crate_backend.scripts.build_embedding_model
          [--alpha 0.6] [--no-reception] [--no-personnel] [--device cpu|mps]
          [--batch-size 64] [--out PATH]

Reads the same album documents as the TF-IDF build (genre/tag votes and the
cleaned Wikipedia text), embeds them with bge-small-en-v1.5 and writes one
joblib file (default: settings.embeddings_model_path). The API loads that
file on its first embeddings request and keeps it until restart, so restart
the backend after rebuilding. The first run downloads the encoder (~130 MB).
"""

import argparse
import asyncio
import time
from pathlib import Path

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.recommend.embeddings import (
    Encoder,
    build_model,
    save_model,
)
from crate_backend.recommend.sentence_encoder import EncoderUnavailable, SentenceTransformerEncoder
from crate_backend.recommend.tfidf import DEFAULT_ALPHA
from crate_backend.scripts.build_tfidf_model import _catalog_source, _megabytes, load_album_docs


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the sentence-embedding model file.")
    parser.add_argument(
        "--alpha", type=float, default=DEFAULT_ALPHA, help="tag weight in the blend, 0–1"
    )
    parser.add_argument(
        "--no-reception", action="store_true", help="drop Reception sections from articles"
    )
    parser.add_argument(
        "--no-personnel", action="store_true", help="drop Personnel/Credits sections"
    )
    parser.add_argument("--device", default="cpu", help="cpu or mps (Apple GPU)")
    parser.add_argument("--batch-size", type=int, default=64, help="texts per encoder batch")
    parser.add_argument("--out", type=Path, default=None, help="model file to write")
    args = parser.parse_args(argv)
    if not 0 <= args.alpha <= 1:
        parser.error("--alpha must be between 0 and 1")
    return args


async def build(args: argparse.Namespace, encoder: Encoder | None = None) -> None:
    out = args.out or Path(get_settings().embeddings_model_path)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    # Created before the encode timer starts: the first run downloads the
    # weights, which would otherwise count as encoding time.
    if encoder is None:
        encoder = SentenceTransformerEncoder(device=args.device, batch_size=args.batch_size)
    ready = time.perf_counter()
    model = build_model(
        docs,
        encoder,
        alpha=args.alpha,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
        },
    )
    encoded = time.perf_counter()
    save_model(model, out)
    saved = time.perf_counter()

    meta = model.metadata
    n_albums, n_text = meta["n_albums"], meta["n_with_text"]
    # Tag strings are encoded too, so the rate is over every encoded text.
    n_texts = n_albums + meta["n_chunks"]
    matrix_bytes = model.tag_vectors.nbytes + model.text_vectors.nbytes
    print(f"Albums:          {n_albums:,} ({n_text:,} with text, {100 * n_text / n_albums:.0f}%)")
    print(f"Chunks embedded: {meta['n_chunks']:,}")
    print(f"Encode rate:     {n_texts / (encoded - ready):.0f} texts/s (tag lines + chunks)")
    print(f"Encoder:         {meta['encoder_name']} @ {meta['encoder_revision']}")
    print(f"Vectors:         {meta['embedding_dim']} dims, {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, encoder setup {ready - loaded:.1f}s, "
        f"encode {encoded - ready:.1f}s, save {saved - encoded:.1f}s"
    )
    print(f"Model version:   {meta['model_version']}")
    if meta.get("n_truncated_inputs"):
        print(
            f"Warning: {meta['n_truncated_inputs']} inputs were longer than the encoder's "
            f"{meta['max_seq_length']}-token window and were cut off. Lower CHUNK_WORDS."
        )


def main() -> None:
    try:
        asyncio.run(build(parse_args()))
    except EncoderUnavailable as error:
        raise SystemExit(str(error)) from error


if __name__ == "__main__":
    main()

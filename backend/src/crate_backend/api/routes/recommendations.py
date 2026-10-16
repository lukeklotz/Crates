import uuid
from typing import Literal, NamedTuple

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.concurrency import run_in_threadpool

from crate_backend.db.session import get_session
from crate_backend.models.catalog import Album
from crate_backend.recommend.embeddings import recommend as recommend_by_embeddings
from crate_backend.recommend.model_store import (
    get_embedding_model,
    get_tfidf_model,
    get_tfidf_phrases_model,
)
from crate_backend.recommend.overlap import recommend_by_overlap, seeds_have_terms
from crate_backend.recommend.tfidf import recommend as recommend_by_tfidf

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

# Names in the 503 detail when an approach's model file isn't built.
_MODEL_NAMES = {"tfidf": "TF-IDF", "phrases": "Sound-phrase", "embeddings": "Embedding"}


class RecommendationRequest(BaseModel):
    album_ids: list[uuid.UUID] = Field(min_length=1, max_length=50)
    limit: int = Field(default=20, ge=1, le=50)
    # "overlap" (Jaccard, Phase 3), "tfidf" (Phase 4), "phrases" (TF-IDF
    # over sound phrases) or "embeddings" (Phase 5a). The default changes
    # only once the evaluation answer key picks a winner.
    approach: Literal["overlap", "tfidf", "phrases", "embeddings"] = "overlap"


class RecommendedAlbum(BaseModel):
    id: str
    title: str
    artist_name: str | None
    release_year: int | None
    cover_art_url: str | None
    score: float
    shared_terms: list[str]
    # Article words/phrases behind the match; always empty for overlap.
    shared_text_terms: list[str]


class RecommendationResponse(BaseModel):
    approach: str
    # Build time of the model file that answered; null for overlap.
    model_version: str | None
    results: list[RecommendedAlbum]
    reason: str | None


class _Ranked(NamedTuple):
    album_id: uuid.UUID
    score: float
    shared_terms: list[str]
    shared_text_terms: list[str]


@router.post("", response_model=RecommendationResponse)
async def recommend(
    request: RecommendationRequest, session: AsyncSession = Depends(get_session)
) -> RecommendationResponse:
    """Albums related to a group's seed albums."""
    seed_ids = list(dict.fromkeys(request.album_ids))
    found = set(await session.scalars(select(Album.id).where(Album.id.in_(seed_ids))))
    missing = [str(album_id) for album_id in seed_ids if album_id not in found]
    if missing:
        raise HTTPException(
            status_code=404, detail={"message": "Unknown album ids", "missing": missing}
        )

    model = None
    if request.approach != "overlap":
        # The first call reads the model file; keep that off the event loop.
        # Build the map here, not at import time, so tests can swap loaders.
        loader = {
            "tfidf": get_tfidf_model,
            "phrases": get_tfidf_phrases_model,
            "embeddings": get_embedding_model,
        }[request.approach]
        model = await run_in_threadpool(loader)
        if model is None:
            raise HTTPException(
                status_code=503, detail=f"{_MODEL_NAMES[request.approach]} model not built"
            )
    model_version = model.metadata["model_version"] if model else None

    def respond(results: list[RecommendedAlbum], reason: str | None) -> RecommendationResponse:
        return RecommendationResponse(
            approach=request.approach, model_version=model_version, results=results, reason=reason
        )

    if not await seeds_have_terms(session, seed_ids):
        return respond([], "seeds_have_no_terms")

    if model is None:
        ranked = [
            _Ranked(r.album_id, r.score, r.shared_terms, [])
            for r in await recommend_by_overlap(session, seed_ids, request.limit)
        ]
    else:
        if not any(seed_id in model.row_of for seed_id in seed_ids):
            return respond([], "seeds_not_in_model")
        if request.approach in ("tfidf", "phrases"):
            ranked = [
                _Ranked(r.album_id, r.score, r.shared_terms, r.shared_text_terms)
                for r in recommend_by_tfidf(model, seed_ids, request.limit)
            ]
        else:
            ranked = [
                _Ranked(r.album_id, r.score, r.shared_terms, [])
                for r in recommend_by_embeddings(model, seed_ids, request.limit)
            ]

    albums = {
        album.id: album
        for album in await session.scalars(
            select(Album).where(Album.id.in_([r.album_id for r in ranked]))
        )
    }
    return respond(
        [
            RecommendedAlbum(
                id=str(r.album_id),
                title=albums[r.album_id].title,
                artist_name=albums[r.album_id].artist_name,
                release_year=albums[r.album_id].release_year,
                cover_art_url=albums[r.album_id].cover_art_url,
                score=r.score,
                shared_terms=r.shared_terms,
                shared_text_terms=r.shared_text_terms,
            )
            for r in ranked
            # A model built before an album left the catalog can still rank it.
            if r.album_id in albums
        ],
        None,
    )

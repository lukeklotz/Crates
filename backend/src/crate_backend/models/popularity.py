import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Album


class PopularitySignal(UUIDPkMixin, TimestampMixin, Base):
    """Raw popularity signals for one album, kept separate by source and
    never blended. Album.popularity is derived from lastfm_listeners only
    (crate_backend.lastfm.scoring); sandbox_add_count is tracked but not
    yet used in ranking."""

    __tablename__ = "popularity_signals"

    album_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("albums.id"), unique=True, index=True
    )

    # Null means no verified match (or no completed attempt), never zero.
    lastfm_listeners: Mapped[int | None] = mapped_column(nullable=True)
    lastfm_matched_artist: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lastfm_matched_title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    # Set on any definitive answer (match, no match, mismatch); left null when
    # retries are exhausted so the next backfill run retries the album.
    lastfm_fetched_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    sandbox_add_count: Mapped[int] = mapped_column(default=0)

    album: Mapped["Album"] = relationship()

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Album

WIKIPEDIA_SOURCE = "wikipedia"


class AlbumText(UUIDPkMixin, TimestampMixin, Base):
    """Descriptive text about one album from one outside source. Stored in
    full so model builds can choose which sections to use without
    re-fetching. Wikipedia text is CC BY-SA: used as model features only,
    never displayed without attribution."""

    __tablename__ = "album_texts"

    album_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("albums.id"), index=True)
    source: Mapped[str] = mapped_column(String(20))

    article_title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    # The revision fetched, so a model build can be reproduced.
    revision_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    # Plain text with "== Section ==" headings; null means no usable article.
    text: Mapped[str | None] = mapped_column(Text, nullable=True)
    # Set on any definitive answer (article, or no article); left null when
    # retries are exhausted so the next backfill run retries the album.
    fetched_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    album: Mapped["Album"] = relationship()

    __table_args__ = (UniqueConstraint("album_id", "source"),)

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Album
    from crate_backend.models.user import User


class Rating(UUIDPkMixin, TimestampMixin, Base):
    """A 0-5 star rating. Optional; never required to use the sandbox."""

    __tablename__ = "ratings"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)
    album_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("albums.id"), index=True)
    stars: Mapped[int] = mapped_column(Integer)

    user: Mapped["User"] = relationship(back_populates="ratings")
    album: Mapped["Album"] = relationship()

    __table_args__ = (
        UniqueConstraint("user_id", "album_id"),
        CheckConstraint("stars >= 0 AND stars <= 5", name="stars_range"),
    )


class Descriptor(UUIDPkMixin, TimestampMixin, Base):
    """A user's own words for what an album feels like."""

    __tablename__ = "descriptors"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)
    album_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("albums.id"), index=True)
    body: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="descriptors")
    album: Mapped["Album"] = relationship()

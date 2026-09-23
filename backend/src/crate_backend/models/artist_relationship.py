import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Artist


class ArtistRelationship(UUIDPkMixin, TimestampMixin, Base):
    """Directed artist-to-artist edge (member of band, collaboration).

    Always stored in MusicBrainz's forward orientation — artist_id is the
    relationship's subject (the member), related_artist_id its object (the
    band) — so the same edge seen from both artists' records is one row.
    """

    __tablename__ = "artist_relationships"

    artist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("artists.id"), index=True)
    related_artist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("artists.id"), index=True)
    relationship_type: Mapped[str] = mapped_column(String(50))

    artist: Mapped["Artist"] = relationship(foreign_keys=[artist_id])
    related_artist: Mapped["Artist"] = relationship(foreign_keys=[related_artist_id])

    __table_args__ = (UniqueConstraint("artist_id", "related_artist_id", "relationship_type"),)

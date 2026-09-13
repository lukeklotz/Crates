import uuid

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin


class Artist(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "artists"

    name: Mapped[str] = mapped_column(String(255), index=True)
    # Populated once the MusicBrainz pipeline (Phase 2) backfills the catalog.
    musicbrainz_id: Mapped[str | None] = mapped_column(String(36), unique=True, nullable=True)

    albums: Mapped[list["Album"]] = relationship(back_populates="primary_artist")


class Album(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "albums"

    title: Mapped[str] = mapped_column(String(500), index=True)
    primary_artist_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("artists.id"), nullable=True
    )
    # Denormalized display name, used until a release is linked to a proper Artist row.
    artist_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    release_year: Mapped[int | None] = mapped_column(nullable=True)
    cover_art_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    # Canonical identity once imported from MusicBrainz (Phase 2); an album
    # primarily corresponds to a MusicBrainz release group.
    musicbrainz_release_group_id: Mapped[str | None] = mapped_column(
        String(36), unique=True, nullable=True
    )
    # Provenance for rows sourced from a stand-in catalog (e.g. the iTunes
    # Search API used by the Phase 1 prototype) before MusicBrainz import.
    external_source: Mapped[str | None] = mapped_column(String(50), nullable=True)
    external_id: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Validated popularity signal is selected in Phase 3; null means unknown,
    # not obscure.
    popularity: Mapped[float | None] = mapped_column(nullable=True)

    primary_artist: Mapped["Artist | None"] = relationship(back_populates="albums")

    __table_args__ = (UniqueConstraint("external_source", "external_id"),)

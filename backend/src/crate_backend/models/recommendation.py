import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crate_backend.db.base import Base
from crate_backend.models.mixins import TimestampMixin, UUIDPkMixin

if TYPE_CHECKING:
    from crate_backend.models.catalog import Album
    from crate_backend.models.group import AlbumGroup


class ModelVersion(UUIDPkMixin, TimestampMixin, Base):
    """An identifiable, immutable version of a recommendation model or
    heuristic (e.g. "popularity_baseline" v1), so every run can be traced
    back to what produced it."""

    __tablename__ = "model_versions"

    name: Mapped[str] = mapped_column(String(100))
    version_tag: Mapped[str] = mapped_column(String(50))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    extra: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    __table_args__ = (UniqueConstraint("name", "version_tag"),)


class RecommendationRun(UUIDPkMixin, TimestampMixin, Base):
    """One request for a group's recommendations, with enough state
    snapshotted to reproduce its results."""

    __tablename__ = "recommendation_runs"

    group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("album_groups.id"), index=True)
    model_version_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("model_versions.id"), nullable=True
    )
    group_revision: Mapped[int] = mapped_column(Integer)
    settings_snapshot: Mapped[dict] = mapped_column(JSONB)
    status: Mapped[str] = mapped_column(String(20), default="pending")

    group: Mapped["AlbumGroup"] = relationship(back_populates="recommendation_runs")
    model_version: Mapped["ModelVersion | None"] = relationship()
    recommendations: Mapped[list["Recommendation"]] = relationship(
        back_populates="run", cascade="all, delete-orphan"
    )


class Recommendation(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "recommendations"

    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("recommendation_runs.id"), index=True)
    album_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("albums.id"), index=True)
    rank: Mapped[int] = mapped_column(Integer)
    score: Mapped[float] = mapped_column()
    explanation: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    run: Mapped["RecommendationRun"] = relationship(back_populates="recommendations")
    album: Mapped["Album"] = relationship()

    __table_args__ = (UniqueConstraint("run_id", "album_id"),)

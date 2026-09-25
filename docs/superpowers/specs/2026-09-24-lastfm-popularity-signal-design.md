# Last.fm popularity signal — design

**Status:** Design complete, pending user review.

## Purpose

Phase 3 of the Crate project plan (`docs/crate-ml-engineering-project-plan.md`) requires a validated album-level popularity signal before the popularity baseline and the lesser-known/moderate/widely-popular controls can be implemented. `Album.popularity` exists as a column but has never been populated — no source has been selected. This spec picks Last.fm as that source, matched against MusicBrainz-identified albums by artist name + album title (Last.fm's own MBID tagging is too sparse to use as the primary lookup key), and adds a second, independent internal signal — an in-app "added to sandbox" counter — that is tracked from now on but not yet used in ranking.

## Decisions made

### Storage shape
A dedicated `PopularitySignal` table, one row per album, rather than extending `Album` with more columns directly. This keeps each raw signal's provenance (source, matched identity, fetch time) separate from `Album.popularity`, which becomes a **derived** value computed from those signals — not a value written to directly by ingestion code. A dedicated table also means adding a future third source (or a second external source) doesn't require another schema migration on `Album` itself.

### The two signals stay separate; only one currently feeds ranking
Two independent, always-present-in-schema signals:
- **`lastfm_listeners`** — Last.fm's unique-listener count for the album, verified by exact match. Nullable: null means "no verified match found," not "zero listeners," consistent with the plan's null-means-unknown convention for popularity.
- **`sandbox_add_count`** — a count of how many times any user has added this album to their sandbox in Crate. Never null; starts at 0 and increments from the moment an album exists in the catalog.

These are **not blended into a single score**. `Album.popularity` is derived from `lastfm_listeners` only (see "Score computation" below). `sandbox_add_count` is collected starting now so it exists as a track record and is available for later use (e.g. ML training features, or a future revisit of the popularity score), but it does not influence popularity/ranking in this phase. This was a deliberate reversal during design: blending was considered (weighted average of normalized signals) and rejected — Last.fm's absolute scale (thousands to millions of listeners) will dwarf Crate's own early usage numbers for the foreseeable future, so blending them either makes the internal signal practically inert (unweighted sum) or requires an arbitrary weighting choice to make it matter (weighted sum). Keeping them separate avoids manufacturing a combined number that doesn't yet mean anything, while still capturing the raw data as it accumulates.

### Popularity metric: listeners, not playcount
Last.fm's `album.getInfo` returns both `listeners` (unique users who've played it) and `playcount` (total plays). Listeners was chosen because it's less skewed by a small number of people looping an album obsessively, and maps more directly onto "how many people know this album" — the framing the plan's lesser-known/moderate/widely-popular control uses. `playcount` is not stored in v1; it can be added to `PopularitySignal` later without disrupting this design if a future evaluation shows it's a better signal.

### Match verification: exact normalized match only
Last.fm is queried by artist name + album title (not MBID). The response is accepted only if the normalized artist name and normalized album title both equal what was sent — normalization means lowercasing, stripping punctuation/diacritics, and collapsing whitespace. No fuzzy/similarity-threshold matching. This trades recall (albums with alternate titles, e.g. "&" vs "and", deluxe-edition suffixes, won't match) for a low false-positive rate — a wrong match would silently corrupt a popularity signal that later feeds a public-facing control and a training feature, which is a worse failure mode than a missing signal (already handled everywhere as "unknown, not obscure").

An album with no `artist_name` (the denormalized field on `Album` can be null per `catalog.py`) is skipped without calling Last.fm at all — there's nothing to match against.

### Score computation: percentile rank, Last.fm only
`Album.popularity` = this album's percentile rank (0.0-1.0) of `lastfm_listeners` among all albums in the catalog that have a verified Last.fm match. Raw listener counts are extremely right-skewed (a handful of albums with millions of listeners, most with a few thousand), so raw counts or a fixed log transform would push almost everything into "lesser-known" under any reasonable bucket cutoffs. Percentile rank keeps the three-way (or later, continuous) popularity control evenly distributed relative to Crate's actual catalog, regardless of Last.fm's absolute skew.

This is **not** computed per-request. It's recomputed as a batch step after a backfill run (or any run that changes `lastfm_listeners` values), since percentile rank is only meaningful relative to the full current distribution. Albums with no verified match keep `Album.popularity = null`.

### Retry/resume behavior
`lastfm_fetched_at` is set whenever a lookup is attempted, **including when it results in no verified match** — not only on success. This means a no-match result is recorded, not indistinguishable from "never tried." Re-running the backfill script by default skips albums that already have a `lastfm_fetched_at`, mirroring the Cover Art Archive script's "only check albums that still have no url" resume behavior. A future flag to force re-checking previously-failed matches (e.g. if matching logic improves) is not built in v1 but the schema doesn't block adding one.

### Internal endpoint for the sandbox counter
The canvas/sandbox is currently frontend-only local state (`frontend/app/page.tsx`) — there is no backend endpoint for any sandbox action yet. Rather than deferring `sandbox_add_count` until full workspace/canvas persistence exists (separate, larger future work), this spec adds one minimal endpoint: `POST /albums/{album_id}/add-to-sandbox`, authenticated via the existing `current_active_user` dependency (`auth/backend.py`). It does not implement sandbox/workspace persistence — it only records that the action happened.

## Data model

```python
class PopularitySignal(UUIDPkMixin, TimestampMixin, Base):
    __tablename__ = "popularity_signals"

    album_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("albums.id"), unique=True, index=True
    )

    # Last.fm listener-count signal. Null means "no verified match found or
    # not yet attempted," never "zero listeners."
    lastfm_listeners: Mapped[int | None] = mapped_column(nullable=True)
    lastfm_matched_artist: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lastfm_matched_title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    # Set on every lookup attempt, including a no-match result, so resumed
    # backfill runs can skip albums already tried.
    lastfm_fetched_at: Mapped[datetime | None] = mapped_column(nullable=True)

    # Internal usage signal. Always present, never null; not currently used
    # in Album.popularity.
    sandbox_add_count: Mapped[int] = mapped_column(default=0)

    album: Mapped["Album"] = relationship()
```

`Album.popularity` (existing column) is written only by the percentile-rank recomputation step, never directly by the Last.fm client or the sandbox-add endpoint.

## Pipeline architecture

1. **Last.fm client** (`backend/src/crate_backend/lastfm/client.py`): `httpx.AsyncClient`-based, following `musicbrainz/cover_art.py`'s shape — a module-level `_sleep` (patchable in tests), the same retry/backoff constants (5 retries, 1s initial backoff doubling to a 60s cap) on 429/5xx, never raises. Paced at 1 request/second — matching the existing Cover Art Archive pacing and comfortably under Last.fm's documented ~5 req/sec limit. A full backfill over ~25,000 albums takes roughly 7 hours; this is a one-off/occasional batch job, not a live-path call.
2. **Matching** (`backend/src/crate_backend/lastfm/match.py`): normalizes artist/title strings (lowercase, strip diacritics/punctuation, collapse whitespace) and compares Last.fm's response against what was sent. Returns the verified `(listeners, matched_artist, matched_title)` or `None`.
3. **Ingest / upsert** (`backend/src/crate_backend/lastfm/ingest.py`): idempotent, keyed by `album_id` — matches the existing MusicBrainz ingest pattern of get-or-create-then-update. Sets `lastfm_fetched_at` on every attempt.
4. **Score recomputation** (`backend/src/crate_backend/lastfm/scoring.py`): a function that reads all `PopularitySignal.lastfm_listeners` values, computes percentile rank, and writes `Album.popularity` for matched albums. Called at the end of the backfill script.
5. **Script** (`backend/src/crate_backend/scripts/backfill_lastfm_popularity.py`): analogous to `scripts/ingest_musicbrainz.py` — iterates albums missing a `lastfm_fetched_at` (unless a `--recheck` style flag is added later), calls the client + matcher + ingest per album, then runs score recomputation once at the end.
6. **Endpoint** (`backend/src/crate_backend/api/routes/albums.py`): `POST /albums/{album_id}/add-to-sandbox`, authenticated. In one transaction: get-or-create the album's `PopularitySignal` row and increment `sandbox_add_count`; insert an `Event(event_type="album_added_to_sandbox", user_id=current_user.id, payload={"album_id": str(album_id)})`. Returns 204.

## Configuration

`core/config.py` gains `lastfm_api_key: str` under the existing `CRATE_` env prefix (`CRATE_LASTFM_API_KEY`), following the same pattern as `database_url`/`auth_secret`. The user will register a free key at last.fm/api/account/create and set it locally; no key is provisioned as part of this spec.

## Error handling & edge cases

- No `artist_name` on the album → skip Last.fm entirely, no request made, no `PopularitySignal` row created for this reason alone.
- Last.fm returns 404 / album not found → treated as no match; `lastfm_fetched_at` set, `lastfm_listeners` stays null.
- Last.fm returns a result but normalized artist or title doesn't match → discarded as a mismatch; same as no-match handling.
- Transport errors / 429 / 5xx → retried per the existing backoff policy; if retries are exhausted, treated as "not yet attempted" (do **not** set `lastfm_fetched_at`), so the next backfill run retries it rather than silently treating a transient failure as a permanent no-match.
- Re-running the backfill script is always safe: already-attempted albums (successful or verified-no-match) are skipped by default; upserts are idempotent by `album_id`.
- `POST /albums/{album_id}/add-to-sandbox` on an unknown `album_id` → 404. Without authentication → 401 (existing `current_active_user` dependency behavior).

## Testing

- `test_lastfm_client.py` — retry/backoff behavior, reusing the patched-`_sleep` approach from `test_cover_art.py`.
- `test_lastfm_match.py` — normalization and exact-match verification: case differences, punctuation, diacritics, artist mismatch, title mismatch, both matching.
- `test_lastfm_ingest.py` — idempotent upsert, `lastfm_fetched_at` set on both match and no-match, resume-skips-already-attempted behavior.
- `test_lastfm_scoring.py` — percentile-rank computation over a known set of listener counts, including the all-null (no matches yet) case.
- `test_albums.py` (extended) — `POST /albums/{album_id}/add-to-sandbox` increments the counter, creates an `Event` row, 401 unauthenticated, 404 unknown album.

## Related files

- `docs/crate-ml-engineering-project-plan.md` — Phase 3, steps 1 and 10, which this spec implements the popularity-signal prerequisite for.
- `docs/superpowers/specs/2026-09-20-musicbrainz-ingestion-design.md` — the ingestion pipeline this design's client/matching/ingest split follows the shape of.
- `backend/src/crate_backend/musicbrainz/cover_art.py` — rate-limited client pattern reused for the Last.fm client.
- `backend/src/crate_backend/musicbrainz/ingest.py` — idempotent upsert pattern reused for `PopularitySignal`.
- `backend/src/crate_backend/models/catalog.py` — `Album.popularity`, the derived field this design populates.
- `backend/src/crate_backend/models/event.py` — `Event`, used for the `album_added_to_sandbox` audit trail.
- `backend/src/crate_backend/core/config.py` — gains `lastfm_api_key`.

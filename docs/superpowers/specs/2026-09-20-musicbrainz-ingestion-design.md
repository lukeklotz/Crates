# MusicBrainz ingestion pipeline — design (in progress)

**Status:** Brainstorming in progress. Architecture and data-acquisition mechanism are settled; schema, relationship-type allowlist, genre/tag thresholds, testing, and provenance recording are still open. Resume from "Open items for next session" below.

## Purpose

Phase 2 of the Crate project plan (`docs/crate-ml-engineering-project-plan.md`) needs a reproducible pipeline that turns MusicBrainz data into Crate's normalized album catalog. This replaces the small hand-written seed catalog (141 albums, `backend/src/crate_backend/scripts/seed_catalog.py`) built during Phase 1, which only has title/artist/year and no genre/tag/credit data. Phase 3 (non-ML baselines: genre-overlap, tag-overlap, graph features from shared musicians/producers/labels/instruments/artist relationships) and Phase 4 (TF-IDF text documents from genres/tags/credits/instruments/labels/text) both depend on this richer metadata existing.

## Decisions made

### Catalog scope
- **All genres**, not restricted to any single genre (an earlier jazz-only scoping was superseded once the goal was clarified as "search/recommend all types of music").
- **Release types:** primary type = Album; secondary type = none (studio) or Live. Compilations, Soundtracks, Remixes, and other secondary types are excluded (pre-LP-era compilation handling and other edge cases are deferred).
- **Target size:** bounded at roughly **10,000–25,000 albums**, matching the original Phase 2 plan and its stated philosophy ("begin with a modest catalog and single-machine processing, then expand... only when those additions solve a demonstrated problem"). A full-database import (well over a million release-groups) was explicitly rejected for now — it would pull Phase 8's scaling work forward without a demonstrated need.
- **Ranking/cap heuristic** (for when the genre+type filter yields more than the target count, which it will): require a minimum bar — at least one genre/tag, at least one release, at least one parsed relationship — to exclude near-empty stub entries, then rank the remainder by a composite of tag-vote count + number of distinct releases (a notability proxy, since well-known albums get reissued/repressed more), and cap at the target. Known bias to carry forward honestly: this still skews toward genres/regions where MusicBrainz's volunteer tagging community is most active (Western rock/pop/electronic).
- **Existing seed data:** the 141-album generic seed catalog gets replaced once the MusicBrainz-derived catalog is ingested (not kept side by side — recommendation signal quality would be too uneven between hand-seeded rows with no metadata and fully-ingested rows).

### Acquisition mechanism
- **MusicBrainz JSON Data Dumps**, not the live rate-limited (1 req/sec) JSON API, and not a full local MusicBrainz Postgres mirror (`musicbrainz-docker`).
  - Rejected the live API for bulk loading: at full multi-genre scale (potentially hundreds of thousands of candidate release-groups before capping), sequential 1 req/sec calls would take weeks to months. The live API remains a good fit later for *incremental*, on-demand lookups (e.g. a user searches for an album not yet in the catalog).
  - Rejected a full Postgres mirror: heavier than needed (their full production schema, Docker Compose replication setup) when the JSON dumps already contain everything we need in the same shape as the live API's JSON responses.
- **Source:** `https://data.metabrainz.org/pub/musicbrainz/data/json-dumps` (mirrored at `ftp.musicbrainz.org`). One `.tar.xz` per entity type, containing an `mbdump/<entity>` file with one JSON object per line, in the same field shape the live web service returns. Data is CC0-licensed (public domain) per MusicBrainz's own dump documentation.
- **Dump files needed:** `release-group`, `release`, `artist`, `label`.
  - **Skip** `recording` — it only contains *standalone* recordings; normal album tracks are embedded inside their parent `release` entry already (medium → track → recording).
  - **Skip** `work`, `event`, `series`, `url` — not needed for the relationship allowlist we're targeting.
- **Verified structural facts** (from MusicBrainz's own JSON Data Dumps documentation):
  - Dumped records already embed genres, tags, aliases, annotations, ratings, and *most* relationships — equivalent to a maximal `inc=` live lookup. No follow-up API calls needed for the bulk build.
  - Two relationship exclusions to be aware of: (1) work-linked relationships live only in the `work` dump (irrelevant, we're not using Work-level data for v1); (2) a release with more than 500 recordings has its recording-linked relationships excluded from the dump (rare box-set edge case — plan to log and skip rather than special-case with a live fallback lookup).
  - Monthly **sample dumps** exist (same paths, `sample` instead of `fullexport`) — useful for developing/testing the parsing pipeline before running it against the full multi-GB dumps.

### Pipeline architecture

Four stages, run as a script analogous to the existing seed script (`uv run python -m crate_backend.scripts.ingest_musicbrainz`), idempotent so re-runs are safe:

1. **Filter pass** over the `release-group` dump (streamed line by line): keep entries matching the genre+type criteria above, holding just their MBIDs + core metadata (title, first-release-date, artist-credit, genres, tags) in memory as the candidate set.
2. **Extract pass** over the `release` dump (streamed): for each release whose release-group is in the candidate set, if it's the best representative release for that group (earliest `status=Official`, falling back to earliest of any status), pull its full tracklist, embedded recording-level relationships (performer/instrument, production credits), and label/catalog-number.
3. **Artist pass** over the `artist` dump (streamed): resolve artist-to-artist relationships (member-of-band, collaborator) for every unique artist MBID encountered in step 2. Deduplicated by artist MBID so a heavily-featured artist (session musician, producer) is only resolved once regardless of how many albums they appear on.
4. **Cover art** (separate, live network calls — no bulk dump exists for this): `GET https://coverartarchive.org/release-group/{mbid}/front` per ingested album. A 404 means no art and is treated as `null`, not an error. Rate-limit politely; Cover Art Archive has no MusicBrainz-style documented hard limit, but ~10k-25k sequential calls still warrants basic pacing/backoff.

Each stage is a separate function; caching the filtered candidate set from stage 1 and the raw parsed data from stage 2 makes the pipeline resumable rather than needing a full restart if interrupted.

## Open items for next session

These still need concrete decisions before implementation can start:

1. **Relationship-type allowlist — exact MusicBrainz type names.** Agreed *categories* (performer+instrument, producer/engineer, artist-to-artist member-of-band/collaboration, release-label), but not yet the literal MusicBrainz relationship type strings to filter on (e.g. which of "instrument", "vocal", "producer", "engineer", "mix", "mastering", "member of band", "collaboration", etc. to keep vs. discard as noise).
2. **Genre vs. tag handling specifics.** MusicBrainz distinguishes curated `genre` (a controlled subset) from freeform folksonomy `tag` (with vote counts). Need a concrete minimum vote-count threshold for including a folksonomy tag, and whether genres and tags get separate schema tables or a unified table with a `is_curated_genre` flag.
3. **Schema/migration design.** No tables exist yet for genre, tag, label, or credit/relationship data. `Album`/`Artist` (`backend/src/crate_backend/models/catalog.py`) only have `musicbrainz_id`/`musicbrainz_release_group_id` for identity. Need to design: Genre/Tag tables + album join tables (with vote-count/weight), Label table + album-label join, a Credit table (or separate performer/production credit tables) capturing person + role + optional instrument, and an artist-to-artist relationship (graph edge) table.
4. **Testing/validation approach**, per Phase 2 step 9 of the project plan: duplicate identifiers, orphan relationships, missing artists, invalid dates, metadata coverage.
5. **Provenance/licensing recording**, per Phase 2 step 10: dump data is CC0, but Cover Art Archive images are user-uploaded and carry per-image licensing that is *not* CC0 — need to decide how/whether to capture per-image license metadata alongside `cover_art_url`.
6. **Rate limiting/backoff specifics for the Cover Art Archive stage** — no hard documented limit like MusicBrainz's, but needs a concrete pacing policy.

## Related files
- `docs/crate-ml-engineering-project-plan.md` — the overall phased project plan this design implements Phase 2 of.
- `backend/src/crate_backend/models/catalog.py` — existing `Album`/`Artist` models to be extended.
- `backend/src/crate_backend/scripts/seed_catalog.py` — the Phase 1 seed script this pipeline supersedes.

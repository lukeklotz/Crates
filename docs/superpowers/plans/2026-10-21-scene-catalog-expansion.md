# Scene-Based Catalog Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Grow Crate's 25,000-album catalog by pulling albums from named scenes that have entry points, depth and connectors to nearby scenes (originally aimed at 100–150k; after the first profile the owner accepted about 60–75k, see Checkpoint decisions). Albums are added in measured batches (+15k, then everything left), and recommendations are compared after each batch.

**Architecture:** A hand-edited `catalog/scenes.toml` lists the scenes, their year windows, MusicBrainz terms and budget shares, plus the *paths* between scenes. One streaming pass over the release-group dump writes a compact **pool file** of every eligible album and a profile report. A pure selector reads the pool and the current catalog, then picks a batch scene by scene. It uses a greedy rule with diminishing returns per artist and for broad-tag-only albums, and it reserves slices for connectors, live albums and well-described deep cuts. The existing ingest code upserts the batch. A coverage report and a path-reach report measure what changed, alongside the existing graded answer key and a new scene key.

**Tech Stack:** Python 3.12 (`tomllib`, `gzip`, `heapq`), SQLAlchemy async + Postgres, pytest, and the existing `crate_backend` MusicBrainz, evaluation and model-build modules.

**Spec:** No separate spec. The owner gave the brief on 2026-10-21 and skipped the design interview. The **Design** section below records the brief's decisions, and everything marked *(my call)* is a default the owner hasn't confirmed. Background: `docs/superpowers/specs/2026-09-20-musicbrainz-ingestion-design.md` (current ingest), `docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md` (eval key).

## Design

**From the owner's brief:**
- Target 100–150k albums. Additions come from chosen scenes, not from a global tag-count ranking. **The success test is better coverage and recommendations, not the album count.** If the scene pools run out, a batch comes in under its target. It is never padded with generic albums.
- Each scene has three layers: recognizable **entry points**, **depth** beyond the obvious records, and **connectors** to nearby scenes. The scene *paths* (for example soul → funk → early hip hop → 1990s rap) also guide later tag normalization and evaluation. That normalization work is not in this plan, but the paths are written down here so it can use them.
- Studio albums are the default, and live albums get a smaller allocation.
- Step 1 is to profile the full dump once. Count eligible albums by scene, first-release year, positive descriptive tag, artist and overlap with the existing 25k. The ~745k "with tags" figure includes albums outside Crate's rules, so it is not the usable pool.
- Within a scene, favour strong tag evidence. Reduce the reward for the tenth album by one artist and for the thousandth album carrying only a broad tag such as "rock". Reserve room for less famous, well-described albums. Artist limits are soft.
- Keep the existing 25k albums untouched. Add +25k, rebuild every model and compare. Then add +50k, rebuild and compare again. Model files omit new albums until they are rebuilt, and the API keeps a loaded model until it restarts.
- Deprioritize generic 2000s guitar indie, garage-rock revival and broad "alternative rock".
- Scenes: the two pasted tables, encoded below in `catalog/scenes.toml`.

**Decisions made here (my calls, all tunable in `scenes.toml` after the profile):**
- **Positive descriptive term:** a genre or tag with vote count > 0 that is not in `nondescriptive_terms` and not a year or decade ("1995", "90s", "1990s"). Names are normalized with the existing `normalize_term`. Eligibility is the current rule (primary type Album; secondary types none or Live only) plus at least one positive descriptive term.
- **Scene match:** the album's first-release year is inside the scene's window (no year means no scene, never guessed). At least `min_matched_terms` of its terms are scene terms, it has one of `requires_any` if that is set, and it has none of `exclude_terms`. The **home scene** is the matching scene with the highest evidence (ties go to the earlier scene in the file).
- **Evidence** = Σ over matched terms of `w × log2(1 + votes)`, where w = 1.0 for scene `terms` and `broad_weight` (0.3) for `broad_terms`. An album is **broad-only** when it matches only broad terms.
- **Connector:** an album that also matches the terms of a scene next to its home scene on some path. The other scene's year window is ignored, because a 1983 funk/electro record is a funk → hip hop connector even though the funk scene ends in 1982.
- **Gain during selection** = evidence × artist factor × broad factor × deprioritized factor:
  - **Artist factor:** with k = the artist's albums already counted, the factor is 1.0 while k < `artist_free_albums` (3), and `artist_decay ** (k - artist_free_albums + 1)` (decay 0.75) after that, so the 10th album gets about 0.1. Major discographies stay reachable because their albums carry high evidence. The artist is the first credited artist's MBID, and the count covers the whole catalog (existing plus already picked). An album with no credited artist is never decayed.
  - **Broad factor:** for broad-only albums, `1 / (1 + n / broad_only_halfway)` (halfway = 200), where n = broad-only albums already in that home scene.
  - **Deprioritized factor:** `deprioritized_factor` (0.4) when the album's single highest-voted descriptive term is in `deprioritized_terms`.
- **Batch budget:** the target is split across scenes by `share`, using largest-remainder rounding so the parts sum exactly to the target. Within a scene: `live_share` (5%) for live albums, `connector_share` (15%) for connectors and `deep_cut_share` (15%) for deep cuts. The rest is open.
- **Deep cut** ("less famous, well described"): total positive votes on the album ≤ `deep_cut_max_votes` (6), at least `deep_cut_min_terms` (4) distinct descriptive terms, and at least `deep_cut_min_scene_terms` (2) matched scene terms. There's no Last.fm data for albums outside the catalog, so tag votes stand in for fame.
- **Entry points** aren't a separate slice. The open slice's greedy fill takes the highest-evidence albums first, and the coverage report measures **entry-point coverage**: the share of each scene's top 100 pool albums by evidence that are in the catalog.
- **2000s indie is not its own scene.** It enters only as connectors (for example albums tagged both shoegaze and dream pop in the 2000s). This keeps the owner's shoegaze → 2000s indie → dream pop path without pulling in generic guitar indie.
- **Batch fill order:** (1) reserved slices (live, connector, deep cut), each by lazy greedy over its own candidates, then (2) the open slice over every remaining studio candidate in the scene. Unused reserved capacity goes to the open slice. A scene whose candidates run out gives its shortfall back, and the shortfall is shared among scenes with candidates left, by share, until the target is met or every pool is empty.
- **The pool file holds raw records, not scene matches.** Matches are recomputed from `scenes.toml` on every read, so retuning scenes never needs another 10-minute dump pass.
- **Live status comes from the pool**, because the `albums` table doesn't store secondary types. No migration.
- **Rollback is a `pg_dump` taken before each batch ingest**, not a delete script.
- **Evaluation:**
  - (a) Re-run the existing 10-seed key: pool, grade the new pairs, score.
  - (b) A new scene key in `eval/scenes/`. About 8 seeds the owner knows, chosen from the center scenes and paths and already in the 25k. Graded on the 25k before batch 1 so there's a baseline, using `overlap,tfidf-tags,embed-tags` to keep grading small.
  - (c) An ungraded path-reach report on frozen seeds.
  - (d) The coverage report.
  - Path reach is defined by tags, so it partly flatters tag-based recommenders. It is a coverage check, not a quality score. Quality comes from the graded keys.

## Checkpoint decisions (owner, 2026-10-21, after the first dump profile)

The first profile (`catalog/reports/profile-2026-10-21.md`) showed that broad tags were filling the scenes. "Electronic" put Merzbow and Prince in the motorik center, and "jazz" put Anthony Braxton in lounge. The owner decided the following, and these override the Design section above where they differ:

- **Stay faithful to the scenes.** A catalog of about 60–75k, or smaller, is fine. Count is not the goal.
- **Broad tags never place an album on their own**, in any scene, with no exceptions. They only add evidence to an album that already has a scene term. The broad-only reward decay and `broad_only_halfway` are gone.
- **Dark, depressive and atonal albums are cut** through a global `cut_terms` list in `scenes.toml`: metal, noise, industrial, drone and dark ambient, dark genres, experimental sound work, free jazz and free improvisation, avant-garde, no wave, noise rock, musique concrète, and meditation. New age is kept. Goth and gothic rock are kept as part of post-punk.
- **Main-tag rule:** a cut term, a scene's `exclude_terms` or a deprioritized term only applies when it is one of the album's main tags. The main tags are those with the top vote count, and ties count. This keeps albums like *Loveless* (noise rock 3, shoegaze 19) and *A Love Supreme* (free jazz 5).
- **Ambient-only albums are dropped:** an album whose only scene term is "ambient" also needs another scene's term (`needs_company = ["ambient"]`).
- **The Japanese scene's gate no longer includes "j pop"**, which was pulling in idol pop.
- **The center stays thin.** There is no hand-picked artist list and no rule that brings in an artist's other albums. MusicBrainz barely tags this music.
- **Connectors through a shared term stay**, for example soul ↔ funk via "soul" and the krautrock era bridges.
- **Batches:** batch 1 is +15,000, and batch 2 is everything left (`--target 100000`; the selector stops when the pools run out). This replaces +25k then +50k.

## Global Constraints

- Never modify or delete an album already in the catalog when ingesting a batch. Existing rows are skipped, not upserted.
- Selection output is deterministic for the same pool, catalog and `scenes.toml` (ties break by MusicBrainz ID).
- Settings: `catalog_dir = _REPO_ROOT / "catalog"` and `scene_pool_path = _REPO_ROOT / "MusicBrainz" / "scene-pool.jsonl.gz"` (gitignored with the dumps).
- Committed outputs: `catalog/scenes.toml`, `catalog/batches/batch-N.jsonl` + `.md`, `catalog/reports/*.md`, `eval/scenes/seeds.json`, `eval/path-reach-seeds.json`, `eval/results/*.md`. Not committed: the pool file, dumps, `eval/scenes/judgments.jsonl`, `eval/scenes/pool.jsonl` and `backups/`.
- Reuse `normalize_term` / `merge_term_votes` from `recommend/text_cleaning.py`. Don't change them, because the TF-IDF model depends on them.
- Match the surrounding code: module docstring with a `Run with:` line, pure logic separate from I/O, and tests in `backend/tests/` that use `db_session` for anything touching Postgres.
- Run backend commands from `backend/` with `uv run`. Run tests with `uv run pytest`.

## Review Focus

1. **No usable first-release year** (missing, "????" or outside every window): the album is in no scene and is counted as "no year" in the profile, never guessed. Test: Task 2, `test_classify_without_year_is_none`.
2. **Zero or negative votes, nondescriptive tags ("seen live"), year tags ("90s")**: these never count as evidence or toward "well described". Test: Task 2, `test_descriptive_terms_drops_non_positive_nondescriptive_and_years`.
3. **Re-running after a partial ingest, or an album already in the 25k**: nothing already in the database is picked, and ingesting the same batch twice is a no-op that leaves existing titles untouched. Tests: Task 5, `test_select_never_picks_catalog_albums`; Task 7, `test_ingest_batch_skips_existing_and_is_rerunnable`.
4. **A scene pool smaller than its budget**: the shortfall moves to other scenes by share, the total never exceeds the target, the summary names each scene that ran out, and a batch whose pools all run out is smaller than the target, not padded. Tests: Task 5, `test_shortfall_moves_to_scenes_with_candidates`, `test_exhausted_pool_returns_fewer_than_target`.
5. **No credited artist, or several credited artists**: decay keys on the first credited artist's MBID, and albums with no artist never decay each other. Tests: Task 3, `test_primary_artist_is_first_credit`; Task 5, `test_albums_without_artist_are_not_decayed`.

---

### Task 1: Scene config file and loader

**Files:**
- Create: `catalog/scenes.toml`
- Create: `backend/src/crate_backend/scenes/__init__.py`, `backend/src/crate_backend/scenes/config.py`
- Modify: `backend/src/crate_backend/core/config.py` (add `catalog_dir`, `scene_pool_path` after the MusicBrainz settings)
- Test: `backend/tests/test_scene_config.py`

**Interfaces:**
- Produces:
  - `class SceneConfigError(ValueError)`
  - `@dataclass(frozen=True) Scene(id: str, name: str, tier: str, years: tuple[int, int | None], share: float, terms: frozenset[str], broad_terms: frozenset[str], requires_any: frozenset[str], exclude_terms: frozenset[str], min_matched_terms: int = 1)`
  - `@dataclass(frozen=True) ScenePath(name: str, scenes: tuple[str, ...])`
  - `@dataclass(frozen=True) SelectionSettings(live_share, connector_share, deep_cut_share, broad_weight, artist_free_albums, artist_decay, broad_only_halfway, deprioritized_factor, deep_cut_max_votes, deep_cut_min_terms, deep_cut_min_scene_terms)`, with float/int fields named exactly as the `[settings]` keys
  - `@dataclass(frozen=True) SceneConfig(settings: SelectionSettings, scenes: tuple[Scene, ...], paths: tuple[ScenePath, ...], nondescriptive_terms: frozenset[str], deprioritized_terms: frozenset[str])` with methods `scene(id) -> Scene` and `neighbors(scene_id) -> frozenset[str]`
  - `TIERS = ("center", "neighbor", "roots", "echoes", "wider")`
  - `parse_scene_config(text: str) -> SceneConfig`, `load_scene_config(path: Path | None = None) -> SceneConfig` (default `Path(settings.catalog_dir) / "scenes.toml"`)

- [ ] **Step 1: Write the failing tests**

```python
MINIMAL = """
[settings]
live_share = 0.05
connector_share = 0.15
deep_cut_share = 0.15
broad_weight = 0.3
artist_free_albums = 3
artist_decay = 0.75
broad_only_halfway = 200
deprioritized_factor = 0.4
deep_cut_max_votes = 6
deep_cut_min_terms = 4
deep_cut_min_scene_terms = 2
nondescriptive_terms = ["Seen Live"]
deprioritized_terms = ["Indie Rock"]

[[scene]]
id = "a"
name = "A"
tier = "center"
years = [1994, 2006]
share = 2
terms = ["Shibuya-kei"]

[[scene]]
id = "b"
name = "B"
tier = "echoes"
years = [2005]
share = 1
terms = ["hauntology"]

[[scene]]
id = "c"
name = "C"
tier = "roots"
years = [1965, 1982]
share = 1
terms = ["krautrock"]

[[path]]
name = "a to c"
scenes = ["a", "b", "c"]
"""

def test_load_normalizes_terms():
    config = parse_scene_config(MINIMAL)
    assert config.scene("a").terms == frozenset({"shibuya kei"})
    assert config.nondescriptive_terms == frozenset({"seen live"})
    assert config.deprioritized_terms == frozenset({"indie rock"})

def test_one_element_years_are_open_ended():
    assert parse_scene_config(MINIMAL).scene("b").years == (2005, None)

def test_neighbors_follow_adjacent_path_steps():
    config = parse_scene_config(MINIMAL)
    assert config.neighbors("b") == frozenset({"a", "c"})
    assert config.neighbors("a") == frozenset({"b"})

def test_unknown_scene_in_path_is_an_error():
    with pytest.raises(SceneConfigError, match="missing"):
        parse_scene_config(MINIMAL.replace('"a", "b", "c"', '"a", "missing"'))

def test_duplicate_scene_id_is_an_error():
    with pytest.raises(SceneConfigError, match="duplicate scene id 'c'"):
        parse_scene_config(MINIMAL.replace('id = "b"', 'id = "c"'))

def test_backwards_years_are_an_error():
    with pytest.raises(SceneConfigError, match="'a'"):
        parse_scene_config(MINIMAL.replace("[1994, 2006]", "[2006, 1994]"))

def test_unknown_tier_is_an_error():
    with pytest.raises(SceneConfigError, match="tier"):
        parse_scene_config(MINIMAL.replace('tier = "center"', 'tier = "core"'))

def test_repository_scenes_file_loads():
    config = load_scene_config()
    assert len(config.scenes) == 21
    assert sum(s.share for s in config.scenes) == 100
    assert {s.tier for s in config.scenes} == set(TIERS)
```

- [ ] **Step 2: Run** `uv run pytest tests/test_scene_config.py -v`. Expected: FAIL (module not found).

- [ ] **Step 3: Implement `crate_backend/scenes/config.py`** with `tomllib`. Normalize every term list with `normalize_term`. Validate unique ids, known tiers, ordered years, `share > 0` and that every path step names a known scene, and name the offending id or path in each error. Add both settings to `core/config.py` with comments like the neighbouring ones.

- [ ] **Step 4: Write `catalog/scenes.toml`** exactly as below. This is the owner's brief in data form, and the profile run in Task 10 is what tunes it.

```toml
# Crate catalog scenes: what the batch selector pulls from the MusicBrainz
# dump, and the paths between scenes that later tag normalization and
# evaluation follow. Plan: docs/superpowers/plans/2026-10-21-scene-catalog-expansion.md
#
# Terms are MusicBrainz genre or tag names, normalized on load (lowercase,
# hyphens to spaces), so "Shibuya-kei" and "shibuya kei" are the same term.
# terms count fully; broad_terms count at broad_weight and an album matching
# only broad terms is "broad-only" and gets diminishing returns.
# years = [from, to] inclusive, or [from] for "to the present".
# share = this scene's part of each batch's additions (shares sum to 100).

[settings]
live_share = 0.05
connector_share = 0.15
deep_cut_share = 0.15
broad_weight = 0.3
artist_free_albums = 3
artist_decay = 0.75
broad_only_halfway = 200
deprioritized_factor = 0.4
deep_cut_max_votes = 6
deep_cut_min_terms = 4
deep_cut_min_scene_terms = 2

# Year and decade tags ("1995", "90s") are dropped in code.
nondescriptive_terms = [
  "seen live", "favorites", "favourite", "favorite", "favourites", "albums i own",
  "owned", "vinyl", "cd", "check out", "to listen", "wishlist", "my collection",
  "1001 albums you must hear before you die", "best of", "classic", "masterpiece",
  "under 2000 listeners", "spotify", "amazing", "awesome", "beautiful",
]

# An album whose single highest-voted descriptive term is one of these has its
# gain multiplied by deprioritized_factor.
deprioritized_terms = [
  "indie rock", "garage rock revival", "post punk revival", "alternative rock",
  "rock", "pop rock",
]

# ---------------------------------------------------------------- center
[[scene]]
id = "motorik-indietronica"
name = "Motorik pop, experimental indie pop, psychedelic electronic pop, indietronica, retrofuturist pop"
tier = "center"
years = [1994, 2006]
share = 11
terms = ["indietronica", "motorik", "krautrock", "experimental pop", "avant pop",
         "psychedelic pop", "electronica", "retro futurism", "space rock revival"]
broad_terms = ["indie pop", "electronic", "post rock", "pop", "experimental"]

[[scene]]
id = "japanese-indie-pop"
name = "Japanese home-recorded indie pop, picopop, electronic twee, softer and experimental Shibuya-kei"
tier = "center"
years = [1994, 2004]
share = 8
terms = ["shibuya kei", "picopop", "twee pop", "japanese indie", "j indie", "bedroom pop",
         "lo fi", "electropop"]
broad_terms = ["indie pop", "j pop", "pop", "electronic", "japanese"]
requires_any = ["shibuya kei", "picopop", "japanese", "japanese indie", "j indie", "j pop"]

[[scene]]
id = "space-age-lounge-chamber"
name = "Space-age pop, lounge and bossa-influenced indie pop, sophisticated chamber pop"
tier = "center"
years = [1993, 2006]
share = 11
terms = ["space age pop", "lounge", "exotica", "bossa nova", "chamber pop", "baroque pop",
         "easy listening", "sophisti pop", "orchestral pop"]
broad_terms = ["indie pop", "pop", "jazz"]

# ---------------------------------------------------------------- close neighbors
[[scene]]
id = "dream-noise-pop"
name = "Dream pop, gentle noise pop, twee"
tier = "neighbor"
years = [1990, 2008]
share = 6
terms = ["dream pop", "noise pop", "ethereal wave", "twee pop", "jangle pop"]
broad_terms = ["indie pop", "indie rock", "pop"]

[[scene]]
id = "art-pop-downtempo"
name = "Art pop, electronic folk, downtempo pop"
tier = "neighbor"
years = [1990, 2008]
share = 6
terms = ["art pop", "folktronica", "downtempo", "ambient pop", "chamber folk"]
broad_terms = ["electronic", "pop", "folk", "indie folk"]

[[scene]]
id = "sample-psych-pop"
name = "Sample-based psychedelic pop"
tier = "neighbor"
years = [1990, 2008]
share = 6
terms = ["plunderphonics", "sound collage", "neo psychedelia", "sampledelia",
         "psychedelic pop"]
broad_terms = ["psychedelic", "electronic", "experimental"]

# ---------------------------------------------------------------- roots
[[scene]]
id = "psych-sunshine-pop"
name = "Psychedelic and sunshine pop"
tier = "roots"
years = [1965, 1982]
share = 3
terms = ["psychedelic pop", "sunshine pop", "baroque pop", "orchestral pop"]
broad_terms = ["psychedelic rock", "pop", "psychedelic"]

[[scene]]
id = "french-pop-yeye"
name = "French pop and yé-yé"
tier = "roots"
years = [1965, 1982]
share = 3
terms = ["yé yé", "ye ye", "french pop", "variété française", "nouvelle chanson"]
broad_terms = ["chanson", "chanson française", "pop", "french"]

[[scene]]
id = "brazil-bossa-tropicalia"
name = "Brazilian bossa nova and tropicália"
tier = "roots"
years = [1965, 1982]
share = 3
terms = ["bossa nova", "tropicália", "tropicalia", "mpb", "samba", "samba rock",
         "brazilian"]
broad_terms = ["latin", "jazz", "brazil"]

[[scene]]
id = "kosmische-motorik"
name = "German kosmische and motorik music"
tier = "roots"
years = [1965, 1982]
share = 3
terms = ["krautrock", "kosmische musik", "kosmische", "berlin school", "motorik",
         "progressive electronic"]
broad_terms = ["electronic", "experimental", "progressive rock"]

[[scene]]
id = "early-electronic-library"
name = "Early electronic pop and library music"
tier = "roots"
years = [1965, 1982]
share = 3
terms = ["library music", "space age pop", "musique concrète", "radiophonic", "moog",
         "synthpop", "synth pop", "exotica"]
broad_terms = ["electronic", "easy listening", "experimental"]

# ---------------------------------------------------------------- later echoes
[[scene]]
id = "later-echoes"
name = "Hauntology, analog-synth pop, experimental bedroom pop, neo-psychedelic pop (close sound only)"
tier = "echoes"
years = [2005]
share = 4
min_matched_terms = 2
terms = ["hauntology", "hypnagogic pop", "bedroom pop", "neo psychedelia", "chillwave",
         "psychedelic pop", "indietronica", "library music"]
broad_terms = ["synthpop", "synth pop", "electronic", "indie pop"]

# ---------------------------------------------------------------- wider scenes
[[scene]]
id = "soul"
name = "Soul, deep soul, psychedelic soul, gospel-influenced soul"
tier = "wider"
years = [1960, 1982]
share = 4
terms = ["soul", "deep soul", "southern soul", "psychedelic soul", "philly soul",
         "northern soul", "chicago soul", "smooth soul"]
broad_terms = ["gospel", "rhythm and blues", "r and b"]

[[scene]]
id = "funk-early-disco"
name = "Funk and early disco"
tier = "wider"
years = [1965, 1982]
share = 3
terms = ["funk", "p funk", "disco", "boogie", "funk soul"]
broad_terms = ["soul", "dance"]

[[scene]]
id = "early-hip-hop"
name = "Early hip hop"
tier = "wider"
years = [1979, 1991]
share = 3
terms = ["old school hip hop", "golden age hip hop", "electro"]
broad_terms = ["hip hop", "rap"]

[[scene]]
id = "nineties-rap"
name = "1990s East Coast, West Coast and Southern rap; boom bap, jazz rap, alternative and sample-heavy hip hop"
tier = "wider"
years = [1986, 2005]
share = 6
terms = ["east coast hip hop", "west coast hip hop", "southern hip hop", "boom bap",
         "jazz rap", "alternative hip hop", "conscious hip hop", "abstract hip hop",
         "g funk", "hardcore hip hop", "instrumental hip hop", "experimental hip hop",
         "turntablism", "gangsta rap"]
broad_terms = ["hip hop", "rap"]

[[scene]]
id = "hard-bop-modal-spiritual"
name = "Hard bop, modal and spiritual jazz"
tier = "wider"
years = [1955, 1980]
share = 4
terms = ["hard bop", "modal jazz", "spiritual jazz", "post bop", "soul jazz"]
broad_terms = ["jazz"]

[[scene]]
id = "fusion-brazilian-jazz"
name = "Jazz fusion and Brazilian jazz"
tier = "wider"
years = [1955, 1980]
share = 3
terms = ["jazz fusion", "jazz funk", "brazilian jazz", "samba jazz", "jazz rock"]
broad_terms = ["jazz"]

[[scene]]
id = "post-punk-shoegaze"
name = "Post-punk and shoegaze"
tier = "wider"
years = [1978, 2010]
share = 4
terms = ["post punk", "shoegaze", "coldwave", "minimal wave", "no wave"]
broad_terms = ["new wave", "indie rock"]
exclude_terms = ["post punk revival"]

[[scene]]
id = "ambient-trip-hop-idm"
name = "Ambient, trip hop and leftfield electronic"
tier = "wider"
years = [1978, 2010]
share = 4
terms = ["ambient", "trip hop", "idm", "leftfield", "glitch", "illbient", "ambient techno"]
broad_terms = ["electronic", "experimental", "electronica"]
exclude_terms = ["dark ambient", "harsh noise", "power electronics"]

[[scene]]
id = "house-techno"
name = "House and techno (the parts that lead toward the core)"
tier = "wider"
years = [1985, 2010]
share = 2
terms = ["deep house", "acid house", "chicago house", "detroit techno", "microhouse",
         "dub techno", "minimal techno"]
broad_terms = ["house", "techno", "electronic"]
exclude_terms = ["trance", "hardstyle", "eurodance", "hard techno", "gabber", "psytrance"]

# ---------------------------------------------------------------- paths
# Adjacent scenes on a path are "neighbors": an album matching both is a
# connector. Paths also name what later tag normalization and evaluation follow.

[[path]]
name = "soul to 1990s rap"
scenes = ["soul", "funk-early-disco", "early-hip-hop", "nineties-rap"]

[[path]]
name = "post-punk and shoegaze through 2000s indie into dream pop and the center"
scenes = ["post-punk-shoegaze", "dream-noise-pop", "motorik-indietronica"]

[[path]]
name = "kosmische to indietronica to the later echoes"
scenes = ["kosmische-motorik", "motorik-indietronica", "later-echoes"]

[[path]]
name = "Brazil to lounge pop"
scenes = ["brazil-bossa-tropicalia", "fusion-brazilian-jazz", "space-age-lounge-chamber"]

[[path]]
name = "jazz to funk"
scenes = ["hard-bop-modal-spiritual", "fusion-brazilian-jazz", "funk-early-disco"]

[[path]]
name = "sample-heavy rap to trip hop to sample-based pop"
scenes = ["nineties-rap", "ambient-trip-hop-idm", "sample-psych-pop"]

[[path]]
name = "yé-yé to lounge pop to Shibuya-kei"
scenes = ["french-pop-yeye", "space-age-lounge-chamber", "japanese-indie-pop"]

[[path]]
name = "1960s psych pop to sample psych to the center"
scenes = ["psych-sunshine-pop", "sample-psych-pop", "motorik-indietronica"]

[[path]]
name = "library music to hauntology"
scenes = ["early-electronic-library", "later-echoes"]

[[path]]
name = "house and ambient into downtempo pop"
scenes = ["house-techno", "ambient-trip-hop-idm", "art-pop-downtempo"]

[[path]]
name = "dream pop to art pop"
scenes = ["dream-noise-pop", "art-pop-downtempo", "space-age-lounge-chamber"]
```

- [ ] **Step 5: Run** `uv run pytest tests/test_scene_config.py -v`. Expected: PASS (8 tests).

- [ ] **Step 6: Commit**

```bash
git add catalog/scenes.toml backend/src/crate_backend/scenes backend/src/crate_backend/core/config.py backend/tests/test_scene_config.py
git commit -m "feat: describe catalog scenes and the paths between them in scenes.toml"
```

---

### Task 2: Descriptive terms and scene matching

**Files:**
- Create: `backend/src/crate_backend/scenes/matching.py`
- Test: `backend/tests/test_scene_matching.py`

**Interfaces:**
- Consumes: `SceneConfig`, `Scene` (Task 1); `merge_term_votes` (`recommend/text_cleaning.py`)
- Produces:
  - `descriptive_terms(genres: list[dict], tags: list[dict], config: SceneConfig) -> dict[str, int]`, taking MusicBrainz `{"name", "count"}` dicts and returning normalized term → votes, positive only
  - `scene_evidence(terms: dict[str, int], scene: Scene, broad_weight: float) -> float`
  - `@dataclass(frozen=True) SceneMatch(home: str, evidence: float, broad_only: bool, matched_terms: tuple[str, ...], connects_to: tuple[str, ...])`, with `matched_terms` and `connects_to` sorted
  - `classify(terms: dict[str, int], year: int | None, config: SceneConfig) -> SceneMatch | None`

- [ ] **Step 1: Write the failing tests.** Reuse `MINIMAL` from Task 1's tests by moving it into `tests/scene_fixtures.py`, and add a scene `d` (tier `wider`, years `[1978, 2010]`, share 1, `terms = ["shoegaze", "dream pop"]`, `broad_terms = ["rock"]`, `exclude_terms = ["post punk revival"]`) plus a path `["d", "a"]`. Update Task 1's tests to import from there.

```python
def test_descriptive_terms_drops_non_positive_nondescriptive_and_years():
    terms = descriptive_terms(
        [{"name": "Shoegaze", "count": 2}],
        [{"name": "shoegaze", "count": 3}, {"name": "seen live", "count": 9},
         {"name": "90s", "count": 4}, {"name": "1991", "count": 4},
         {"name": "noise", "count": 0}, {"name": "loud", "count": -1}],
        config,
    )
    assert terms == {"shoegaze": 3}

def test_scene_evidence_weights_broad_terms():
    assert scene_evidence({"shoegaze": 3, "rock": 5}, config.scene("d"), 0.3) == pytest.approx(
        2 + 0.3 * math.log2(6)
    )

def test_classify_without_year_is_none():
    assert classify({"shoegaze": 3}, None, config) is None

def test_classify_outside_every_window_is_none():
    assert classify({"shoegaze": 3}, 1970, config) is None

def test_exclude_term_removes_scene():
    assert classify({"shoegaze": 3, "post punk revival": 1}, 1991, config) is None

def test_broad_only_match():
    match = classify({"rock": 4}, 1991, config)
    assert match.home == "d" and match.broad_only is True

def test_home_is_highest_evidence_and_ties_go_to_earlier_scene():
    # a: shibuya kei (1994–2006); d: shoegaze (1978–2010); both match in 1996
    assert classify({"shibuya kei": 1, "shoegaze": 7}, 1996, config).home == "d"
    assert classify({"shibuya kei": 3, "shoegaze": 3}, 1996, config).home == "a"

def test_connector_ignores_neighbor_year_window():
    # c (krautrock) is 1965–1982 but adjacent to b on the path; 2010 is only in b
    match = classify({"hauntology": 2, "krautrock": 1}, 2010, config)
    assert match.home == "b" and match.connects_to == ("c",)

def test_matching_a_non_neighbor_is_not_a_connector():
    match = classify({"shoegaze": 2, "hauntology": 1}, 2008, config)
    assert match.home == "d" and match.connects_to == ()

def test_min_matched_terms_and_requires_any():
    # Rewrite scene b with min_matched_terms = 2 and scene a with
    # requires_any = ["japanese"] via string replacement in the fixture text.
    ...
```
Write the last test as two concrete assertions. A `{"hauntology": 2}` album in 2010 doesn't match b when `min_matched_terms = 2`, and a `{"shibuya kei": 2}` album in 1996 doesn't match a when `requires_any = ["japanese"]`, though it does once `"japanese": 1` is added.

- [ ] **Step 2: Run** `uv run pytest tests/test_scene_matching.py -v`. Expected: FAIL (import error).

- [ ] **Step 3: Implement `matching.py`.** Use `merge_term_votes` over genres and tags, then drop votes ≤ 0, `config.nondescriptive_terms`, and terms matching `^\d{2,4}s?$`. A scene matches when its window holds the year (`years[1] is None` means open-ended), the `requires_any` and `exclude_terms` rules pass, and `len(matched) >= min_matched_terms`. A neighbor is a connector when its terms match, its `requires_any`/`exclude_terms` rules pass and `min_matched_terms` is met. Its years are ignored.

- [ ] **Step 4: Run** `uv run pytest tests/test_scene_matching.py tests/test_scene_config.py -v`. Expected: PASS.

- [ ] **Step 5: Commit** `feat: match albums to catalog scenes by descriptive terms and year`

---

### Task 3: Pool file, dump profile and the profile script

**Files:**
- Create: `backend/src/crate_backend/scenes/pool.py`, `backend/src/crate_backend/scenes/profile.py`, `backend/src/crate_backend/scripts/profile_catalog_pool.py`
- Modify: `backend/src/crate_backend/musicbrainz/extract.py` (rename `_is_catalog_eligible` → `is_catalog_eligible` and `_to_candidate` → `to_candidate`, and update callers; behaviour unchanged)
- Test: `backend/tests/test_scene_pool.py`, `backend/tests/test_scene_profile.py`, `backend/tests/test_profile_catalog_pool_script.py`

**Interfaces:**
- Consumes: `classify`, `descriptive_terms`, `SceneMatch` (Task 2); `is_catalog_eligible`, `to_candidate`, `stream_jsonl_from_tar`, `read_dump_metadata`
- Produces:
  - `POOL_FIELDS = ("id", "title", "primary-type", "secondary-types", "first-release-date", "artist-credit", "genres", "tags")`
  - `@dataclass(frozen=True) PoolAlbum(musicbrainz_id: str, title: str, artist_name: str, year: int | None, is_live: bool, primary_artist_id: str | None, terms: dict[str, int], match: SceneMatch | None, record: dict)`, with `total_votes` (sum of `terms` values) and `n_terms` properties
  - `to_pool_album(record: dict, config: SceneConfig) -> PoolAlbum | None`, which is None unless `is_catalog_eligible` holds and there is at least one descriptive term. The year is parsed like `musicbrainz.ingest._release_year`, so move that helper to `extract.py` as `release_year` and import it in both places.
  - `write_pool(records: Iterable[dict], path: Path) -> int` writes gzip JSONL of `POOL_FIELDS` only and returns the count written. `read_pool(path: Path, config: SceneConfig) -> Iterator[PoolAlbum]` re-classifies on read.
  - `profile.ProfileCounts` has `add_release_group(record: dict, pool_album: PoolAlbum | None, in_catalog: bool) -> None` and the funnel fields `release_groups`, `album_primary`, `allowed_types`, `with_any_term`, `with_descriptive_term`, `in_scene`, `in_scene_in_catalog`, `no_year`, plus per-scene `Counter`s. `render_profile(counts: ProfileCounts, config: SceneConfig, *, snapshot: str, catalog_size: int) -> str`
  - `select.is_deep_cut(album: PoolAlbum, settings: SelectionSettings) -> bool`, which uses `album.total_votes`, `album.n_terms` and `len(album.match.matched_terms)` and returns False when `match` is None
  - Script `profile_catalog_pool`: `profile_dump(dump_dir: Path, pool_path: Path, report_dir: Path) -> Path` and `profile_pool(pool_path: Path, report_dir: Path) -> Path`, each returning the report path

The report sections, in order:
1. **Funnel**, one line per field above.
2. **Scenes**: one table row per scene with studio, live, in catalog, not in catalog, broad-only, deep-cut candidates, connector candidates, distinct artists and the top 5 artists.
3. **Years**: eligible and in-scene albums per decade, plus "no year".
4. **Terms**: the top 300 descriptive terms by album count, with the scene ids that list each one or `unassigned`, and `deprioritized` where that applies.
5. **Artists**: albums per artist among in-scene albums, bucketed as 1, 2–3, 4–9, 10–24 and 25+, then the top 25 artists.
6. **Existing catalog**: how many of the 25k are in the pool, in a scene (by scene), or not eligible under these rules.

Deep-cut candidates use `select.is_deep_cut` from Task 5, so implement `is_deep_cut` in Task 3 inside `scenes/select.py` with its test, and Task 5 fills in the rest of that module.

- [ ] **Step 1: Write the failing tests** (`_release_group` helper as in `tests/test_extract.py`):
  - `test_pool_album_none_for_single_compilation_or_no_descriptive_terms`
  - `test_pool_album_marks_live` (`secondary_types=["Live"]` → `is_live is True`)
  - `test_primary_artist_is_first_credit`: two credits give the first credit's id, and `artist_credit=[]` gives `None`
  - `test_pool_round_trip_reclassifies_with_new_config`: write a record tagged `shoegaze`, then read it with the fixture config (home `d`) and with a config whose scene `d` drops `shoegaze` (`match is None`)
  - `test_write_pool_keeps_only_pool_fields`: a record with an extra `"relations"` key doesn't have it after the round trip
  - `test_is_deep_cut` (fixture settings: max votes 6, min terms 4, min scene terms 2; 1991 album): `{"shoegaze":1,"dream pop":1,"noise":1,"lo fi":1}`, which matches 2 of scene d's terms, → True, the same with `"shoegaze": 5` → False (8 votes), and only 3 terms → False
  - `test_profile_funnel_counts`: 6 synthetic records (Single; Compilation; Album with no tags; Album with only "seen live"; Album with no year tagged shoegaze; Album 1991 tagged shoegaze, in catalog) → `release_groups == 6, album_primary == 5, allowed_types == 4, with_any_term == 3, with_descriptive_term == 2, no_year == 1, in_scene == 1, in_scene_in_catalog == 1`
  - `test_render_profile_marks_unassigned_terms`: a term no scene lists shows up as `unassigned`
  - Script test, monkeypatching like `test_ingest_musicbrainz_script.py`: `profile_dump` writes a pool with the eligible records only and a report named `profile-<TIMESTAMP date>.md`. `profile_pool` rewrites the report from the pool without calling `stream_jsonl_from_tar` (patch it to raise).

- [ ] **Step 2: Run** the three test files. Expected: FAIL.

- [ ] **Step 3: Implement.** `profile_dump` loads the catalog's `musicbrainz_release_group_id` set once and streams the dump once. It writes pool records for every `to_pool_album`-eligible record and adds every record to `ProfileCounts`. The report goes to `Path(settings.catalog_dir) / "reports"`. The CLI is `uv run python -m crate_backend.scripts.profile_catalog_pool [--from-pool]`, and its docstring states the ~10-minute dump pass and that `--from-pool` re-profiles after editing `scenes.toml`.

- [ ] **Step 4: Run** `uv run pytest tests/test_scene_pool.py tests/test_scene_profile.py tests/test_profile_catalog_pool_script.py tests/test_extract.py tests/test_musicbrainz_ingest.py -v`. Expected: PASS.

- [ ] **Step 5: Commit** `feat: profile the release-group dump by scene and write the scene pool file`

---

### Task 4: Catalog albums with scene matches

**Files:**
- Create: `backend/src/crate_backend/scenes/catalog.py`
- Test: `backend/tests/test_catalog_scenes.py`

**Interfaces:**
- Consumes: `descriptive_terms`, `classify` (Task 2); `Album`, `AlbumGenre`, `AlbumTag`, `Genre`, `Tag`, `Artist`, `AlbumText` (WIKIPEDIA_SOURCE)
- Produces: `@dataclass(frozen=True) CatalogAlbum(album_id: uuid.UUID, musicbrainz_id: str | None, title: str, artist_name: str | None, primary_artist_id: str | None, year: int | None, terms: dict[str, int], match: SceneMatch | None, has_text: bool, popularity: float | None)` and `async load_catalog_albums(session: AsyncSession, config: SceneConfig) -> list[CatalogAlbum]`. Here `primary_artist_id` is the artist's MusicBrainz ID, so it is comparable with `PoolAlbum.primary_artist_id`.

- [ ] **Step 1: Write the failing test** `test_load_catalog_albums_matches_scenes` (db_session). Insert an album from 1991 with a shoegaze tag (count 3), an artist with an MBID and a Wikipedia `AlbumText`, plus an album with no tags. Assert the first has `match.home == "d"`, `has_text is True` and the artist MBID, and that the second has `match is None`. Filter results to the two inserted ids, because the dev database holds the real catalog.

- [ ] **Step 2: Run.** Expected: FAIL.

- [ ] **Step 3: Implement** with four bulk queries (albums+artist, genre links, tag links, album ids having Wikipedia text) assembled in Python, not one query per album. That way 100k albums load in seconds.

- [ ] **Step 4: Run.** Expected: PASS.

- [ ] **Step 5: Commit** `feat: load catalog albums with their scene matches`

---

### Task 5: Batch selector

**Files:**
- Modify: `backend/src/crate_backend/scenes/select.py` (created in Task 3 with `is_deep_cut`)
- Test: `backend/tests/test_batch_select.py`

**Interfaces:**
- Consumes: `PoolAlbum` (Task 3), `CatalogAlbum` (Task 4), `SceneConfig`
- Produces:
  - `SLICES = ("live", "connector", "deep", "open")`
  - `@dataclass(frozen=True) Pick(musicbrainz_id: str, scene: str, slice: str, gain: float, evidence: float)`
  - `@dataclass BatchResult(picks: list[Pick], budgets: dict[str, int], shortfalls: dict[str, int])`, where `shortfalls` maps a scene to the budget it could not fill before redistribution
  - `scene_budgets(config: SceneConfig, target: int, scene_ids: Iterable[str] | None = None) -> dict[str, int]` (largest remainder, exact sum, ties to earlier scene)
  - `select_batch(pool: Iterable[PoolAlbum], catalog: Iterable[CatalogAlbum], config: SceneConfig, target: int) -> BatchResult`

Algorithm (my call, from the Design section). Candidates are the pool albums with a `match` and an MBID not in the catalog. Counters start from the catalog: artist counts by `primary_artist_id`, and broad-only counts by home scene. For each scene, slice capacities are `floor(budget × share)` for live, connector and deep, with the remainder open. Run phase 1 (reserved slices) and then phase 2 (open) with a **lazy greedy**:

```
heap of (-gain, musicbrainz_id, album) using gain at push time
while capacity and heap:
    pop top; recompute gain with current counters
    if recomputed gain < next top's stored gain: push back with new gain; continue
    take it: record Pick, bump artist and broad-only counters, remove from other slices
```

Live albums are only eligible for the live slice. The connector slice takes albums with non-empty `connects_to`, and the deep slice takes `is_deep_cut` albums. Phase 1 capacity left unfilled moves into that scene's open slice. After phase 2, the unfilled budget of scenes with no candidates left is recorded in `shortfalls` and re-split by `scene_budgets(config, leftover, scenes_with_candidates)`. Phase 2 then repeats until nothing is left over or no scene has candidates. Gain is defined in the Design section.

- [ ] **Step 1: Write the failing tests.** Build pool albums with `to_pool_album` from synthetic records and use small settings. Set `connector_share = deep_cut_share = live_share = 0` except where a test is about that slice.
  - `test_scene_budgets_largest_remainder`: shares a=2, b=1, target 10 → `{"a": 7, "b": 3}` (6.67 rounds to 7 by remainder)
  - `test_select_never_picks_catalog_albums`: a pool album whose MBID is in the catalog list is never picked
  - `test_artist_decay_is_soft`: `artist_free_albums=3`, `artist_decay=0.5`. Artist X has 5 albums at evidence 4.0 and artist Y has 3 at 3.0, target 4 in one scene. Picks are 3 by X, then Y (X's 4th gain is 2.0 < 3.0). With 3 X albums already in the catalog, the first pick is Y.
  - `test_albums_without_artist_are_not_decayed`: 5 artistless albums at evidence 2.0 and 1 by artist Z at 1.5, target 5 → all 5 artistless are picked
  - `test_broad_only_rewards_diminish`: `broad_only_halfway=1`. A scene has 3 broad-only albums (`rock` votes 15 → 0.3·log2(16) = 1.2) and one specific album at evidence 1.0, target 2. Picks are one broad-only, then the specific album (the second broad-only gain is 0.6).
  - `test_deprioritized_top_term_is_penalized`: an album whose top term is `indie rock` loses to a lower-evidence album
  - `test_live_albums_only_fill_the_live_slice`: `live_share=0.2`, target 10, 20 live and 20 studio candidates → exactly 2 live picks
  - `test_connector_slice_reserved`: `connector_share=0.5`, target 4. 2 connectors at low evidence and 10 non-connectors at high evidence → both connectors picked, with `slice == "connector"`.
  - `test_unused_reserved_slice_goes_to_open`: `connector_share=0.5`, no connectors, target 4 → 4 open picks
  - `test_shortfall_moves_to_scenes_with_candidates` (a two-scene config): shares a=7, b=3, target 10, a has 2 candidates and b has 20 → 10 picks, `shortfalls == {"a": 5}`, and b gets 8
  - `test_exhausted_pool_returns_fewer_than_target`: target 100, 12 candidates → 12 picks
  - `test_selection_is_deterministic`: same inputs twice gives identical `picks`, and equal-gain ties come out in MBID order

- [ ] **Step 2: Run** `uv run pytest tests/test_batch_select.py -v`. Expected: FAIL.

- [ ] **Step 3: Implement `select_batch`** and the helpers `_gain(album, scene_id, counters, settings) -> float` and `_artist_factor(k, settings) -> float`.

- [ ] **Step 4: Run.** Expected: PASS.

- [ ] **Step 5: Commit** `feat: select catalog batches by scene with diminishing returns and reserved slices`

---

### Task 6: `select_catalog_batch` script

**Files:**
- Create: `backend/src/crate_backend/scripts/select_catalog_batch.py`
- Test: `backend/tests/test_select_catalog_batch_script.py`

**Interfaces:**
- Consumes: `read_pool`, `load_catalog_albums`, `select_batch`, `load_scene_config`
- Produces:
  - `async select(name: str, target: int, *, force: bool) -> Path`, which writes `catalog/batches/<name>.jsonl` and `<name>.md` and returns the JSONL path
  - JSONL line keys: `musicbrainz_id, title, artist_name, year, scene, slice, gain, live`
  - `read_batch_ids(path: Path) -> list[str]`, used by Task 7

The summary `.md` covers: the target and actual pick count; per scene the budget, picks by slice and shortfall; the 10 artists with the most picks; picks per decade; and the `scenes.toml` git hash (`git rev-parse HEAD:catalog/scenes.toml`, or "uncommitted" if that fails).

- [ ] **Step 1: Write the failing tests.** Monkeypatch `read_pool`, `load_catalog_albums` and the session factory as in `test_ingest_musicbrainz_script.py`, and point `catalog_dir` at `tmp_path`.
  - `test_select_writes_batch_and_summary`: the JSONL has `target` lines with exactly the listed keys, and the summary contains every scene id
  - `test_select_refuses_to_overwrite_without_force`: the second call raises `SystemExit`, and `force=True` overwrites
  - `test_read_batch_ids_round_trip`

- [ ] **Step 2: Run.** Expected: FAIL.
- [ ] **Step 3: Implement.** CLI: `uv run python -m crate_backend.scripts.select_catalog_batch --name batch-1 --target 25000 [--force]`. Print the summary.
- [ ] **Step 4: Run.** Expected: PASS.
- [ ] **Step 5: Commit** `feat: write a catalog batch file and summary from the scene pool`

---

### Task 7: Ingest a batch without touching existing albums

**Files:**
- Modify: `backend/src/crate_backend/scripts/ingest_musicbrainz.py`
- Test: `backend/tests/test_ingest_musicbrainz_script.py`

**Interfaces:**
- Consumes: `read_batch_ids` (Task 6), `POOL_FIELDS`/pool gzip format (Task 3), `to_candidate`, `artist_ids_in_credits`, `resolve_artists`, `upsert_album`, `upsert_artist_relationships`
- Produces: `async ingest_batch(batch_path: Path, pool_path: Path, artist_archive: Path) -> None` and a CLI flag `--batch PATH`. With `--batch`, `ingest_batch` replaces `ingest_dumps`, and the cover-art stage still runs unless `--skip-cover-art` is given.

Behaviour:
1. Read the batch IDs and drop any already in `albums.musicbrainz_release_group_id`.
2. Scan the pool file's raw records for the remaining IDs and build `to_candidate` from each.
3. Resolve only the artists credited on these candidates (a single artist-dump pass).
4. Upsert in one transaction with progress every 1,000.
5. Print the counts: in the batch, already in the catalog, missing from the pool and ingested.

Artist relationship upserts keep the current behaviour (`upsert_artist_relationships` is already idempotent).

- [ ] **Step 1: Write the failing tests:**
  - `test_ingest_batch_skips_existing_and_is_rerunnable`: the pool (written with `write_pool` to `tmp_path`) holds `test-rg-1` and `test-rg-2`. The database already has an `Album` with `musicbrainz_release_group_id="test-rg-1"` and `title="Kept Title"`. After `ingest_batch`, that title is still `"Kept Title"` and `test-rg-2` exists with its tag. A second run leaves the `Album` count for those two IDs at 2.
  - `test_ingest_batch_reports_ids_missing_from_pool`: a batch ID not in the pool prints `missing from pool: 1` (capsys)

- [ ] **Step 2: Run.** Expected: FAIL.
- [ ] **Step 3: Implement.** Add `--batch` to `main()` and update the module docstring's `Run with:` line.
- [ ] **Step 4: Run** `uv run pytest tests/test_ingest_musicbrainz_script.py -v`. Expected: PASS (including the existing tests).
- [ ] **Step 5: Commit** `feat: ingest a catalog batch, skipping albums already in the catalog`

---

### Task 8: Coverage report

**Files:**
- Create: `backend/src/crate_backend/scenes/coverage.py`, `backend/src/crate_backend/scripts/catalog_coverage.py`
- Test: `backend/tests/test_catalog_coverage.py`

**Interfaces:**
- Consumes: `CatalogAlbum`, `PoolAlbum`, `read_batch_ids`, `SceneConfig`, `popularity_quartile`
- Produces:
  - `ENTRY_POINT_DEPTH = 100`
  - `@dataclass(frozen=True) SceneCoverage(scene: str, albums: int, live: int, by_batch: dict[str, int], artists: int, max_per_artist: int, entry_point_coverage: float, deep_cuts: int, with_text: float, quartiles: dict[str, int])`. In `by_batch`, the key `"original"` means not in any batch file.
  - `@dataclass(frozen=True) EdgeCoverage(path: str, a: str, b: str, connectors: int)`, counting catalog albums with home a connecting to b, plus home b connecting to a
  - `scene_coverage(catalog, pool_top: dict[str, set[str]], live_ids: set[str], batches: dict[str, set[str]], config) -> list[SceneCoverage]`
  - `edge_coverage(catalog, config) -> list[EdgeCoverage]`
  - `render_coverage(scenes, edges, *, total: int, in_no_scene: int, label: str) -> str`
  - Script: `async write_coverage(label: str) -> Path` writes `catalog/reports/coverage-<date>-<label>.md`. `pool_top` holds each scene's top `ENTRY_POINT_DEPTH` pool MBIDs by evidence, counting catalog albums too.

- [ ] **Step 1: Write the failing tests:**
  - `test_entry_point_coverage_is_share_of_top_pool_albums_in_catalog`: pool top for `d` = 4 IDs, 3 in the catalog → 0.75
  - `test_edge_coverage_counts_both_directions`: one album home a → b and one home b → a gives `connectors == 2` on the a–b edge
  - `test_by_batch_marks_original_albums`
  - `test_render_lists_every_scene_and_edge`

- [ ] **Step 2: Run.** Expected: FAIL.
- [ ] **Step 3: Implement.** CLI: `uv run python -m crate_backend.scripts.catalog_coverage --label baseline-25k`.
- [ ] **Step 4: Run.** Expected: PASS.
- [ ] **Step 5: Commit** `feat: report catalog coverage by scene and path edge`

---

### Task 9: Scene answer key and path-reach report

**Files:**
- Modify: `backend/src/crate_backend/evaluation/seeds.py` (add an `add` subcommand)
- Create: `backend/src/crate_backend/evaluation/path_reach.py`
- Modify: `.gitignore` (add `/eval/scenes/pool.jsonl`, `/eval/scenes/judgments.jsonl`, `/backups/` and `/models/archive/`)
- Test: `backend/tests/test_eval_seeds.py`, `backend/tests/test_path_reach.py`

**Interfaces:**
- Consumes: `search_candidates`, `is_eligible`, `seed_from`, `load_seeds`/`save_seeds`, `run_variants`, `parse_variant_names`, `load_catalog_albums`, `SceneConfig`
- Produces:
  - `choose_and_add(seeds: list[Seed], matches: list[SeedCandidate], *, read_line, write) -> list[Seed] | None`, modelled on `choose_and_swap`. CLI: `seeds add "title words" [--artist NAME]`, creating `seeds.json` in `eval_dir()` when it doesn't exist. The scene key is used with `CRATE_EVAL_DIR=../eval/scenes`, so the existing `pool`, `grade` and `score` commands work unchanged.
  - `REACH_K = 10`
  - `pick_path_seeds(catalog: list[CatalogAlbum], config, per_scene: int) -> dict[str, list[uuid.UUID]]` takes the top `per_scene` catalog albums by home-scene evidence for every scene on a path, ties by album id, with at most one seed per artist per scene
  - `@dataclass(frozen=True) ReachRow(variant: str, scene: str, same_scene: float, neighbor_scene: float, no_scene: float, artists: float)`, all means over that scene's seeds of the share of the top `REACH_K`, except `artists`, which is the mean distinct artists
  - `reach_rows(runs: dict[str, dict[uuid.UUID, list[uuid.UUID]]], seed_scenes: dict[uuid.UUID, str], catalog_index: dict[uuid.UUID, CatalogAlbum], config) -> list[ReachRow]`
  - `render_reach(rows, *, label: str) -> str`
  - CLI: `uv run python -m crate_backend.evaluation.path_reach --label baseline-25k [--variants ...] [--per-scene 10] [--refresh-seeds]`. Seeds are frozen in `eval/path-reach-seeds.json` on the first run and reused afterwards unless `--refresh-seeds` is given. The CLI writes `eval/results/path-reach-<date>-<label>.md`.

- [ ] **Step 1: Write the failing tests:**
  - `test_choose_and_add_appends_choice` and `test_choose_and_add_hides_existing_seeds` (same style as the existing swap tests)
  - `test_pick_path_seeds_one_per_artist_and_highest_evidence_first`
  - `test_reach_rows_shares`: one seed in `d` whose top-4 run holds 2 albums in d, 1 in a neighbor and 1 in no scene → `same_scene == 0.5`, `neighbor_scene == 0.25`, `no_scene == 0.25`
  - `test_frozen_seeds_are_reused`: a second CLI-level call with no `--refresh-seeds` reads the existing file (patch `pick_path_seeds` to raise)

- [ ] **Step 2: Run.** Expected: FAIL.
- [ ] **Step 3: Implement.** The report header says plainly: "Scene membership comes from tags, so tag-based variants are favoured; read this as coverage, not quality."
- [ ] **Step 4: Run** `uv run pytest tests/test_eval_seeds.py tests/test_path_reach.py -v`. Expected: PASS.
- [ ] **Step 5: Commit** `feat: add a scene answer key command and a path-reach report`

---

### Task 10: Profile the dump, tune scenes and record the 25k baseline (operational)

No new code. Each step is a command with a result to check. **Two owner checkpoints are marked with ⏸.**

- [ ] **Step 1: Check disk.** Run `df -h ~`. You need at least 12 GB free (the two dumps, a pool file of about 150 MB, a database backup, and models about four times their current size). On 2026-10-21 there was 15 GB free. If there is less, stop and tell the owner.
- [ ] **Step 2: Download** `release-group.tar.xz` and `artist.tar.xz` from the folder named by `https://data.metabrainz.org/pub/musicbrainz/data/json-dumps/LATEST` into `MusicBrainz/`. Run `uv run python -c "from crate_backend.musicbrainz.dump_reader import read_dump_metadata as r; from pathlib import Path; print(r(Path('../MusicBrainz/release-group.tar.xz')))"` and confirm it prints a TIMESTAMP.
- [ ] **Step 3: Profile.** Run `uv run python -m crate_backend.scripts.profile_catalog_pool`. Expected: `catalog/reports/profile-<date>.md` and `MusicBrainz/scene-pool.jsonl.gz`. The funnel's first lines should be close to the 2026-10-19 count (about 4.5M release groups and 1.73M after the type filter).
- [ ] **Step 4: ⏸ Owner review of the profile.** Show the owner the Scenes table, the top `unassigned` terms and the deep-cut and connector counts. Ask them to confirm: scene term lists (add the real MusicBrainz spellings the Terms table reveals), shares (scenes whose pool is smaller than their batch-1 budget will run short), junk tags to add to `nondescriptive_terms`, and whether the total in-scene pool can reach +75k at all. Edit `scenes.toml` and re-run with `--from-pool` until the owner is satisfied. Commit `scenes.toml` and the final profile report: `chore: tune catalog scenes from the dump profile`.
- [ ] **Step 5: Baseline coverage.** Run `uv run python -m crate_backend.scripts.catalog_coverage --label baseline-25k`. Commit the report.
- [ ] **Step 6: Baseline path reach.** Run `uv run python -m crate_backend.evaluation.path_reach --label baseline-25k --variants overlap,tfidf-tags,tfidf-tags+text,embed-tags,embed-tags+text`. Commit `eval/path-reach-seeds.json` and the report.
- [ ] **Step 7: ⏸ Scene key seeds.** Ask the owner to pick about 8 albums they know well from the center scenes and the path endpoints, which must already be in the 25k. Show them the top catalog albums per center scene from the coverage report to choose from. Add each with `CRATE_EVAL_DIR=../eval/scenes uv run python -m crate_backend.evaluation.seeds add "title words" --artist NAME`.
- [ ] **Step 8: Grade the scene key on the 25k.** Run `CRATE_EVAL_DIR=../eval/scenes uv run python -m crate_backend.evaluation.pool --variants overlap,tfidf-tags,embed-tags`, then `... evaluation.grade` (the owner grades), then `... evaluation.score --variants overlap,tfidf-tags,embed-tags`. Commit `eval/scenes/seeds.json` and `eval/scenes/results/<date>.md`.
- [ ] **Step 9: Archive the 25k models.** Run `mkdir -p ../models/archive/25k && cp ../models/*.joblib ../models/archive/25k/`. Task 9 gitignores this folder.

---

### Task 11: Batch 1 (+15,000), rebuild and compare (operational)

- [ ] **Step 1: Back up the database.** Run `mkdir -p ../backups && docker compose exec -T db pg_dump -U crate -Fc crate > ../backups/pre-batch-1.dump`. Check that the file is over 10 MB.
- [ ] **Step 2: Select.** Run `uv run python -m crate_backend.scripts.select_catalog_batch --name batch-1 --target 15000` (checkpoint decision; originally 25000). Read the summary, and spot-check 20 random lines from three scenes (one center, one roots, one wider) for obvious misfits. Commit `catalog/batches/batch-1.*`.
- [ ] **Step 3: Ingest.** Run `uv run python -m crate_backend.scripts.ingest_musicbrainz --batch ../catalog/batches/batch-1.jsonl --skip-cover-art`. Expected: "already in catalog: 0" and an ingested count equal to the batch size minus "missing from pool".
- [ ] **Step 4: Links and text.** Run `uv run python -m crate_backend.scripts.link_wikidata`, then `uv run python -m crate_backend.scripts.backfill_wikipedia_text`. The link pass re-reads links for the existing 25k from the newer dump, which is expected. Articles whose links changed are fetched again.
- [ ] **Step 5: Slow backfills.** These take about 7 hours each at 1 request a second. They can run in background terminals at the same time as each other and as Step 6:
  - `uv run python -m crate_backend.scripts.ingest_musicbrainz --cover-art-only`
  - `uv run python -m crate_backend.scripts.backfill_lastfm_popularity`

  Popularity percentiles are recomputed over the bigger catalog, so existing albums' percentiles shift. The seeds' quartiles stay as stored in `seeds.json`.
- [ ] **Step 6: Rebuild all four models** (after Step 4):
  - `uv run python -m crate_backend.scripts.build_tfidf_model`
  - `uv run --group phrases python -m crate_backend.scripts.build_tfidf_model --sound-phrases`
  - `uv run --group embeddings python -m crate_backend.scripts.build_embedding_model --device mps`
  - `uv run --group embeddings python -m crate_backend.scripts.build_embedding_model --sound-filter --out ../models/embed-tags+sound.joblib --device mps`

  Each build prints the album count, which should equal the new catalog size.
- [ ] **Step 7: Restart the API.** Stop and start `make backend`. `--reload` does not reload model files.
- [ ] **Step 8: Measure** (after Step 5 finishes, so popularity is current):
  - `catalog_coverage --label after-batch-1`
  - `path_reach --label after-batch-1 --variants overlap,tfidf-tags,tfidf-tags+text,embed-tags,embed-tags+text`, which reuses the frozen seeds
  - Old key: `evaluation.pool`, then `evaluation.grade` (owner), then `evaluation.score`
  - Scene key: the same three commands with `CRATE_EVAL_DIR=../eval/scenes` and `--variants overlap,tfidf-tags,embed-tags`
- [ ] **Step 9: Write the comparison.** Create `docs/method-reports/catalog-expansion.md` with before/after tables. Show per scene the albums, entry-point coverage, connectors per path edge and the share with text. Show path reach per variant. Show NDCG@5 and Recall@5 for both keys, overall and by quartile, with per-seed wins and losses against baseline. Say plainly where it got worse. Note that 10 and 8 seeds only separate large differences. Commit.
- [ ] **Step 10: ⏸ Owner decision.** Present the comparison. Batch 2 goes ahead as planned if old-key NDCG@5 for every core variant is within 0.05 of baseline, the scene key improves for the best variant, and path reach rises on most edges. Otherwise, agree on `scenes.toml` changes first (shares, terms, decay constants) and record them in the method report. The owner can also roll back with `pg_restore -c` from `backups/pre-batch-1.dump` and the archived models.

---

### Task 12: Batch 2 (everything left), rebuild and compare (operational)

- [ ] **Step 1:** Proceed only after the Task 11 ⏸ decision, and with any `scenes.toml` changes committed. Archive the batch-1 models: `mkdir -p ../models/archive/batch-1 && cp ../models/*.joblib ../models/archive/batch-1/`.
- [ ] **Step 2:** Repeat Task 11 Steps 1–9 with `pre-batch-2.dump`, `--name batch-2 --target 100000` (takes every remaining in-scene album) and labels `after-batch-2`. Expect about 14 hours for each slow backfill. Add the after-batch-2 columns to the method report.
- [ ] **Step 3: ⏸** Present the results. A third batch, tag normalization along the paths, or stopping are the owner's call. None of these is part of this plan.

---

## Known limits (stated up front)

- **The scene pool may not reach +75k.** Thinly tagged center scenes such as picopop and Shibuya-kei probably have only hundreds of tagged MusicBrainz albums. Task 10 measures this before anything is ingested, and the plan takes fewer albums rather than padding.
- **Model files grow about 4×** (tfidf ≈ 350 MB, each embedding file ≈ 300 MB at 100k). The API holds every loaded file per worker, so watch memory on the laptop. The memory notes from 2026-10-19 show the machine already swapping.
- **Overlap is computed live in Postgres.** At 100k albums it may be slower per request. Measure it in Task 11 Step 8 by timing one `try_recs` call. Don't optimize it in this plan.
- **Popularity quartiles shift** as less-famous albums arrive, so "median pop." in reports isn't comparable across batches. Seed quartiles are frozen in the seed files.

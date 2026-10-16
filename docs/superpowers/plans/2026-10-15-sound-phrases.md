# Sound-Phrase Recommender Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `phrases` recommendation approach: TF-IDF over tags plus only the sound-describing phrases spaCy extracts from each album's Wikipedia article, selectable in the frontend.

**Architecture:**
- **Build:** a new pure module, `recommend/sound_phrases.py`, extracts phrases from spaCy-parsed text. `build_tfidf_model --sound-phrases` feeds those phrases into the existing `TfidfModel` in place of article words (a new `_phrase_block`) and writes a separate file, `models/tfidf-phrases.joblib`.
- **Serving:** the API loads that file for `approach: "phrases"` and ranks it through the unchanged TF-IDF `recommend()`. The frontend adds a picker entry and a "Sounds alike" label.

**Tech Stack:** Python 3.12, spaCy 3.8.7 + `en_core_web_sm` 3.8.0, scikit-learn `TfidfVectorizer`, FastAPI, pytest, Next.js/React (TypeScript), uv, ruff, oxlint.

**Spec:** `docs/superpowers/specs/2026-10-15-sound-phrases-design.md`

## Global Constraints

- **Dependencies:** pin `spacy==3.8.7` and `en_core_web_sm` 3.8.0 from `https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl`, in a `phrases` dependency group that `dev` includes.
- **Imports:** the API never imports spaCy. Only `scripts/build_tfidf_model.py` imports it, inside the `--sound-phrases` code path.
- **Prose only:** credit lines are removed before parsing.
- **Model file:** the phrase model is an ordinary `TfidfModel`, written to `settings.tfidf_phrases_model_path` (default `<repo>/models/tfidf-phrases.joblib`). `tfidf.joblib` is never overwritten by a phrase build.
- **Vectorizer settings:** phrase block `min_df=2`, `max_df=0.5` (the `build_model` defaults); α default 0.6.
- **API:**
  - approaches are `"overlap"`, `"tfidf"`, `"phrases"`, `"embeddings"`, with the default still `"overlap"`;
  - the missing-model 503 detail is exactly `"Sound-phrase model not built"`;
  - the response schema doesn't change.
- **Frontend:**
  - picker label exactly `TF-IDF (tags + sound phrases)`;
  - explanation label `Sounds alike:` for phrases results, `Described alike:` otherwise;
  - the error message for an unbuilt model is unchanged.
- **Workflow and style:**
  - work directly on `main` (owner preference); commit per task; never push;
  - end every commit message with:
    ```
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8
    ```
  - backend commands run from `backend/`;
  - ruff line length 100, and `ruff format` must leave changed files unchanged.

## Review Focus

1. **Seed album with no phrases** (article all credits, or no article): the phrases approach must still recommend on tags alone instead of returning nothing. *Pinned in Task 2 (`test_albums_without_phrases_score_on_tags_alone`, seed side) and Task 4 (`test_phrases_seed_without_phrases_still_ranks_on_tags`).*
2. **Only one of the two TF-IDF files built:** `phrases` must work when `tfidf.joblib` is missing and vice versa; each approach uses its own loader. *Pinned in Task 4 (`test_phrases_uses_its_own_model_not_the_tfidf_one`, and `test_loaders_keep_their_own_files`).*
3. **Results shown after switching the picker:** the "Sounds alike" / "Described alike" label must follow the approach that *produced* the shown results (`groupRecs.approach`), not the picker's current value. *Pinned in Task 5's manual check, step 4.*
4. **`phrases` list misaligned with `docs`:** a caller bug must fail loudly, not silently shift phrases onto the wrong albums. *Pinned in Task 2 (`test_misaligned_phrases_are_rejected`).*
5. **No album has any phrase** (empty catalog, or extraction finds nothing): the build must produce a valid tags-only model, not crash inside scikit-learn. *Pinned in Task 2 (`test_no_phrases_at_all_gives_a_tags_only_model`).*

## File Structure

| File | Change | Responsibility |
|---|---|---|
| `backend/pyproject.toml`, `backend/uv.lock` | Modify | `phrases` dependency group; `dev` includes it |
| `backend/src/crate_backend/recommend/sound_phrases.py` | Create | Pure extraction rules over spaCy docs |
| `backend/tests/test_sound_phrases.py` | Create | Rule tests with the real parser |
| `backend/src/crate_backend/recommend/tfidf.py` | Modify | `phrases=` parameter, `_phrase_block`, metadata |
| `backend/tests/test_recommend_tfidf.py` | Modify | Phrase block tests |
| `backend/src/crate_backend/core/config.py` | Modify | `tfidf_phrases_model_path` setting |
| `backend/src/crate_backend/scripts/build_tfidf_model.py` | Modify | `--sound-phrases` flag, spaCy loading, summary |
| `backend/tests/test_build_tfidf_model_script.py` | Modify | Flag parsing and invalid combinations |
| `backend/src/crate_backend/recommend/model_store.py` | Modify | `get_tfidf_phrases_model()` |
| `backend/tests/test_tfidf_model_store.py` | Modify | Phrase loader tests |
| `backend/src/crate_backend/api/routes/recommendations.py` | Modify | `phrases` approach |
| `backend/tests/test_recommendations_api.py` | Modify | `phrases` API tests |
| `frontend/app/page.tsx` | Modify | Picker entry, "Sounds alike" label |
| `docs/method-reports/sound-phrases.md` | Modify | Status: built |

---

### Task 1: Dependency group and extraction module

**Files:**
- Modify: `backend/pyproject.toml` (the `[dependency-groups]` table)
- Modify: `backend/uv.lock` (regenerated by `uv lock`)
- Create: `backend/src/crate_backend/recommend/sound_phrases.py`
- Test: `backend/tests/test_sound_phrases.py`

**Interfaces:**
- Consumes: `normalize_term(name: str) -> str` and the regex `_CREDIT_LINE` from `crate_backend.recommend.text_cleaning`.
- Produces:
  - `prose_only(text: str) -> str`
  - `extract(doc, known_terms: frozenset[str] = frozenset()) -> list[str]`
  - `extract_all(texts: Iterable[str], nlp, known_terms: frozenset[str] = frozenset(), batch_size: int = 32) -> list[list[str]]`
  - constant `SPACY_MODEL = "en_core_web_sm"`

- [ ] **Step 1: Add the `phrases` dependency group**

In `backend/pyproject.toml`, replace the `[dependency-groups]` table's `dev` entry and add `phrases` after `embeddings`:

```toml
[dependency-groups]
dev = [
    "pytest>=9.1.1",
    "pytest-asyncio>=1.4.0",
    "ruff>=0.16.7",
    # The sound-phrase tests run the real parser, so dev always has it.
    { include-group = "phrases" },
]
# Only the embedding build script needs these (torch is a large download);
# the API and the tests never import them.
embeddings = [
    "sentence-transformers>=3.0.0",
]
# The sound-phrase build (build_tfidf_model --sound-phrases) parses articles
# with spaCy. Pinned to the versions the extraction rules were tuned on,
# because parses (and so the rule tests) change between model versions.
phrases = [
    "spacy==3.8.7",
    "en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl",
]
```

Run: `uv lock && uv sync`
Expected: both succeed; `uv run python -c "import spacy; spacy.load('en_core_web_sm'); print(spacy.__version__)"` prints `3.8.7`.

- [ ] **Step 2: Write the failing tests**

Create `backend/tests/test_sound_phrases.py`:

```python
import pytest
import spacy

from crate_backend.recommend.sound_phrases import (
    SPACY_MODEL,
    extract,
    extract_all,
    prose_only,
)

# Expected outputs were checked against spacy 3.8.7 + en_core_web_sm 3.8.0.
# A parser upgrade that changes them should fail here, not drift silently.
KNOWN = frozenset({"acid jazz", "hip hop", "heavy metal", "new wave"})


@pytest.fixture(scope="module")
def nlp():
    return spacy.load(SPACY_MODEL)


@pytest.fixture
def phrases(nlp):
    return lambda text, known=KNOWN: extract(nlp(text), known)


def test_modifiers_of_music_nouns_and_their_conjuncts(phrases):
    assert phrases("The album pairs jangly guitars and breathy vocals.") == [
        "jangly guitars",
        "breathy vocals",
    ]


def test_a_generic_noun_keeps_only_its_descriptor(phrases):
    assert phrases("They are an industrial band from Vancouver.") == ["industrial"]


def test_adjectives_after_a_linking_verb(phrases):
    assert phrases("The sound is warm and spacious.") == ["warm sound", "spacious sound"]


def test_labels_after_a_describing_verb(phrases):
    assert phrases("Critics called the album ferocious.") == ["ferocious"]
    assert phrases("Reviewers described it as brash and raw.") == ["brash", "raw"]


def test_hyphenated_words_are_rebuilt_and_normalized_like_tags(phrases):
    assert phrases("It has a lo-fi production.") == ["lo fi production"]


def test_adjacent_descriptors_join_only_into_known_terms(phrases):
    assert phrases("It is an acid jazz record.") == ["acid jazz"]
    assert phrases("It is a hip hop album.") == ["hip hop"]
    assert phrases("A hip hop group from Atlanta.") == ["hip hop"]
    assert phrases("A loud punk band.") == ["loud", "punk"]


def test_a_known_join_may_use_an_ignored_word(phrases):
    assert phrases("A new wave band.") == ["new wave"]
    assert phrases("A new band.") == []


def test_without_known_terms_nothing_is_joined(phrases):
    assert phrases("It is an acid jazz record.", frozenset()) == ["acid", "jazz"]


def test_negated_nouns_give_nothing(phrases):
    assert phrases("There is no ska on the record.") == []
    assert phrases("The album lacks melodic guitars.") == []
    assert phrases("It was recorded without distorted guitars.") == []


def test_names_places_ordinals_and_ignored_words_give_nothing(phrases):
    assert phrases("It was the second album by the Canadian band.") == []
    assert phrases("It opens with the best-selling opening track.") == []
    assert phrases("His solo album.") == []


def test_only_an_adverb_right_before_the_noun_is_a_descriptor(phrases):
    assert phrases("It features jangly guitars.") == ["jangly guitars"]
    assert phrases("Crunchy guitars. Crunchy guitars again.") == ["crunchy guitars"]


def test_guitar_solo_is_a_specific_phrase(phrases):
    assert phrases("The guitar solo is long.") == ["guitar solo"]


def test_prose_only_removes_credit_lines():
    text = "Thundercat – bass (tracks 2, 10)\nThe album has a chunky groove."

    assert prose_only(text) == "The album has a chunky groove."


def test_a_long_line_with_a_dash_is_prose_not_a_credit():
    line = "The band – " + "very " * 40 + "loud"

    assert prose_only(line) == line


def test_extract_all_keeps_one_list_per_text_including_empty_ones(nlp):
    texts = ["The record has a funk groove.", "", "Elvin Jones – drums"]

    assert extract_all([prose_only(t) for t in texts], nlp, KNOWN) == [["funk groove"], [], []]
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `uv run pytest tests/test_sound_phrases.py -q`
Expected: collection error, `ModuleNotFoundError: No module named 'crate_backend.recommend.sound_phrases'`.

- [ ] **Step 4: Write the module**

Create `backend/src/crate_backend/recommend/sound_phrases.py`:

```python
"""Extract the phrases of an album article that describe how it sounds, for
the sound-phrase recommender (`approach: "phrases"`).

Most stored article text is release history, charts and biography. This
keeps only descriptors attached to music nouns ("crunchy guitars",
"warm sound", "industrial" from "industrial band"), using spaCy's parse.
These functions take parsed docs; only the build script imports spaCy.

Design: docs/superpowers/specs/2026-10-15-sound-phrases-design.md
"""

import re
from collections.abc import Iterable
from typing import Any

from crate_backend.recommend.text_cleaning import _CREDIT_LINE, normalize_term

SPACY_MODEL = "en_core_web_sm"

# Nouns whose descriptor is kept with the noun: "crunchy guitars".
SPECIFIC_NOUNS = frozenset(
    {
        "sound", "soundscape", "guitar", "guitarwork", "vocal", "voice", "singing", "drum",
        "drumming", "percussion", "bass", "bassline", "beat", "riff", "production", "groove",
        "melody", "harmony", "synth", "synthesizer", "synthesiser", "keyboard", "piano", "organ",
        "string", "horn", "saxophone", "sax", "rhythm", "tempo", "texture", "atmosphere", "mood",
        "tone", "arrangement", "instrumentation", "lyric", "chorus", "hook", "sample", "feel",
        "timbre", "noise", "distortion", "reverb", "ballad", "solo",
    }
)  # fmt: skip
# Nouns that add nothing themselves, so only the descriptor is kept:
# "industrial" from "industrial band", "ferocious" from "a ferocious album".
GENERIC_NOUNS = frozenset(
    {
        "song", "track", "album", "record", "music", "style", "band", "group", "duo", "trio",
        "musician", "singer", "rapper", "artist", "ensemble", "act",
    }
)  # fmt: skip
# A subject's adjective after these describes it: "the sound is warm".
LINKING_VERBS = frozenset({"be", "sound", "feel", "seem", "become", "remain", "appear"})
# An object's label after these describes it: "called the album ferocious".
DESCRIBING_VERBS = frozenset(
    {"call", "describe", "label", "deem", "consider", "dub", "characterize", "characterise", "term"}
)
# Heads that negate their noun without a grammatical "not": "lacks melody",
# "without distorted guitars".
NEGATING_HEADS = frozenset({"lack", "without"})
# Descriptors about release order, sales, rank or opinion rather than sound.
# Tuned on the 300-album sample (eval/text-relevance/, 2026-10-15).
IGNORED_WORDS = frozenset(
    {
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
        "tenth", "debut", "new", "previous", "same", "other", "next", "last", "final", "only",
        "own", "many", "several", "various", "more", "most", "such", "entire", "whole",
        "original", "commercial", "critical", "best", "greatest", "good", "great", "successful",
        "unsuccessful", "popular", "major", "early", "late", "later", "latest", "recent",
        "upcoming", "official", "single", "double", "full", "extended", "studio", "bonus",
        "title", "lead", "hit", "unreleased", "additional", "different", "certain", "main",
        "particular", "individual", "few", "much", "big", "live", "compilation", "cover",
        "separate", "standard", "similar", "specific", "overall", "total", "famous", "classic",
        "selling", "charting", "released", "top", "favorite", "favourite", "mediocre", "follow",
        "following", "forthcoming", "remastered", "available", "hidden", "lost", "remaining",
        "finished", "written", "produced", "mixed", "recorded", "uncredited", "notable",
        "renowned", "real", "basic", "complete", "closest", "highest", "better", "worse", "bad",
        "excellent", "fine", "finest", "enjoyable", "impressive", "wonderful", "difficult",
        "accomplished", "anticipated", "acclaimed", "shortest", "longest", "general", "present",
        "extra", "long", "strong", "personal", "deluxe", "expanded", "limited", "guest",
        "sophomore", "eponymous", "titled", "named", "fellow", "former", "founding", "longtime",
        "current", "star", "young", "independent", "underground", "mainstream", "award",
        "winning", "nominated", "influential", "important", "significant", "ambitious",
        "reissued", "rerecorded", "included", "featured", "listed", "rated", "ranked", "opening",
        "closing", "earlier", "subsequent", "latter", "breakthrough", "signature", "executive",
        "vinyl", "concept", "biggest", "strongest", "able", "unable", "potential", "future",
        "support", "milestone", "affair", "also", "just", "even", "mostly", "largely", "mainly",
        "almost", "nearly", "very", "too", "solo", "backing", "musical", "music", "recording",
        "record", "consecutive", "numerous", "album",
    }
)  # fmt: skip
# spaCy entity types that name things rather than describe sound.
DROPPED_ENTITIES = frozenset(
    {
        "NORP", "GPE", "LOC", "ORG", "PERSON", "DATE", "TIME", "ORDINAL", "CARDINAL", "MONEY",
        "PERCENT", "QUANTITY", "WORK_OF_ART", "EVENT", "FAC", "PRODUCT", "LANGUAGE",
    }
)  # fmt: skip
# A "Name – roles" line longer than this is prose with a dash in it.
MAX_CREDIT_LINE_CHARS = 160
_WORD = re.compile(r"[a-z][a-z-]*[a-z]")


def prose_only(text: str) -> str:
    """`text` without credit lines ("Elvin Jones – drums")."""
    return "\n".join(
        line
        for line in text.splitlines()
        if not (len(line) <= MAX_CREDIT_LINE_CHARS and _CREDIT_LINE.match(line.strip()))
    )


def extract(doc: Any, known_terms: frozenset[str] = frozenset()) -> list[str]:
    """The sound phrases of one parsed text, normalized like tags and in
    first-seen order without duplicates. Adjacent descriptors are joined
    when the joined form is in `known_terms` (the catalog's normalized
    tag terms), so "acid jazz record" gives "acid jazz" but "loud punk
    band" gives "loud" and "punk"."""
    phrases: dict[str, None] = {}
    for token in doc:
        anchor = _anchor(token)
        if anchor is None or _negated(token):
            continue
        for text in _join_known(_descriptors(token, anchor), known_terms):
            phrase = text if anchor in GENERIC_NOUNS else f"{text} {token.text.lower()}"
            phrases[normalize_term(phrase)] = None
    return list(phrases)


def extract_all(
    texts: Iterable[str], nlp: Any, known_terms: frozenset[str] = frozenset(), batch_size: int = 32
) -> list[list[str]]:
    """One phrase list per text, in order, parsing in batches."""
    return [extract(doc, known_terms) for doc in nlp.pipe(texts, batch_size=batch_size)]


def _anchor(token: Any) -> str | None:
    lemma = token.lemma_.lower()
    if token.pos_ == "NOUN" and (lemma in SPECIFIC_NOUNS or lemma in GENERIC_NOUNS):
        return lemma
    # "described it as raw": the pronoun stands for the album.
    if token.pos_ == "PRON" and token.lower_ == "it" and token.head.lemma_ in DESCRIBING_VERBS:
        return "album"
    return None


def _negated(token: Any) -> bool:
    def has_negation(t: Any) -> bool:
        return any(c.dep_ == "neg" or (c.dep_ == "det" and c.lower_ == "no") for c in t.children)

    return has_negation(token) or has_negation(token.head) or token.head.lemma_ in NEGATING_HEADS


def _descriptors(token: Any, anchor: str) -> list[Any]:
    found = []
    for child in token.children:
        # The small model parses unfamiliar adjectives ("jangly guitars") as
        # adverbs; only one directly before the noun is a descriptor, not
        # "guitars again".
        adverb = child.dep_ == "advmod" and child.pos_ == "ADV" and child.i == token.i - 1
        if (
            child.dep_ == "amod"
            or adverb
            or (child.dep_ == "compound" and (anchor in SPECIFIC_NOUNS or child.pos_ == "NOUN"))
        ):
            found += _with_conjuncts(child)
    head = token.head
    if token.dep_ in ("nsubj", "nsubjpass") and head.lemma_ in LINKING_VERBS:
        found += [d for c in head.children if c.dep_ == "acomp" for d in _with_conjuncts(c)]
    if token.dep_ in ("dobj", "nsubjpass") and head.lemma_ in DESCRIBING_VERBS:
        for child in head.children:
            if child.dep_ in ("oprd", "acomp", "xcomp", "ccomp") and child.pos_ == "ADJ":
                found += _with_conjuncts(child)
            if child.dep_ == "prep" and child.lower_ == "as":
                for obj in child.children:
                    if obj.dep_ == "pobj":
                        found += (
                            _with_conjuncts(obj)
                            if obj.pos_ == "ADJ"
                            else [a for a in obj.children if a.dep_ == "amod"]
                        )
    return found


def _with_conjuncts(token: Any) -> list[Any]:
    """`token` and its "and"/"or" partners: "lush and spacious"."""
    found = [token]
    for child in token.children:
        if child.dep_ == "conj":
            found += _with_conjuncts(child)
    return found


def _join_known(descriptors: list[Any], known_terms: frozenset[str]) -> list[str]:
    """Descriptor texts, with runs of adjacent descriptor tokens joined where
    the run (three tokens, else two) is a known term."""
    texts = {d.i: _with_known_prefix(d, known_terms) for d in descriptors}
    # Joining may use words that are ignored on their own: "new wave".
    raw = {d.i: _descriptor_text(d, ignore=False) for d in descriptors}
    order = sorted(texts)
    out: list[str] = []
    k = 0
    while k < len(order):
        for size in (3, 2):
            run = order[k : k + size]
            if (
                len(run) == size
                and run[-1] - run[0] == size - 1
                and all(raw[i] for i in run)
                and normalize_term(" ".join(raw[i] for i in run)) in known_terms
            ):
                out.append(" ".join(raw[i] for i in run))
                k += size
                break
        else:
            if texts[order[k]]:
                out.append(texts[order[k]])
            k += 1
    return out


def _with_known_prefix(token: Any, known_terms: frozenset[str]) -> str | None:
    """The descriptor's text, joined with a compound directly before it when
    the pair is a known term: spaCy sometimes nests "hip" under "hop"."""
    text = _descriptor_text(token, ignore=False)
    for child in token.children:
        if text and child.dep_ == "compound" and child.i == token.i - 1:
            prefix = _descriptor_text(child, ignore=False)
            if prefix and normalize_term(f"{prefix} {text}") in known_terms:
                return f"{prefix} {text}"
    return _descriptor_text(token)


def _descriptor_text(token: Any, ignore: bool = True) -> str | None:
    """The descriptor as written, rebuilt across hyphens ("lo-fi"), or None
    when it isn't a sound word. `ignore=False` skips the IGNORED_WORDS check,
    for joins that form a known term."""
    if token.pos_ not in ("ADJ", "ADV", "NOUN", "VERB") or token.like_num:
        return None
    if token.ent_type_ in DROPPED_ENTITIES:
        return None
    text = _hyphenated(token)
    if _WORD.fullmatch(text) is None or len(text) < 3:
        return None
    if ignore and any(word in IGNORED_WORDS for word in text.split("-")):
        return None
    return text


def _hyphenated(token: Any) -> str:
    """'electro-industrial' from either of its word tokens: spaCy splits a
    hyphenated word written without spaces into word, '-', word."""
    doc, start, end = token.doc, token.i, token.i
    while (
        start >= 2
        and doc[start - 1].text == "-"
        and not doc[start - 2].whitespace_
        and not doc[start - 1].whitespace_
    ):
        start -= 2
    while (
        end + 2 < len(doc)
        and doc[end + 1].text == "-"
        and not doc[end].whitespace_
        and not doc[end + 1].whitespace_
    ):
        end += 2
    return doc[start : end + 1].text.lower()
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `uv run pytest tests/test_sound_phrases.py -q`
Expected: `15 passed`. If a single assertion differs, check that the installed versions are spacy 3.8.7 and en_core_web_sm 3.8.0 before touching the rules.

- [ ] **Step 6: Lint, format and run the full suite**

Run: `uv run ruff check src tests && uv run ruff format src/crate_backend/recommend/sound_phrases.py tests/test_sound_phrases.py && uv run pytest -q`
Expected: ruff clean; all tests pass (402 before this task plus 15 new).

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml uv.lock src/crate_backend/recommend/sound_phrases.py tests/test_sound_phrases.py
git commit -m "feat: extract sound-describing phrases from album articles with spaCy

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

---

### Task 2: Phrase block in the TF-IDF model

**Files:**
- Modify: `backend/src/crate_backend/recommend/tfidf.py` (`build_model` at lines 85-124; new `_phrase_block` after `_text_block`)
- Test: `backend/tests/test_recommend_tfidf.py`

**Interfaces:**
- Consumes: nothing from Task 1. Phrase lists are plain `list[list[str]]`.
- Produces:
  - `build_model(docs, *, alpha=DEFAULT_ALPHA, ngram_range=(1, 2), min_df=2, max_df=0.5, max_features=None, extra_metadata=None, phrases: list[list[str]] | None = None) -> TfidfModel`
  - When `phrases` is given:
    - `model.text_terms` are phrases;
    - `model.has_text[i]` is True when album `i` kept at least one phrase;
    - `metadata["text_source"] == "sound_phrases"` and `metadata["phrase_vectorizer"] == {"min_df": ..., "max_df": ...}`, with no `text_vectorizer` key.
  - Otherwise `metadata["text_source"] == "article"` and `text_vectorizer` is as before.

- [ ] **Step 1: Write the failing tests**

Append to `backend/tests/test_recommend_tfidf.py`:

```python
def test_phrases_are_whole_terms():
    model = model_of(
        album("A", "rock"),
        album("B", "rock"),
        phrases=[["crunchy guitars"], ["crunchy guitars", "warm sound"]],
    )

    assert sorted(model.text_terms) == ["crunchy guitars", "warm sound"]


def test_a_phrase_in_only_one_album_is_dropped_by_min_df():
    model = build_model(
        [album("A", "rock"), album("B", "rock")],
        phrases=[["crunchy guitars", "warm sound"], ["crunchy guitars"]],
        min_df=2,
        max_df=1.0,
    )

    assert list(model.text_terms) == ["crunchy guitars"]


def test_albums_without_phrases_score_on_tags_alone():
    seed = album("Seed", "jazz")
    match = album("Match", "jazz")
    for phrases in ([["warm sound"], []], [[], ["warm sound"]]):
        model = model_of(seed, match, phrases=phrases)

        [result] = recommend(model, [seed.album_id], 5)

        assert result.score == pytest.approx(1.0)
        assert result.shared_text_terms == []


def test_shared_phrases_explain_the_match():
    seed = album("Seed", "jazz")
    model = model_of(
        seed,
        album("Match", "jazz"),
        album("Other", "jazz"),
        phrases=[["warm sound", "chunky groove"], ["chunky groove"], ["warm sound"]],
    )

    results = {r.album_id: r for r in recommend(model, [seed.album_id], 5)}

    assert results[album("Match").album_id].shared_text_terms == ["chunky groove"]
    assert results[album("Other").album_id].shared_text_terms == ["warm sound"]


def test_metadata_records_the_text_source():
    docs = [album("A", "jazz", text="modal"), album("B", "jazz", text="modal")]

    article = model_of(*docs)
    phrase = model_of(*docs, phrases=[["warm sound"], ["warm sound"]])

    assert article.metadata["text_source"] == "article"
    assert "text_vectorizer" in article.metadata
    assert phrase.metadata["text_source"] == "sound_phrases"
    assert phrase.metadata["phrase_vectorizer"] == {"min_df": 1, "max_df": 1.0}
    assert "text_vectorizer" not in phrase.metadata


def test_phrases_replace_the_article_text():
    model = model_of(
        album("A", "jazz", text="modal saxophone"),
        album("B", "jazz", text="modal saxophone"),
        phrases=[["warm sound"], ["warm sound"]],
    )

    assert list(model.text_terms) == ["warm sound"]


def test_misaligned_phrases_are_rejected():
    with pytest.raises(ValueError, match="2 albums"):
        model_of(album("A", "jazz"), album("B", "jazz"), phrases=[["warm sound"]])


def test_no_phrases_at_all_gives_a_tags_only_model():
    seed = album("Seed", "jazz")
    model = model_of(seed, album("Match", "jazz"), phrases=[[], []])

    assert not model.has_text.any()
    assert len(model.text_terms) == 0
    assert len(recommend(model, [seed.album_id], 5)) == 1
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_recommend_tfidf.py -q`
Expected: the 8 new tests fail with `TypeError: build_model() got an unexpected keyword argument 'phrases'`; the existing tests still pass.

- [ ] **Step 3: Implement**

In `backend/src/crate_backend/recommend/tfidf.py`, replace `build_model` (lines 85-124) with:

```python
def build_model(
    docs: list[AlbumDoc],
    *,
    alpha: float = DEFAULT_ALPHA,
    ngram_range: tuple[int, int] = (1, 2),
    # As in scikit-learn: an int is a document count, a float a proportion.
    min_df: float = 2,
    max_df: float = 0.5,
    max_features: int | None = None,
    extra_metadata: dict[str, Any] | None = None,
    # Sound phrases per album, aligned with `docs`. When given they replace
    # the article text as the second block (approach "phrases").
    phrases: list[list[str]] | None = None,
) -> TfidfModel:
    if phrases is not None and len(phrases) != len(docs):
        raise ValueError(f"phrases has {len(phrases)} lists for {len(docs)} albums")
    text_params = {
        "ngram_range": ngram_range,
        "min_df": min_df,
        "max_df": max_df,
        "max_features": max_features,
    }
    tag_terms, tag_matrix = _tag_block(docs)
    if phrases is None:
        text_terms, text_matrix = _text_block(docs, text_params)
        text_metadata = {
            "text_source": "article",
            "text_vectorizer": {**text_params, "ngram_range": list(ngram_range)},
        }
    else:
        text_terms, text_matrix = _phrase_block(phrases, min_df, max_df)
        text_metadata = {
            "text_source": "sound_phrases",
            "phrase_vectorizer": {"min_df": min_df, "max_df": max_df},
        }
    # A row that vectorized to nothing (only stop words) is no text at all.
    has_text = np.diff(text_matrix.indptr) > 0
    metadata = {
        "model_version": datetime.now(UTC).isoformat(timespec="seconds"),
        "alpha": alpha,
        **text_metadata,
        "n_albums": len(docs),
        "n_with_text": int(has_text.sum()),
        "sklearn_version": sklearn.__version__,
        **(extra_metadata or {}),
    }
    return TfidfModel(
        album_ids=[doc.album_id for doc in docs],
        titles=[doc.title for doc in docs],
        tag_terms=tag_terms,
        tag_matrix=tag_matrix,
        text_terms=text_terms,
        text_matrix=text_matrix,
        has_text=has_text,
        metadata=metadata,
    )
```

Then add, directly after `_text_block`:

```python
def _phrase_block(
    phrases: list[list[str]], min_df: float, max_df: float
) -> tuple[np.ndarray, sparse.csr_matrix]:
    """Each phrase is one term, counted once per album; then smoothed IDF and
    L2 normalization, with the same document-frequency limits as text."""
    if not any(phrases):
        return np.array([], dtype=object), sparse.csr_matrix((len(phrases), 0))
    vectorizer = TfidfVectorizer(
        analyzer=_phrases_as_terms, binary=True, min_df=min_df, max_df=max_df
    )
    matrix = vectorizer.fit_transform(phrases)
    return vectorizer.get_feature_names_out(), sparse.csr_matrix(matrix)


def _phrases_as_terms(phrases: list[str]) -> list[str]:
    """The vectorizer's analyzer: an album's phrases are already its terms."""
    return phrases
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_recommend_tfidf.py tests/test_tfidf_model_store.py -q`
Expected: all pass.

- [ ] **Step 5: Lint, format, full suite**

Run: `uv run ruff check src tests && uv run ruff format src/crate_backend/recommend/tfidf.py tests/test_recommend_tfidf.py && uv run pytest -q`
Expected: clean; all pass.

- [ ] **Step 6: Commit**

```bash
git add src/crate_backend/recommend/tfidf.py tests/test_recommend_tfidf.py
git commit -m "feat: let a TF-IDF model use sound phrases as its text block

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

---

### Task 3: Setting and `--sound-phrases` build flag

**Files:**
- Modify: `backend/src/crate_backend/core/config.py` (after `tfidf_model_path`)
- Modify: `backend/src/crate_backend/scripts/build_tfidf_model.py` (docstring, imports, `parse_args`, `build`)
- Test: `backend/tests/test_build_tfidf_model_script.py`

**Interfaces:**
- Consumes:
  - Task 1: `prose_only`, `extract_all`, `SPACY_MODEL`.
  - Task 2: `build_model(..., phrases=...)`.
- Produces:
  - `Settings.tfidf_phrases_model_path: str`
  - CLI flag `--sound-phrases` (`args.sound_phrases: bool`)
  - `extract_phrases(docs: list[AlbumDoc]) -> tuple[list[list[str]], dict[str, str]]`, returning the phrase lists and the spaCy metadata.

- [ ] **Step 1: Write the failing tests**

Append to `backend/tests/test_build_tfidf_model_script.py`:

```python
def test_sound_phrases_is_off_by_default_and_read_when_given():
    assert not parse_args([]).sound_phrases
    assert parse_args(["--sound-phrases", "--no-reception"]).sound_phrases


@pytest.mark.parametrize("flags", [["--no-bigrams"], ["--max-features", "1000"]])
def test_sound_phrases_rejects_article_only_flags(flags):
    with pytest.raises(SystemExit):
        parse_args(["--sound-phrases", *flags])


def test_extract_phrases_reads_prose_and_joins_known_tags():
    from crate_backend.recommend.tfidf import AlbumDoc
    from crate_backend.scripts.build_tfidf_model import extract_phrases

    docs = [
        AlbumDoc(uuid.uuid4(), "A", {"acid jazz": 3}, text="It is an acid jazz record."),
        AlbumDoc(uuid.uuid4(), "B", {}, text="Elvin Jones – drums"),
        AlbumDoc(uuid.uuid4(), "C", {}, text=""),
    ]

    phrases, metadata = extract_phrases(docs)

    assert phrases == [["acid jazz"], [], []]
    assert metadata["spacy_version"] == "3.8.7"
    assert metadata["spacy_model"] == "en_core_web_sm-3.8.0"
```

Also add to the existing `test_parse_args_defaults`, after its last assert:

```python
    assert not args.sound_phrases
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_build_tfidf_model_script.py -q`
Expected: the new tests fail (`unrecognized arguments: --sound-phrases`, `ImportError: cannot import name 'extract_phrases'`, `AttributeError: ... 'sound_phrases'`).

- [ ] **Step 3: Add the setting**

In `backend/src/crate_backend/core/config.py`, directly after the `tfidf_model_path` line:

```python

    # Sound-phrase TF-IDF model file, written by
    # scripts/build_tfidf_model.py --sound-phrases and read by the API on
    # first use for approach "phrases".
    tfidf_phrases_model_path: str = str(_REPO_ROOT / "models" / "tfidf-phrases.joblib")
```

- [ ] **Step 4: Implement the flag**

In `backend/src/crate_backend/scripts/build_tfidf_model.py`:

(a) In the module docstring, replace the `Run with:` block and the paragraph after it with:

```
Run with: uv run python -m crate_backend.scripts.build_tfidf_model
          [--alpha 0.6] [--no-bigrams] [--no-reception] [--no-personnel]
          [--max-features N] [--out PATH]
      or: uv run --group phrases python -m crate_backend.scripts.build_tfidf_model
          --sound-phrases [--alpha 0.6] [--no-reception] [--out PATH]

Reads every album's genre/tag votes and stored Wikipedia text, fits the
model and writes one joblib file (default: settings.tfidf_model_path). With
--sound-phrases the text block is the sound phrases spaCy extracts from each
article's prose instead of every word, written to
settings.tfidf_phrases_model_path for approach "phrases" (design:
docs/superpowers/specs/2026-10-15-sound-phrases-design.md). The API loads a
file on its first request and keeps it until restart, so restart the backend
after rebuilding. Evaluation variants are separate files built with --out.
```

(b) Add these imports (keeping ruff's import order):

```python
import statistics
from collections import Counter
```

and:

```python
from crate_backend.recommend.sound_phrases import SPACY_MODEL, extract_all, prose_only
```

(c) In `parse_args`, add before `parser.add_argument("--out", ...)`:

```python
    parser.add_argument(
        "--sound-phrases",
        action="store_true",
        help="text block from spaCy-extracted sound phrases (approach 'phrases')",
    )
```

and after the existing alpha check, before `return args`:

```python
    if args.sound_phrases and (args.no_bigrams or args.max_features is not None):
        parser.error("--no-bigrams and --max-features apply to article text, not --sound-phrases")
```

(d) Add this function above `build`:

```python
def extract_phrases(docs: list[AlbumDoc]) -> tuple[list[list[str]], dict[str, str]]:
    """Each album's sound phrases from its article prose, and the parser's
    versions for the model metadata. Only this code path imports spaCy."""
    try:
        import spacy
    except ImportError as error:
        raise SystemExit("sound phrases need spaCy. Run: uv sync --group phrases") from error
    nlp = spacy.load(SPACY_MODEL)
    known_terms = frozenset(term for doc in docs for term in doc.term_votes)
    phrases = extract_all((prose_only(doc.text) for doc in docs), nlp, known_terms)
    metadata = {
        "spacy_version": str(spacy.__version__),
        "spacy_model": f"{nlp.meta['lang']}_{nlp.meta['name']}-{nlp.meta['version']}",
    }
    return phrases, metadata
```

(e) Replace `build` with:

```python
async def build(args: argparse.Namespace) -> None:
    settings = get_settings()
    default_out = (
        settings.tfidf_phrases_model_path if args.sound_phrases else settings.tfidf_model_path
    )
    out = args.out or Path(default_out)
    started = time.perf_counter()
    async with async_session_factory() as session:
        docs = await load_album_docs(
            session, drop_reception=args.no_reception, drop_personnel=args.no_personnel
        )
    loaded = time.perf_counter()

    phrases, phrase_metadata = extract_phrases(docs) if args.sound_phrases else (None, {})
    parsed = time.perf_counter()
    model = build_model(
        docs,
        alpha=args.alpha,
        ngram_range=(1, 1) if args.no_bigrams else (1, 2),
        max_features=args.max_features,
        phrases=phrases,
        extra_metadata={
            "catalog_source": _catalog_source(),
            "drop_reception": args.no_reception,
            "drop_personnel": args.no_personnel,
            **phrase_metadata,
        },
    )
    fitted = time.perf_counter()
    save_model(model, out)
    saved = time.perf_counter()

    matrix_bytes = sum(
        m.data.nbytes + m.indices.nbytes + m.indptr.nbytes
        for m in (model.tag_matrix, model.text_matrix)
    )
    n_albums, n_text = model.metadata["n_albums"], model.metadata["n_with_text"]
    label = "phrases" if phrases is not None else "text"
    print(f"Albums:          {n_albums:,} ({n_text:,} with {label}, {100 * n_text / n_albums:.0f}%)")
    print(f"Tag terms:       {len(model.tag_terms):,}")
    if phrases is not None:
        _print_phrase_summary(phrases, model)
    else:
        print(f"Text terms:      {len(model.text_terms):,}")
    print(f"Nonzeros:        {model.tag_matrix.nnz:,} tag, {model.text_matrix.nnz:,} {label}")
    print(f"Matrices:        {_megabytes(matrix_bytes)} in memory")
    print(f"File:            {out} ({_megabytes(out.stat().st_size)})")
    print(
        f"Time:            load {loaded - started:.1f}s, parse {parsed - loaded:.1f}s, "
        f"fit {fitted - parsed:.1f}s, save {saved - fitted:.1f}s"
    )
    print(f"Model version:   {model.metadata['model_version']}")
    if matrix_bytes > _LARGE_MODEL_BYTES and args.max_features is None and phrases is None:
        print("Model exceeds 500 MB: rebuild with --max-features 100000 and record the change.")


def _print_phrase_summary(phrases: list[list[str]], model: TfidfModel) -> None:
    """What the extraction found, so a build can be sanity-checked without
    opening the file."""
    per_album = [len(p) for p in phrases if p]
    median = statistics.median(per_album) if per_album else 0
    extracted = len({phrase for album in phrases for phrase in album})
    print(f"Phrases:         {extracted:,} distinct extracted, {len(model.text_terms):,} kept")
    print(f"Per album:       median {median:g} (albums with any phrase)")
    albums_per_term = Counter(
        dict(zip(model.text_terms, (model.text_matrix > 0).sum(axis=0).A1, strict=True))
    )
    print(
        "Most common:     "
        + "; ".join(f"{term} ({n})" for term, n in albums_per_term.most_common(25))
    )
```

and extend the `tfidf` import line to:

```python
from crate_backend.recommend.tfidf import (
    DEFAULT_ALPHA,
    AlbumDoc,
    TfidfModel,
    build_model,
    save_model,
)
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `uv run pytest tests/test_build_tfidf_model_script.py tests/test_config.py -q`
Expected: all pass.

- [ ] **Step 6: Lint, format, full suite**

Run: `uv run ruff check src tests && uv run ruff format src/crate_backend/core/config.py src/crate_backend/scripts/build_tfidf_model.py tests/test_build_tfidf_model_script.py && uv run pytest -q`
Expected: clean; all pass.

- [ ] **Step 7: Commit**

```bash
git add src/crate_backend/core/config.py src/crate_backend/scripts/build_tfidf_model.py tests/test_build_tfidf_model_script.py
git commit -m "feat: build a sound-phrase TF-IDF model with --sound-phrases

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

---

### Task 4: Serve `approach: "phrases"`

**Files:**
- Modify: `backend/src/crate_backend/recommend/model_store.py`
- Modify: `backend/src/crate_backend/api/routes/recommendations.py` (imports at line 13; `RecommendationRequest.approach` at lines 23-26; the loader block at lines 69-78; the ranking branch at lines 92-101)
- Test: `backend/tests/test_tfidf_model_store.py`, `backend/tests/test_recommendations_api.py`

**Interfaces:**
- Consumes:
  - Task 3: `Settings.tfidf_phrases_model_path`.
  - Task 2: `build_model(..., phrases=...)` (tests only).
- Produces:
  - `get_tfidf_phrases_model() -> TfidfModel | None`
  - `POST /recommendations` accepting `approach: "phrases"`

- [ ] **Step 1: Write the failing model-store tests**

Append to `backend/tests/test_tfidf_model_store.py`:

```python
@pytest.fixture
def phrases_path(tmp_path, monkeypatch):
    path = tmp_path / "tfidf-phrases.joblib"
    monkeypatch.setattr(get_settings(), "tfidf_phrases_model_path", str(path))
    monkeypatch.setattr(model_store, "_loaded", {})
    return path


def test_phrase_model_is_none_until_built(phrases_path):
    assert model_store.get_tfidf_phrases_model() is None

    save_model(_tiny_model(), phrases_path)

    assert model_store.get_tfidf_phrases_model() is not None


def test_loaders_keep_their_own_files(model_path, phrases_path):
    save_model(_tiny_model(), phrases_path)

    assert model_store.get_tfidf_model() is None
    assert model_store.get_tfidf_phrases_model() is not None
```

- [ ] **Step 2: Write the failing API tests**

Append to `backend/tests/test_recommendations_api.py`:

```python
@pytest.fixture
def use_phrases_model(monkeypatch):
    """Serve the given model (or None: no model file built) for phrases requests."""

    def use(model):
        monkeypatch.setattr(recommendations_route, "get_tfidf_phrases_model", lambda: model)

    return use


def _phrase_model(docs_and_phrases):
    docs = [doc for doc, _ in docs_and_phrases]
    phrases = [phrases for _, phrases in docs_and_phrases]
    return build_model(docs, min_df=1, max_df=1.0, phrases=phrases)


async def test_phrases_rank_from_the_model_and_explain_with_phrases(
    client, db_session, use_phrases_model
):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match", release_year=1999)
    model = _phrase_model(
        [(_doc(seed, "jazz"), ["chunky groove"]), (_doc(match, "jazz"), ["chunky groove"])]
    )
    use_phrases_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="phrases")

    assert response.status_code == 200
    body = response.json()
    assert body["approach"] == "phrases"
    assert body["model_version"] == model.metadata["model_version"]
    [result] = body["results"]
    assert result["id"] == str(match.id)
    assert result["shared_terms"] == ["jazz"]
    assert result["shared_text_terms"] == ["chunky groove"]


async def test_phrases_without_a_built_model_is_503(client, db_session, use_phrases_model):
    seed = await _album(db_session, "Seed", "a")
    use_phrases_model(None)

    response = await _post(client, album_ids=[str(seed.id)], approach="phrases")

    assert response.status_code == 503
    assert response.json() == {"detail": "Sound-phrase model not built"}


async def test_phrases_uses_its_own_model_not_the_tfidf_one(
    client, db_session, use_model, use_phrases_model
):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match")
    use_model(None)
    use_phrases_model(_phrase_model([(_doc(seed, "jazz"), []), (_doc(match, "jazz"), [])]))

    phrases = await _post(client, album_ids=[str(seed.id)], approach="phrases")
    tfidf = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert phrases.status_code == 200
    assert tfidf.status_code == 503


async def test_phrases_seed_without_phrases_still_ranks_on_tags(
    client, db_session, use_phrases_model
):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match")
    use_phrases_model(
        _phrase_model([(_doc(seed, "jazz"), []), (_doc(match, "jazz"), ["warm sound"])])
    )

    response = await _post(client, album_ids=[str(seed.id)], approach="phrases")

    [result] = response.json()["results"]
    assert result["id"] == str(match.id)
    assert result["shared_text_terms"] == []


async def test_phrases_seeds_missing_from_the_model_explain_the_empty_result(
    client, db_session, use_phrases_model
):
    seed = await _album(db_session, "Seed", "a")
    other = await _album(db_session, "Other")
    use_phrases_model(_phrase_model([(_doc(other, "jazz"), ["warm sound"])]))

    response = await _post(client, album_ids=[str(seed.id)], approach="phrases")

    assert response.json()["results"] == []
    assert response.json()["reason"] == "seeds_not_in_model"
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `uv run pytest tests/test_tfidf_model_store.py tests/test_recommendations_api.py -q`
Expected:
- the store tests fail with `AttributeError: module ... has no attribute 'get_tfidf_phrases_model'`;
- the API fixture's `monkeypatch.setattr` raises `AttributeError` for `get_tfidf_phrases_model`.

- [ ] **Step 4: Implement the loader**

Replace `get_tfidf_model` in `backend/src/crate_backend/recommend/model_store.py` with:

```python
def get_tfidf_model() -> TfidfModel | None:
    """The model at settings.tfidf_model_path, loaded on first use and kept
    for the life of the process. None while the file doesn't exist. That
    answer isn't cached, so a first build needs no restart; a rebuild of an
    already-loaded model does."""
    return _load_tfidf(Path(get_settings().tfidf_model_path))


def get_tfidf_phrases_model() -> TfidfModel | None:
    """The sound-phrase model at settings.tfidf_phrases_model_path, with the
    same loading rules as get_tfidf_model."""
    return _load_tfidf(Path(get_settings().tfidf_phrases_model_path))


def _load_tfidf(path: Path) -> TfidfModel | None:
    if path not in _loaded:
        if not path.exists():
            return None
        _loaded[path] = load_model(path)
    return _loaded[path]
```

and update its module docstring's first line to:

```python
"""The API process's copies of the model files: TF-IDF (Phase 4, Milestone 2),
sound-phrase TF-IDF, and sentence embeddings (Phase 5a)."""
```

- [ ] **Step 5: Implement the route**

In `backend/src/crate_backend/api/routes/recommendations.py`:

(a) Replace the model_store import with:

```python
from crate_backend.recommend.model_store import (
    get_embedding_model,
    get_tfidf_model,
    get_tfidf_phrases_model,
)
```

(b) Replace the `approach` field and its comment with:

```python
    # "overlap" (Jaccard, Phase 3), "tfidf" (Phase 4), "phrases" (TF-IDF
    # over sound phrases) or "embeddings" (Phase 5a). The default changes
    # only once the evaluation answer key picks a winner.
    approach: Literal["overlap", "tfidf", "phrases", "embeddings"] = "overlap"
```

(c) Add below `router = APIRouter(...)`:

```python
# Names in the 503 detail when an approach's model file isn't built.
_MODEL_NAMES = {"tfidf": "TF-IDF", "phrases": "Sound-phrase", "embeddings": "Embedding"}
```

(d) Replace the loader block:

```python
    model = None
    if request.approach != "overlap":
        # The first call reads the model file; keep that off the event loop.
        # Look the loader up here, not at import time, so tests can swap it.
        loader = get_tfidf_model if request.approach == "tfidf" else get_embedding_model
        model = await run_in_threadpool(loader)
        if model is None:
            name = "TF-IDF" if request.approach == "tfidf" else "Embedding"
            raise HTTPException(status_code=503, detail=f"{name} model not built")
```

with:

```python
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
```

(e) Replace `if request.approach == "tfidf":` in the ranking branch with:

```python
        if request.approach in ("tfidf", "phrases"):
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `uv run pytest tests/test_tfidf_model_store.py tests/test_recommendations_api.py -q`
Expected: all pass, including the existing `test_tfidf_without_a_built_model_is_503` (detail still `"TF-IDF model not built"`) and `test_the_default_approach_is_still_overlap`.

- [ ] **Step 7: Lint, format, full suite**

Run: `uv run ruff check src tests && uv run ruff format src/crate_backend/recommend/model_store.py src/crate_backend/api/routes/recommendations.py tests/test_tfidf_model_store.py tests/test_recommendations_api.py && uv run pytest -q`
Expected: clean; all pass.

- [ ] **Step 8: Commit**

```bash
git add src/crate_backend/recommend/model_store.py src/crate_backend/api/routes/recommendations.py tests/test_tfidf_model_store.py tests/test_recommendations_api.py
git commit -m "feat: serve sound-phrase recommendations as approach phrases

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

---

### Task 5: Frontend picker and "Sounds alike" label

**Files:**
- Modify: `frontend/app/page.tsx` (lines 62-67: `Approach` and `APPROACHES`; lines 985-989: the text-terms line)

**Interfaces:**
- Consumes: Task 4's `approach: "phrases"` and the unchanged `shared_text_terms` field.
- Produces: nothing for later tasks.

- [ ] **Step 1: Add the approach**

Replace lines 62-67 of `frontend/app/page.tsx`:

```tsx
type Approach = 'overlap' | 'tfidf' | 'embeddings';
const APPROACHES: { value: Approach; label: string }[] = [
  { value: 'overlap', label: 'Overlap (genre/tag Jaccard)' },
  { value: 'tfidf', label: 'TF-IDF (tags + Wikipedia text)' },
  { value: 'embeddings', label: 'Embeddings' },
];
```

with:

```tsx
type Approach = 'overlap' | 'tfidf' | 'phrases' | 'embeddings';
const APPROACHES: { value: Approach; label: string }[] = [
  { value: 'overlap', label: 'Overlap (genre/tag Jaccard)' },
  { value: 'tfidf', label: 'TF-IDF (tags + Wikipedia text)' },
  { value: 'phrases', label: 'TF-IDF (tags + sound phrases)' },
  { value: 'embeddings', label: 'Embeddings' },
];
```

- [ ] **Step 2: Label phrase matches "Sounds alike"**

Replace:

```tsx
                          {r.shared_text_terms.length > 0 && (
                            <small className="rec-terms">
                              Described alike: {r.shared_text_terms.join(', ')}
                            </small>
                          )}
```

with:

```tsx
                          {r.shared_text_terms.length > 0 && (
                            <small className="rec-terms">
                              {/* The approach that produced these results, not the picker's. */}
                              {groupRecs.approach === 'phrases'
                                ? 'Sounds alike'
                                : 'Described alike'}
                              : {r.shared_text_terms.join(', ')}
                            </small>
                          )}
```

- [ ] **Step 3: Lint and type-check**

Run (from `frontend/`): `npm run lint && npx tsc --noEmit`
Expected: no errors.

- [ ] **Step 4: Check by hand in the running app**

This needs Task 6's model build, so do it after Task 6 Step 2. Then:
1. Run `make dev` from the repo root.
2. Open http://localhost:3000.
3. Drag two albums with articles (e.g. *The Stone Roses*, *Definitely Maybe*) into a group.
4. Pick **TF-IDF (tags + sound phrases)** → **FIND RECOMMENDATIONS**. Results show `Shares: …` and, where phrases matched, `Sounds alike: …`.
5. Switch the picker to **TF-IDF (tags + Wikipedia text)** *without* re-running. The stale notice reads "These results came from phrases." and the lines still say **Sounds alike**.
6. Run again: the lines now say **Described alike**.

- [ ] **Step 5: Commit**

```bash
git add frontend/app/page.tsx
git commit -m "feat: offer sound-phrase recommendations in the approach picker

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

---

### Task 6: Build the real model and verify

**Files:**
- Modify: `docs/method-reports/sound-phrases.md` (status line)

**Interfaces:**
- Consumes: everything above.
- Produces: `models/tfidf-phrases.joblib` (gitignored, not committed).

- [ ] **Step 1: Full suite**

Run (from `backend/`): `uv run pytest -q && uv run ruff check src tests`
Expected: all pass; clean.

- [ ] **Step 2: Build the phrase model**

Run (from `backend/`; Postgres must be up, e.g. `make db` from the repo root): `uv run --group phrases python -m crate_backend.scripts.build_tfidf_model --sound-phrases`

Expected, roughly:
- **Albums with phrases:** about 40–45% of 25,000. The 300-album prototype run found phrases for 272/300 albums that have articles, and about 51% of albums have articles.
- **Per album:** median about 4.
- **Most common:** led by genre-style terms (*rock, pop, electronic, metal, hip hop*), with texture phrases further down (*guitar riff, distinctive sound, catchy*).
- **File:** `.../models/tfidf-phrases.joblib`.

If albums-with-phrases is under 30%, or the most-common list is dominated by words like *opening*, *executive* or *record*, stop and report: the rules regressed.

- [ ] **Step 3: Restart the API and spot-check**

Restart the backend (`make backend`, or the `make dev` session), then run:

```bash
curl -s localhost:8000/recommendations -H 'Content-Type: application/json' \
  -d '{"album_ids":["6b7cb74a-df56-4da9-bc11-0f086b779201"],"approach":"phrases","limit":5}' | python3 -m json.tool | head -40
```

Expected: HTTP 200, `"approach": "phrases"`, five results for *Heaven or Las Vegas*, at least one with non-empty `shared_text_terms`.

- [ ] **Step 4: Do Task 5 Step 4 (the hand check in the app)**

- [ ] **Step 5: Update the method report status**

In `docs/method-reports/sound-phrases.md`, replace the status block:

```markdown
> **Status: proposed, not built.** Everything below about extraction comes from two throwaway probes run on 2026-10-15 over the 300-album text-relevance sample (`eval/text-relevance/`). The scoring step is a design proposal and hasn't been graded.
```

with:

```markdown
> **Status: built, not graded.** Served as `approach: "phrases"` and selectable in the frontend; build with `uv run --group phrases python -m crate_backend.scripts.build_tfidf_model --sound-phrases`. Extraction rules: [`sound_phrases.py`](../../backend/src/crate_backend/recommend/sound_phrases.py). No graded comparison yet.
```

- [ ] **Step 6: Commit**

```bash
git add docs/method-reports/sound-phrases.md
git commit -m "docs: mark the sound-phrase method as built

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QonRbUmv9DJbkYKYzi6MV8"
```

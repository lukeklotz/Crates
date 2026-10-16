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
            # The noun's lemma, so "acoustic guitar" and "acoustic guitars"
            # are one phrase.
            phrase = text if anchor in GENERIC_NOUNS else f"{text} {anchor}"
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
    # Only capitalized words: the small model also tags plain adjectives
    # ("an acoustic guitar") as entities, while names and nationalities
    # ("Canadian", "Vancouver") are capitalized.
    if token.ent_type_ in DROPPED_ENTITIES and token.text[:1].isupper():
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

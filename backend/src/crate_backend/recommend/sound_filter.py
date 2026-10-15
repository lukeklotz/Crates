"""Keep only the article sentences that describe how an album sounds, for
the `embed-tags+sound` variant (Phase 5a follow-up).

Most stored article text is release logistics, chart history and band
biography, which pulls an album's text vector toward the same artist or
toward "famous album" articles instead of toward similar-sounding music.
Each sentence is embedded with the same encoder as the model and kept when
its mean similarity to its TOP_EXAMPLES closest SOUND_EXAMPLES beats the same
measure over OTHER_EXAMPLES by more than a margin. Comparing against both
sets avoids one absolute similarity cutoff, which would shift with writing
style; averaging a few examples keeps one lucky match from deciding.
Credit lines ("Name – bass guitar") are dropped without scoring: they name
people, not sounds, yet the encoder rated even crew lines like
"Tim Young – mastering" as sound.

Examples tuned on 300 sampled articles (2026-10-15): about two thirds of
kept sentences describe the sound, and nearly all dropped ones do not.
"""

import re
from dataclasses import dataclass

import numpy as np

from crate_backend.recommend.embeddings import Encoder
from crate_backend.recommend.text_cleaning import _CREDIT_LINE

DEFAULT_MARGIN = 0.0
TOP_EXAMPLES = 3
# A "Name – roles" line longer than this is prose with a dash in it.
MAX_CREDIT_LINE_CHARS = 160

# Written to cover the ways articles describe music: instrumentation,
# production, rhythm, vocals, mood, genre and comparisons to other artists.
SOUND_EXAMPLES = (
    "The album features jangly guitars over a loose, danceable groove.",
    "The songs are built on down-tuned, polyrhythmic riffs and blast beats.",
    "Lush string arrangements accompany her breathy, intimate vocals.",
    "The production is lo-fi, with tape hiss and distorted drum machines.",
    "Its sound blends psychedelic rock with elements of funk and soul.",
    "The record moves away from synth-pop toward a stripped-down acoustic folk sound.",
    "Critics compared the album's droning, reverb-heavy guitars to My Bloody Valentine.",
    "The tracks are slow and melancholic, driven by sparse piano and ambient textures.",
    "Aggressive, fast-paced songs with shouted vocals and short running times.",
    "The album draws on jazz harmony, with extended saxophone solos and swing rhythms.",
    "Heavy basslines, chopped samples and boom bap beats underpin the rapping.",
    "The music is upbeat and anthemic, with soaring choruses and layered harmonies.",
    "Critics praised the album's dense, hypnotic wall of sound.",
    "The guitar solos are fast and technical, with heavy distortion.",
    "Reviewers described the record as dreamy and atmospheric, with shimmering synthesizers.",
    "The song is a mid-tempo ballad with a gospel choir and organ.",
)

# The kinds of sentence that dominate album articles without saying anything
# about the sound.
OTHER_EXAMPLES = (
    "The album was released on 9 November 1998 by Nuclear Blast Records.",
    "It peaked at number three on the Billboard 200 and was certified platinum.",
    "The band embarked on a world tour to promote the record.",
    "The singer struggled with addiction and later went to rehab.",
    "The album was recorded at Battery Studios in London over eight months.",
    "Rolling Stone ranked it among the 500 Greatest Albums of All Time.",
    "The cover art was photographed by a friend of the band.",
    "A remastered deluxe edition with bonus tracks was reissued on vinyl in 2017.",
    "Dark Comedy is the second studio album by American rapper Open Mike Eagle.",
    "At Metacritic, the album received an average score of 75, indicating generally favorable reviews.",
    "A remix of the single featuring two guest rappers was released in May 2021.",
    "After the bassist left, the band continued as a four-piece.",
    "The producer helped the singer regain focus with a fresh perspective.",
    "Several shows in the United States and Canada were cancelled.",
    "The singer said it was the best song she had ever written.",
)

# A sentence ends at . ! or ? followed by whitespace and a capital letter,
# optionally behind an opening quote or bracket. "1.5 rpm" and "e.g. this"
# do not split.
_SENTENCE_BREAK = re.compile(r"(?<=[.!?])\s+(?=[\"“‘'(\[]?[A-Z])")


def split_sentences(text: str) -> list[str]:
    """Sentences of `text`. Each line is split on its own, so a credits line
    ("Name – bass guitar") is one sentence."""
    sentences: list[str] = []
    for line in text.splitlines():
        sentences.extend(s.strip() for s in _SENTENCE_BREAK.split(line) if s.strip())
    return sentences


@dataclass(frozen=True)
class SoundFilterResult:
    # One per input text: its kept sentences joined by spaces, or "".
    texts: list[str]
    n_sentences: int
    n_kept: int
    # Albums that had text and kept none of it.
    n_emptied: int


def filter_sound(
    texts: list[str], encoder: Encoder, margin: float = DEFAULT_MARGIN
) -> SoundFilterResult:
    """Keep the sentences of each text that describe sound. All prose
    sentences are encoded in a single call so the encoder can batch them
    freely."""
    examples = encoder.encode([*SOUND_EXAMPLES, *OTHER_EXAMPLES])
    sound, other = examples[: len(SOUND_EXAMPLES)], examples[len(SOUND_EXAMPLES) :]

    per_text = [split_sentences(text) for text in texts]
    sentences = [s for group in per_text for s in group]
    prose = np.array([not _is_credit_line(s) for s in sentences], dtype=bool)
    keep = np.zeros(len(sentences), dtype=bool)
    if prose.any():
        vectors = encoder.encode([s for s, p in zip(sentences, prose, strict=True) if p])
        lead = _top_mean(vectors @ sound.T) - _top_mean(vectors @ other.T)
        keep[prose] = lead > margin

    kept_texts: list[str] = []
    position = 0
    for group in per_text:
        flags = keep[position : position + len(group)]
        position += len(group)
        kept_texts.append(" ".join(s for s, k in zip(group, flags, strict=True) if k))
    return SoundFilterResult(
        texts=kept_texts,
        n_sentences=len(sentences),
        n_kept=int(keep.sum()),
        n_emptied=sum(
            1 for group, kept in zip(per_text, kept_texts, strict=True) if group and not kept
        ),
    )


def _is_credit_line(sentence: str) -> bool:
    return len(sentence) <= MAX_CREDIT_LINE_CHARS and _CREDIT_LINE.match(sentence) is not None


def _top_mean(similarities: np.ndarray) -> np.ndarray:
    """Each row's mean over its TOP_EXAMPLES largest values."""
    k = min(TOP_EXAMPLES, similarities.shape[1])
    return np.sort(similarities, axis=1)[:, -k:].mean(axis=1)

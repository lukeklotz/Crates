# Recommendation report: TF-IDF similarity

## How it works

TF-IDF stands for **term frequency–inverse document frequency**. It gives a term more weight when it is prominent in an album's data but uncommon across the catalog. Crate builds two separate, length-normalized vectors for each album:

1. **Genre/tag vector:** each normalized genre or tag name is one term. MusicBrainz vote counts supply frequency, compressed with `1 + ln(votes)`, then rarity across albums supplies IDF.
2. **Wikipedia text vector:** cleaned article text supplies words and two-word phrases. Common English and music-press filler words are removed; terms appearing in only one article or more than half the articles are dropped.

The build code in [`tfidf.py`](../../backend/src/crate_backend/recommend/tfidf.py) shows both representations:

```python
{term: 1 + math.log(max(votes, 1)) for term, votes in doc.term_votes.items()}
tfidf = TfidfTransformer(norm="l2", smooth_idf=True, sublinear_tf=False).fit_transform(tf)

vectorizer = TfidfVectorizer(
    stop_words=sorted(ENGLISH_STOP_WORDS | MUSIC_PRESS_STOPWORDS),
    sublinear_tf=True,
    **params,
)
```

At request time, a dot product of normalized vectors gives cosine similarity. If both albums have article text, the score is **0.6 × tag similarity + 0.4 × text similarity**; otherwise it uses tag similarity alone. Candidate scores are summed across seeds. Seeds and nonpositive results are removed, and the top terms contributing to each match become the explanations.

## Analogy and ELI5 example

Imagine a class where every album has a list of describing words. Nearly everyone writes `music`, so it tells you little. Only two students write `spiritual jazz`, so that phrase is a stronger clue that their albums belong together. TF-IDF acts like a teacher who puts more weight on distinctive clues and less on words everyone used.

For a listener who groups two modal-jazz albums, another album sharing rare tags such as `spiritual jazz` can rank above one that shares only `jazz`. If both albums also have Wikipedia articles, overlapping article words and phrases can add evidence. The exact score depends on the fitted catalog statistics, so this is an illustration, not a prediction of a particular result.

## Why it was chosen

The Jaccard baseline treats common and rare terms equally. TF-IDF directly tests whether rarity weighting improves recommendations. Per-album credits and labels were unavailable, so Wikipedia articles added descriptive text beyond the tag list. The team chose a classical text method before semantic embeddings so the same data can be compared under two kinds of representation. Separate tag and article vectors let albums without articles remain searchable through their tags.

## Tradeoffs

- **Strengths:** Distinctive terms carry more weight; vote counts matter without growing linearly; explanations can name the terms that contributed; prebuilt sparse matrices make online scoring fast.
- **Limitations:** It needs literal shared vocabulary: `melancholic` and `sorrowful` do not automatically match. Wikipedia text can overemphasize artist or personnel names. Rare but misleading mood tags can also dominate.
- **Coverage bias:** Wikipedia articles are far more common for popular albums. The tag fallback prevents missing text from becoming an empty representation, but the blend can still change score scales: documented by-eye checks found many no-article albums above article-backed ones.
- **Operational cost:** The model must be built offline and loaded from a file. Newly added albums are absent until a rebuild, and a running API must restart to use a rebuilt, already-loaded model. The default remains Jaccard while evaluation is unfinished.

## Source pointers

- [`backend/src/crate_backend/recommend/tfidf.py`](../../backend/src/crate_backend/recommend/tfidf.py), lines 85–221: feature build, blend, ranking, explanations.
- [`backend/src/crate_backend/recommend/text_cleaning.py`](../../backend/src/crate_backend/recommend/text_cleaning.py): normalization and article filtering.
- [`docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md`](../superpowers/specs/2026-09-26-tfidf-text-recommender-design.md): rationale and data-coverage decisions.

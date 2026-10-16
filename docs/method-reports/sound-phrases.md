# Recommendation report: sound phrases

> **Status: built, not graded.** Served as `approach: "phrases"` and selectable in the frontend; build with `uv run --group phrases python -m crate_backend.scripts.build_tfidf_model --sound-phrases`. Extraction rules: [`sound_phrases.py`](../../backend/src/crate_backend/recommend/sound_phrases.py). No graded comparison yet.

## How it works

The method reads each album's cleaned Wikipedia article with the spaCy parser (`en_core_web_sm`) and keeps only short phrases that describe how the album sounds. Those phrases are then treated as extra tags.

1. **Parse.** spaCy labels each word's part of speech, which word it modifies, and whether it is negated. It also tags names, places, nationalities and dates (named-entity recognition).
2. **Anchor on music nouns.** There are about 60 of them, in two groups:
   - *Specific nouns* (*guitar, vocals, production, groove, sound, drums, strings, riff, texture…*) keep the noun in the phrase.
   - *Generic nouns* (*album, song, record, music, band, singer, rapper…*) contribute only their descriptor.
3. **Take what describes the anchor:**
   - adjectives and noun modifiers: "**crunchy** guitars", "**vintage** production", "**industrial** band" → *industrial*;
   - adjectives after a linking verb: "the sound is **warm and cinematic**" → *warm sound*, *cinematic sound*;
   - labels after describing verbs: "called the album **ferocious**", "described it as **raw**".

   Hyphenated words are rebuilt whole (*pop-punk*, *lo-fi*, *ear-candy choruses*).
4. **Drop:**
   - negated phrases ("no ska", "lacks melody");
   - tokens recognized as names, places, nationalities, dates or numbers;
   - a hand-written ignore list of position, sales and opinion words (*debut, opening, charting, selling, best, favorite, biggest*).
5. **Separate credits.** Phrases from personnel lines ("Name – bass guitar") are marked as credits, so they can be weighted or dropped on their own.
6. **Score (proposed).** Each album gets a TF-IDF phrase vector:
   - **Weighting:** a phrase counts more when it is rare across the catalog. *chunky groove* is distinctive; *bass guitar*, which is on almost every album, is close to worthless.
   - **Blend:** when both albums have phrases, the phrase cosine is blended with the tag cosine the same way TF-IDF text is today (e.g. 0.6 × tag + 0.4 × phrase). Otherwise only tags are used.
   - **Explanations:** the shared phrases with the most weight become the match explanation.

Example output from the probe:

| Album | Extracted phrases |
|---|---|
| Red Clay — Freddie Hubbard | chunky groove |
| Artificial Soldier — Front Line Assembly | industrial, electronic, ferocious, brutal |
| BELOVED — GIVĒON | soul, warm feel, heavy drums, vintage production, staccato strings, cinematic sound, groovy production… |
| Rocks — Aerosmith | hard-rock, brash, raw, piano riff, guitar riff, drug-fueled, dark… |
| (Breach) — The Wallflowers | *(nothing: the article doesn't describe the sound)* |

## Analogy and ELI5 example

The text methods built so far read an album's review by photocopying the whole page. This one goes through the review with a highlighter and marks only the words a musician would use to describe the record: *raw, brash, piano riff, crunchy guitars*. Two albums are similar when their highlighted words match, and rare highlights like *chunky groove* count for more than common ones like *bass guitar*. Studio names, chart positions and the band's backstory never get highlighted, so they can't make two albums look alike.

## Why it was chosen

- **The text is mostly off-topic.** Reading the 300-album sample showed most embedding text isn't about the sound. In section terms, composition/music/musical style sections are under 10% of article words.
- **Graded results back that up:**
  - Adding the whole article lowered scores for both TF-IDF (0.665 → 0.499 NDCG@5) and embeddings (0.598 → 0.415).
  - Filtering at the sentence level (`embed-tags+sound`) helped only a little (0.451). It still kept about one off-topic sentence in three, and names and dates got through inside kept sentences.
- **Sentence structure cuts at the right level.** Extracting phrases by grammar keeps descriptors and can't let names or dates through.
- **TF-IDF fits sparse phrases.** It's the strongest graded variant, it downweights common phrases automatically, and it explains matches in exact terms.

## How it compares with the existing methods

NDCG@5 is a 0-to-1 score for how good the top 5 picks are, with good picks near the top counting more. The numbers below cover 10 seeds from the 2026-10-15 run, which mixes human and LLM grades; with this few seeds, gaps of a few hundredths are noise.

| Method | What it compares | Article text used | NDCG@5 |
|---|---|---|---|
| overlap (Jaccard) | Sets of genre/tag names | None | 0.497 |
| tfidf-tags | Tags weighted by votes and rarity | None | **0.665** |
| tfidf-tags+text | Tags + every article word and word pair, minus filler words | All of it | 0.499 |
| embed-tags | Tag line as a meaning vector | None | 0.598 |
| embed-tags+text | Above + the whole article as a meaning vector | All of it | 0.415 |
| embed-tags+sound | Above, only sentences that read like sound descriptions | Sound-like sentences | 0.451 |
| **sound phrases** | Tags + extracted sound phrases, TF-IDF weighted | Descriptive phrases only | not built |

- **vs `tfidf-tags+text`:** same machinery, but fed only sound vocabulary instead of every word. This is the most direct test of whether text hurt because it was off-topic.
- **vs `embed-tags+sound`:**
  - *Filtering level:* phrase-level and rule-based instead of sentence-level and similarity-based.
  - *Result:* cleaner, with no names or dates, but it misses descriptions that don't fit "descriptor + music noun".
- **vs the embedding methods:** no synonyms (*warm sound* and *warm production* are different terms), but every match is exact and explainable.

## Tradeoffs

- **Strengths:**
  - The most on-topic text signal of any method.
  - Explanations can name the shared phrases ("shares: crunchy guitars, pop-punk").
  - In the probe, 87% of extracted phrases were not already in the album's tags.
  - spaCy runs only at build time, so serving stays a dot product.
- **Limitations:**
  - Extraction is sparse: a median of 4 new phrases per album, and 50 of 300 sampled albums got none.
  - The rules match exact phrasing. Descriptions in unusual sentence shapes are missed, and the parser makes mistakes.
  - The ignore list and noun list are hand-written and need upkeep.
  - Known open issues from probe round 2:
    - multiword genres split apart (*acid* / *jazz*, a stray *hop*);
    - leftover position words (*opening, earlier, subsequent, executive*).
- **Scoring bias against albums with phrases (open decision):**
  - **The blend:** when both albums have phrases, the score is 0.6 × tag + 0.4 × phrase cosine. When either album has none, the score is the full tag cosine.
  - **Why it bites:** phrase vectors are short (median 5), so phrase cosines are usually near 0. A candidate *with* phrases therefore scores about 0.6× its tag similarity, while one without keeps 1.0×.
  - **Measured on the built model (200 random seeds):**
    - only 29% of top-20 results have phrases, against 45% of the catalog;
    - only about 25% of results show any shared phrase.
  - **Not specific to this method:** the existing `tfidf` approach has the same bias.
  - **Options:** blend one-sided pairs too (missing phrase cosine = 0), or use a separate α for phrases.
- **Coverage and ranking risk:**
  - About half the catalog has no article, so the method can affect at most about 44% of albums.
  - Descriptive phrases come mostly from long articles about popular albums, which adds to the popularity skew the existing text methods already have.
- **Operational cost:**
  - Adds spaCy and an English model (about 12 MB) as a build-only dependency group, like `embeddings`.
  - Parsing about 12.8k articles adds minutes to the build.
  - New albums need a rebuild, as with the other offline models.

## Source pointers

- [`backend/src/crate_backend/recommend/text_cleaning.py`](../../backend/src/crate_backend/recommend/text_cleaning.py): `clean_article` and the credit-line pattern; extraction would run on its output.
- [`backend/src/crate_backend/recommend/tfidf.py`](../../backend/src/crate_backend/recommend/tfidf.py): the TF-IDF build and α-blended scoring the phrase vector would plug into.
- [`backend/src/crate_backend/recommend/sound_filter.py`](../../backend/src/crate_backend/recommend/sound_filter.py): the sentence-level filter behind `embed-tags+sound`, the comparison point.
- [`eval/text-relevance/`](../../eval/text-relevance/): the 300-album sample of embedding text the probes ran on.
- [`eval/results/2026-10-15.md`](../../eval/results/2026-10-15.md): the graded scores quoted above.

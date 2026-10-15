# Recommendation report: semantic embeddings

## How it works

A pretrained sentence encoder maps text into a vector of numbers. Vectors pointing in similar directions indicate similar meaning even when the original words differ. Crate uses the pinned `BAAI/bge-small-en-v1.5` encoder during an **offline build**. For each album, it embeds (1) a comma-separated string of its top 20 genres/tags by vote and (2) its cleaned Wikipedia article in 250-word chunks. It averages the article's chunk vectors and normalizes the result. Albums without an article keep a tag vector and a zero text vector.

The core build and scoring code in [`embeddings.py`](../../backend/src/crate_backend/recommend/embeddings.py) is:

```python
tag_texts = [tag_string(doc.term_votes) for doc in docs]
encoded_tags = _unit_rows(encoder.encode([tag_texts[row] for row in tagged]))

np.add.at(text_vectors, owners, _unit_rows(encoder.encode(chunks)))
text_vectors[has_text] /= norms[has_text, None]

return np.where(both_have_text, alpha * tag + (1 - alpha) * text, tag).sum(axis=0)
```

The vectors are unit length, so their dot product is cosine similarity. As with TF-IDF, a pair with article text on both sides uses **0.6 × tag cosine + 0.4 × article cosine**; otherwise it uses tag cosine alone. Scores sum across group seeds. Seed albums and nonpositive scores are excluded. The service loads saved vectors and does not run the neural encoder for each request. The displayed shared tags are drawn from actual metadata; they are **not** an explanation of what the embedding itself learned.

## Analogy and ELI5 example

Imagine placing albums on a map where nearby spots mean “these descriptions feel alike.” A word-count method looks for identical street names. This model can place `melancholic` and `sorrowful` near each other because it has learned that the words have related meanings. A new candidate could therefore be close to a sad, quiet seed even if the two descriptions use different words. That is a capability of the representation, not a guarantee that any particular pair will rank well.

## Why it was chosen

TF-IDF cannot connect different wording with similar meaning. The project therefore compares pretrained semantic vectors with TF-IDF over the **same** tag and Wikipedia inputs, making the representation change easier to evaluate. The small 384-dimensional encoder was chosen for an 8 GB development machine and its 512-token window; the design notes explicitly say this choice was based on outside benchmark recollection, not a Crate-specific measurement. Chunking preserves the article beyond its introduction. Keeping vectors in a file avoids adding a vector database at this catalog size.

## Tradeoffs

- **Strengths:** Can match related descriptions without exact shared words; fast online dot-product scoring after the offline build; no per-request encoder or `torch` requirement in the API.
- **Limitations:** Semantic proximity can be vague or misleading. Averaging chunks can blur a long article's distinct sections. The model cannot reliably say which words caused a match, so the UI's shared-tag evidence may not explain the actual vector score.
- **Coverage and ranking risk:** About half the catalog has album article text, with coverage strongly skewed toward popular albums. Averaged article vectors can have a different cosine-score distribution from tag vectors, potentially favoring albums with text.
- **Operational cost:** Encoder weights and article chunks take time and memory to build. New albums require a rebuild, and the API needs a restart to use a rebuilt model already loaded in memory. The method is selectable but remains opt-in; the default is still Jaccard pending a measured comparison.

## Source pointers

- [`backend/src/crate_backend/recommend/embeddings.py`](../../backend/src/crate_backend/recommend/embeddings.py), lines 60–141 and 180–235: chunking, vectors, scoring, explanation terms.
- [`backend/src/crate_backend/recommend/sentence_encoder.py`](../../backend/src/crate_backend/recommend/sentence_encoder.py), lines 12–83: encoder identity and offline use.
- [`docs/superpowers/specs/2026-10-08-embedding-recommender-design.md`](../superpowers/specs/2026-10-08-embedding-recommender-design.md): design decisions and risks.

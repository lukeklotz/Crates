# Crates


Crates is an album-discovery and recommendation platform built around a visual sandbox. Search for albums, drag them onto an open canvas, and group them by mood or direction. Each group becomes the input for recommendations, with a per-group control that leans results toward obscure, mid-popularity, or widely popular albums.

Recommendations focus on cultural and descriptive similarity by using genres, tags, Wikipedia text, labels, and artist relationships. MusicBrainz release groups are the canonical album identity.

I wanted to build this project because I love looking for new music, but I was getting bored with the algorithms that Spotify and YouTube use. They often seem to recommend music that is most likely to keep me on their apps.

While that sounds great, I find that the music they recommend is missing something. Oftentimes, I hear a song and think, “Ah, yes, this is... good... I guess...” The song is good, but it’s missing that special thing that makes it interesting. My hope with this project is to develop a system that can recommend something interesting.

## How recommendations work

There are two recommenders right now. Both run over the same album data.

- **TF-IDF (term frequency–inverse document frequency).** Each album becomes a sparse vector of its genre/tag terms and the words and two-word phrases from its Wikipedia article. A term counts for more when MusicBrainz users voted for it often on that album, and for less when lots of albums share it. For example, "shoegaze" says more about an album than "rock" does. Common words from music writing, like "album" and "chart," are dropped.
- **Sentence embeddings.** A pretrained encoder (`BAAI/bge-small-en-v1.5`) turns text into dense vectors where passages that mean similar things land close together, even when they use different words. Long articles are split into chunks of about 250 words, and the chunk vectors are averaged. A variant called `tags+sound` first filters each article down to sentences that describe how the record sounds. It does this by comparing each sentence's embedding to example sentences about sound and to example sentences about chart runs, tours, and release dates.

Each album gets two vectors, one for tags and one for text. Similarity between two albums is the **cosine similarity** of their vectors, which measures the angle between them. When both albums have an article, the tag score and the text score are blended. When either one lacks an article, they're compared on tags alone, so they aren't penalized for the missing text. A group's recommendations are ranked by the sum of each candidate's similarity to every album in the group.

**Popularity** is separate from similarity. It is each album's percentile rank among Last.fm listener counts, and it drives the obscure-to-popular control. Models are evaluated offline against a set of seed albums, with graded relevance judgments in `eval/`.

## Layout

- `backend/` — Python API, data models, and migrations
- `frontend/` — the sandbox UI (Next.js)
- `pipelines/`, `catalog/` — catalog ingestion and feature building
- `models/`, `eval/` — recommendation models and evaluation
- `infrastructure/`, `docker-compose.yml` — local and deployment setup
- `docs/` — plans and design notes

See `crate-ml-engineering-project-plan.md` for the full project plan.

> **Status:** Crates is under active development. A fully deployed version will be available soon.

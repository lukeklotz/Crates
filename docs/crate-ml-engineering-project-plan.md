# Crate: Machine Learning Engineering Project Plan

## Project summary

Crate is an album-discovery and recommendation platform built around a visual album sandbox and deliberate listening. Users search for albums, drag them onto an open canvas, and organize them into groups that express a particular mood, interest, or direction. Each group becomes an explicit input for recommendations, with controls that let users steer results toward lesser-known albums, moderately popular albums, or widely popular albums. Users can optionally rate albums from 0–5 stars and describe what an album feels like in their own words; ratings are not required to begin discovering music.

The project is intended to serve two purposes:

1. Build a genuinely useful music-discovery product.
2. Demonstrate the complete skill set expected of a machine learning engineer: data ingestion, feature engineering, classical ML, deep learning, evaluation, model deployment, distributed processing, monitoring, and production software engineering.

## Conversation and decision summary

The project began with the question: **What single project would provide the strongest practical preparation and portfolio evidence for a machine learning engineering job?** An end-to-end album recommendation platform emerged as the best fit because it combines Luke's interests in music, software engineering, and machine learning while requiring substantially more than a notebook-level model.

Research into current machine learning roles—particularly roles available around Portland, Beaverton, and Hillsboro—showed repeated demand for Python, SQL, PyTorch, AWS, Spark, data pipelines, Docker, CI/CD, and model operationalization. Portland-specific opportunities also suggest two useful specializations: retail and recommendation systems around companies such as Nike, and C++/GPU-oriented AI infrastructure around Intel.

The following major decisions were made:

- **PyTorch** will be the primary deep-learning framework.
- **scikit-learn** will be used for preprocessing, transparent baselines, classical NLP, and evaluation.
- **MusicBrainz** will be the canonical source for album identity and structured music metadata.
- A Crate album will primarily correspond to a **MusicBrainz release group**, preventing separate pressings and reissues from being treated as unrelated albums.
- **Discogs** may later be evaluated as an enrichment source, but its licensing and API restrictions make it unsuitable as the project's canonical foundation.
- Recommendations will emphasize **cultural and descriptive similarity**, not acoustic or sonic analysis.
- Album representations will incorporate genres, tags, descriptive language, labels, performers, instruments, producers, and artist relationships.
- Crate will eventually collect its own high-value data by allowing users to attach descriptive words or short reflections to album ratings.
- The system will begin with a modest catalog and single-machine processing, then expand to S3, Parquet, PySpark, incremental pipelines, and production infrastructure only when those additions solve a demonstrated problem.
- The application will precompute expensive features and candidate relationships offline so that live recommendations remain fast.
- The main page will be an initially blank album sandbox, with search and visual grouping as the primary discovery workflow.
- A user-created group will be the primary recommendation context. Adding an album to a group expresses intent for that search, not a positive rating or a permanent taste preference.
- Recommendation controls will belong to each group, starting with a popularity preference. Ratings and broader personalization will remain optional supporting signals.

The resulting system will progress from explainable heuristics to TF-IDF retrieval, semantic text embeddings, personalized ranking, and collaborative filtering. Every advanced model must be compared against simpler baselines under the same evaluation protocol.

## UI/UX direction — The album sandbox

### Main page and search

The main page opens onto a blank canvas with a persistent album search field and a short empty-state prompt: **Search for an album. Bring it here. Find what connects.** There is no initial recommendation feed or required rating questionnaire. Search results appear in a compact panel showing cover art, album title, artist, and release year. Users can drag a result onto the canvas or choose **Add to sandbox**. Adding the first album removes the empty-state prompt.

Album cards prioritize cover art while keeping titles and artists readable. Users can move cards, inspect album details, or remove cards without changing their ratings. The workspace saves automatically, with a visible save state and undo for removal and grouping changes. The first release can use a finite, scrollable canvas; an infinite canvas and zoom are later options if user testing shows a need.

### Visual grouping

Users arrange albums freely, select several cards, and choose **Create group**. A visible enclosing frame identifies membership and offers an optional name, such as “Rainy evening” or “More like these.” Dropping another album inside an existing frame highlights the destination before confirming membership. Proximity alone does not silently create groups, and distances between cards do not affect recommendation weights in the first release.

Each group has a title, album count, and **Find recommendations** action. A single album is enough to start; multiple albums define a shared direction. Users can move a group as a unit, add or remove members, rename it, or ungroup it while keeping its albums on the canvas. An album can be reused across groups through **Add to group**, but cannot appear twice in the same group. Dragging a card between groups moves that instance; copying to another group is an explicit action.

Dragging must have equivalent button and keyboard actions: add to sandbox, select albums, create group, and move to or remove from a group. On narrow screens, stacked groups and an **Add to group** picker preserve the workflow without requiring precise spatial placement.

### Group recommendations and controls

Selecting **Find recommendations** opens a side panel tied to that group. It shows the seed albums, recommendation settings, and results while keeping the canvas visible. Results never automatically become group members. Each result includes a cover, title, artist, a short evidence-based explanation, and actions to inspect, save, dismiss, or add it to a chosen group.

The first algorithm control is **Popularity**, with three clear options:

| Setting | Intended behavior |
| --- | --- |
| Lesser-known | Favor relevant albums with lower measured popularity. |
| Somewhere in the middle | Favor relevant albums in a moderate popularity range. |
| Widely popular | Favor relevant albums with higher measured popularity. |

Include a separate **No preference** default so that “middle” is not confused with “ignore popularity.” Start with discrete options rather than a continuous slider that implies unsupported precision. Explain the control with: **Choose how well-known you want the results to be.** Popularity is distinct from similarity: a lesser-known result should still relate to the seed group.

Changing a setting marks the results as needing an update; **Update recommendations** applies the new setting. Changing group membership has the same effect. Existing results remain visible with their previous context until a replacement succeeds. Each group remembers its own settings. If the available catalog cannot satisfy a preference, explain that limitation and offer to broaden it rather than silently ignoring the selection.

Later controls may include **Stay close ↔ Explore further**, an era range, artist exclusions, and per-album influence. Keep these out of the initial interface until their behavior can be demonstrated reliably. Do not expose raw model weights or imply that semantic descriptions establish acoustic similarity.

### Recommendation contract and data requirements

- Start with equal influence for all seed albums. Retrieve candidates for each seed and combine their similarity evidence; evaluate whether results represent the group rather than allowing one seed to dominate.
- Exclude the seed release groups and duplicate releases. Treat exclusions for already-rated or previously heard albums as explicit preferences, since a canvas album is not necessarily liked or even heard.
- Apply popularity as a ranking preference among relevant candidates, not as a replacement for relevance. Test moderate popularity as a target range rather than a weakened preference for popular albums.
- Select and validate a permitted album-level popularity source before enabling this control. Record the signal definition, source, timestamp, coverage, and missing values. Artist popularity must not silently stand in for album popularity, and missing data must not be interpreted as obscurity.
- Explain measured popularity in accessible language once the source is chosen. Until a reliable signal is available, keep the control unavailable with a brief explanation; prototype values must be labeled as illustrative.
- Save the seed IDs, group revision, settings, and model/data versions for each recommendation run so results and explanations can be reproduced.
- Preserve separate events for group membership, recommendation requests, saves, dismissals, and ratings. Group membership is search context, not an implicit positive training label.

### First-release acceptance criteria

A new user can search, add albums to the sandbox, form a group, and request recommendations without first rating albums. 
Group edits are undoable, loading and errors are visible, and stale results are clearly identified. Recommendation validation measures seed-group 
relevance and whether popularity settings shift the measured popularity distribution while retaining relevance. 
Usability testing checks that people understand grouping, the distinction between popularity and similarity, and whether adding an album changes their taste profile.

---

## Phase 0 — Define the product and success criteria

### Objective

Define what Crate is solving before selecting detailed implementations.

### Steps

1. Define the core user journey:
   - Open the blank sandbox and search for albums.
   - Drag or add albums onto the canvas.
   - Select albums and create a visual group.
   - Choose a popularity preference and request recommendations for the group.
   - Inspect recommendations with explanations and add interesting results to a group or save them.
   - Create an account to retain work across devices; do not require registration before initial exploration.
   - Optionally rate albums from 0–5 stars and add descriptive words or a short reflection.
   - Rate, save, or dismiss recommendations.
2. Document the product philosophy:
   - Deliberate grouping and optional ratings instead of passive listening surveillance.
   - Meaningful discovery instead of engagement maximization.
   - User-visible explanations.
   - User control over recommendation direction.
3. Define the initial recommendation modes:
   - Based on a user-created album group, including a single-album group.
   - Popularity-directed discovery within that group's context.
   - Later: optional full-profile personalization and exploration controls.
4. Establish success metrics:
   - Recall@K and NDCG@K.
   - Catalog coverage.
   - Diversity and novelty.
   - Recommendation acceptance and subsequent ratings.
   - API latency and failure rate.
5. Write the initial product requirements and system design.

### Completion criterion

The first release boundary, data requirements, evaluation protocol, and product goals are documented.

---

## Phase 1 — Build the application foundation

### Objective

Create a usable application before introducing machine learning.

### Steps

1. Establish the repository structure:

   ```text
   crate/
   ├── frontend/
   ├── backend/
   ├── pipelines/
   ├── models/
   ├── infrastructure/
   ├── tests/
   └── docs/
   ```

2. Build the backend with FastAPI.
3. Create the PostgreSQL database.
4. Design initial tables for users, artists, albums, workspaces, canvas album instances, album-groups, group-album memberships (with user_id denormalized), per-group settings, ratings, descriptors, recommendation runs, recommendations, events, and model versions.
5. Build the frontend with React or SvelteKit.
6. Implement authentication.
7. Implement album search against a small local dataset.
8. Implement the album canvas, explicit grouping, keyboard/button alternatives, workspace persistence, and group recommendation panel. Add optional rating and taste-profile interfaces after the primary workflow works.
9. Add unit and API integration tests.
10. Containerize the application with Docker Compose.

### Completion criterion

A user can run Crate locally, search for albums, arrange them in a sandbox, create and save groups, and request a group's recommendations through a placeholder service. Optional ratings do not block this workflow; real recommendations arrive in Phase 3.

---

## Phase 2 — Build the MusicBrainz data pipeline

### Objective

Create a reproducible source of canonical album and artist data.

### Steps

1. Learn the MusicBrainz entity model: artist, release group, release, recording, work, label, and relationship.
2. Use release-group MBIDs as canonical external album identifiers.
3. Build a small API ingestion prototype.
4. Implement rate limiting, retries, exponential backoff, caching, and response validation.
5. Select an initial catalog of approximately 10,000–25,000 albums.
6. Normalize MusicBrainz records into Crate's schema.
7. Import artists, dates, genres, tags, labels, credits, instruments, relationships, and external identifiers.
8. Integrate the Cover Art Archive.
9. Add tests for duplicate identifiers, orphan relationships, missing artists, invalid dates, and metadata coverage.
10. Record source and licensing provenance.

### Completion criterion

Crate has a normalized, searchable music catalog with stable identifiers and a repeatable ingestion process.

**Status:** Complete as of 2026-09-23 — 25,000 albums ingested from the 2026-09-23 MusicBrainz snapshot (replication sequence 189205), replacing the 141-album seed catalog. Per-album credits, labels, and tracklists are deferred because the `release` dump is out of scope; see `docs/superpowers/specs/2026-09-20-musicbrainz-ingestion-design.md`.

---

## Phase 3 — Build non-ML recommendation baselines

### Objective

Create simple, explainable systems that trained models must outperform.

### Steps

1. Validate a permitted album-level popularity signal and implement a global popularity baseline. Handle unknown popularity explicitly.
2. Implement genre-overlap and tag-overlap recommendations.
3. Build graph features from shared musicians, producers, labels, instruments, and artist relationships.
4. Combine signals using manually selected weights.
5. Exclude seed albums, duplicate releases, and reissues of the same release group. Support explicit exclusions for rated or previously heard albums.
6. Add diversity across artists, genres, labels, and eras.
7. Generate deterministic explanations based on actual shared features.
8. Build a manually reviewed evaluation set covering diverse seed albums.
9. Aggregate evidence across multiple group seeds with equal initial influence and compare against single-seed recommendations.
10. Implement and evaluate lesser-known, moderate, widely popular, and no-preference settings while preserving relevance.

### Completion criterion

A group containing one or more albums produces useful, explainable recommendations without a trained model or required ratings. Popularity preferences measurably steer results where signal coverage supports them.

**Status:** Thin version complete as of 2026-09-24. Phase 3 was deliberately cut down to a single baseline so the project reaches ML work (Phase 4) sooner. The completion criterion above is only partly met: recommendations are explainable, but popularity steering is not built and nothing has been evaluated yet.

- **Done:**
  - Step 2: genre/tag overlap, scored with Jaccard similarity.
  - Step 5: seed albums are excluded.
  - Step 7: deterministic shared-term explanations.
  - Step 9, partly: seeds in a group have equal influence, but results are not yet compared against single-seed recommendations.
  - All of this is exposed as `POST /recommendations` and wired into the group panel.
- **Step 1, partly:** Last.fm listener counts were chosen as the popularity signal, and a backfill script exists. Coverage hasn't been measured yet, Last.fm's API terms haven't been reviewed for this use, and no popularity baseline has been built.
- **Deferred:**
  - Step 3: shared-musician and producer graph features. Blocked by the missing per-album credits from Phase 2.
  - Step 4: hand-weighted signal combination.
  - Step 5, partly: explicit exclusions for rated or already-heard albums.
  - Step 6: diversity.
  - Step 8: a hand-reviewed evaluation set. Needed before Phase 4 results can be compared with this baseline.
  - Step 10: popularity settings. The UI shows these options disabled.

Details, known limitations, and measured latency are in `docs/recommendation-systems.md`. The design is in `docs/superpowers/specs/2026-09-24-overlap-baseline-recommender-design.md`.

---

## Phase 4 — Build the scikit-learn textual recommender

### Objective

Introduce classical NLP and information retrieval.

### Steps

1. Construct a structured text document for each album using genres, tags, credits, instruments, labels, annotations, and permitted descriptive text.
2. Normalize text while preserving meaningful musical phrases.
3. Build a TF-IDF model with scikit-learn.
4. Compare unigrams, bigrams, source weights, minimum document frequencies, and truncated SVD.
5. Calculate cosine similarity between album documents.
6. Precompute nearest neighbors for each album.
7. Combine textual similarity with graph features.
8. Use Maximal Marginal Relevance or a similar method to diversify results.
9. Extract shared descriptive terms for explanations.
10. Compare results against popularity, tag, genre, and graph-only baselines.

### Completion criterion

The textual recommender measurably improves on simpler baselines and produces intelligible explanations.

---

## Phase 5 — Build the PyTorch semantic recommender

### Objective

Learn similarities in meaning rather than requiring exact shared words.

### Steps

1. Select a pretrained text-embedding model.
2. Generate album-document embeddings.
3. Version each embedding by album document, encoder, data snapshot, and creation time.
4. Store and retrieve embeddings using PostgreSQL and `pgvector`.
5. Compare semantic retrieval against TF-IDF quantitatively and manually.
6. Build a PyTorch projection model combining text embeddings with genres, labels, years, personnel, and graph features.
7. Implement negative sampling and a suitable ranking or metric-learning objective.
8. Track runs, parameters, metrics, artifacts, and model lineage with MLflow.
9. Register the strongest validated model.

### Completion criterion

Crate finds culturally related albums whose descriptions express similar ideas using different vocabulary.

---

## Phase 6 — Build personalized taste modeling

### Objective

Move from album similarity to user-specific recommendation.

### Steps

1. Initialize a new user profile from rated-album embeddings.
2. Convert ratings into positive, neutral, and negative preference weights.
3. Build a weighted user representation.
4. Prevent popular albums from dominating the profile.
5. Detect multiple taste clusters rather than averaging incompatible interests together.
6. Learn which descriptive concepts appear most predictive for each user.
7. Add personalized ranking features including cluster similarity, distance from disliked albums, novelty, diversity, and confidence.
8. Build a PyTorch ranking model.
9. Compare learned and manually weighted rankers.
10. Add controls for safer, more exploratory, cluster-specific, era-specific, or genre-excluding recommendations.
11. Keep the selected group as the primary context; make broader taste-profile influence an explicit opt-in rather than silently overriding group intent.

### Completion criterion

Users with overlapping ratings but different broader profiles or descriptions receive meaningfully different recommendations.

---

## Phase 7 — Add collaborative filtering

### Objective

Discover relationships that metadata and language do not express directly.

### Steps

1. Collect sufficient real or appropriately licensed rating data.
2. Implement matrix factorization in PyTorch.
3. Add user embeddings, album embeddings, biases, regularization, batching, validation, and early stopping.
4. Compare rating-prediction and ranking objectives.
5. Evaluate cold-start and established-user performance separately.
6. Generate collaborative candidates from patterns in deliberate ratings.
7. Combine collaborative, textual, and graph representations.
8. Train a two-stage candidate-generation and ranking system.
9. Measure and mitigate popularity feedback loops.
10. Report performance separately for popular and long-tail albums.

### Completion criterion

The hybrid model outperforms text-only and collaborative-only systems without sacrificing cold-start quality.

---

## Phase 8 — Create the scalable data platform

### Objective

Expand from a small catalog to hundreds of thousands or millions of albums without making the application slow.

### Steps

1. Create raw, cleaned, feature, and model-ready layers in AWS S3.
2. Store analytical tables in Parquet.
3. Partition event data by date and source.
4. Implement incremental processing using timestamps, content hashes, pipeline versions, and idempotent writes.
5. Reimplement justified transformations in PySpark.
6. Preserve a local Polars or pandas implementation.
7. Benchmark processing time, memory, storage, and cost.
8. Orchestrate ingestion, validation, document construction, embedding, evaluation, and training with Prefect or Airflow.
9. Create immutable dataset snapshots.
10. Optionally demonstrate compatible jobs on Databricks.

### Completion criterion

The training dataset can be reproduced, and routine jobs process only new or changed records.

---

## Phase 9 — Productionize on AWS

### Objective

Deploy a reliable public application and repeatable infrastructure.

### Steps

1. Define infrastructure using Terraform.
2. Deploy FastAPI on ECS/Fargate, PostgreSQL on RDS, and data/model artifacts in S3.
3. Deploy the frontend through appropriate static hosting.
4. Store secrets securely and configure IAM, HTTPS, and network boundaries.
5. Build CI/CD with GitHub Actions.
6. Gate deployments with unit, integration, migration, data-quality, model-behavior, and security checks.
7. Deploy models by immutable version.
8. Add canary or shadow evaluation.
9. Implement application and model rollback.
10. Load-test the service and report throughput, tail latency, failures, and cost per thousand recommendations.

### Completion criterion

Crate is publicly accessible, reproducibly deployed, secure, observable, and capable of rolling back faulty releases.

---

## Phase 10 — Add observability and continuous learning

### Objective

Determine whether the deployed service and recommendation models remain healthy and useful.

### Steps

1. Record recommendation impressions with candidate, rank, score, model version, user, and timestamp.
2. Record opens, dismissals, saves, `already heard` responses, and ratings.
3. Monitor latency, errors, database health, worker failures, and pipeline duration.
4. Monitor feature availability, embedding drift, catalog coverage, popularity concentration, and diversity.
5. Create dashboards and alerts.
6. Establish retraining triggers.
7. Add Kafka or Kinesis when multiple independent event consumers justify streaming infrastructure.
8. Run controlled model comparisons or A/B tests.
9. Evaluate performance by user maturity, popularity, genre, era, and catalog region.
10. Document a simulated incident and recovery.

### Completion criterion

The team can identify unhealthy models, trace every recommendation to a model version, and recover from production failures.

---

## Phase 11 — Recruit users and validate the product

### Objective

Turn the technical system into real-world evidence.

### Steps

1. Recruit the first 10 test users.
2. Observe onboarding, search, canvas arrangement, grouping, recommendation controls, optional rating, and explanation problems, including workflows without dragging.
3. Improve the cold-start experience.
4. Expand toward 50–100 genuine users.
5. Collect several thousand deliberate ratings and descriptors.
6. Interview users about relevance, discovery, bad recommendations, and explanation usefulness.
7. Analyze individual failure cases alongside aggregate metrics.
8. Retrain and compare model versions.
9. Publish anonymized aggregate statistics.
10. Maintain a changelog showing how evidence affected development decisions.

### Completion criterion

Crate has real users, real feedback, measurable improvements, and documented product decisions.

---

## Phase 12 — Package Crate as an MLE portfolio centerpiece

### Objective

Make the project's engineering evidence easy for employers to assess.

### Steps

1. Write a polished README covering the problem, live demo, architecture, setup, model results, and production metrics.
2. Publish a technical case study documenting baselines, experiments, failures, tradeoffs, costs, and outcomes.
3. Create architecture and data-flow diagrams.
4. Publish an ML evaluation report.
5. Record a three-to-five-minute demonstration.
6. Publish model cards and data cards.
7. Expose representative tests and CI results.
8. Document licensing and data provenance.
9. Prepare interview explanations for cold start, ranking metrics, leakage, deployment, monitoring, scalability, and cost.
10. Write targeted resume bullets containing measured results.

### Completion criterion

A hiring manager can understand the product, inspect its ML methodology, run the repository, and verify production evidence without an initial explanation from its creator.

---

## Optional Intel-focused extension

After the main product works:

1. Export the PyTorch ranker to ONNX.
2. Create a C++ inference service with ONNX Runtime.
3. Benchmark it against Python inference.
4. Measure memory, throughput, and tail latency.
5. Experiment with quantization.
6. Profile CPU and GPU execution.

This extension is valuable for Intel and ML-infrastructure roles, but it should not delay the central product.

## Recommended milestone sequence

```text
Working application
→ explainable baseline
→ semantic recommender
→ personalization
→ hybrid collaborative model
→ scalable data pipeline
→ public production system
→ real-user evidence
```

Job applications do not need to wait until the final phase. By the end of Phase 6, Crate can already demonstrate meaningful machine learning engineering. Phases 7–10 strengthen the project into evidence that its creator can operate a real ML product, while Phases 11–12 convert that engineering work into a compelling portfolio case study.

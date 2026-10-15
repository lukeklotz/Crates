# Catalog search: case-insensitive substring matching

## What this method does

Catalog search helps a listener find a **known album or artist** to place on the canvas. It is separate from the recommendation methods, which find related albums from a group of seeds. The browser sends a submitted query to `/api/search`; that route forwards it to the backend's `GET /albums/search` endpoint. The backend trims surrounding spaces, looks for the query anywhere in an album title **or** artist name, sorts matching albums by title, and returns at most 24. The comparison is case-insensitive.

The key operation in [`albums.py`](../../backend/src/crate_backend/api/routes/albums.py) is:

```python
pattern = f"%{term}%"
stmt = (
    select(Album)
    .where(Album.title.ilike(pattern) | Album.artist_name.ilike(pattern))
    .order_by(Album.title)
    .limit(MAX_RESULTS)
)
```

`%` means “any characters before or after,” and PostgreSQL `ILIKE` makes the match case-insensitive. The frontend submits the search on form submission; it does not run a ranking model or use the recommendation approach selector.

## Analogy and ELI5 example

Imagine looking through a shelf of album cards with a highlighter. You highlight a card if the typed letters appear anywhere in its album title or artist name. Then you alphabetize the highlighted cards by album title and show the first 24.

For example, searching `coltrane` can find albums whose artist field contains “John Coltrane,” even if `coltrane` is absent from the title. Searching `love` can find an album with “Love” in its title. A misspelling such as `coltrain` will not match `Coltrane`: this is literal substring matching, not fuzzy search.

## Why this technique was chosen

The product needs a direct way for users to locate an album before creating a group. A simple database query is easy to implement, easy to explain, and works without training data or a prebuilt search index. This is the right baseline for a catalog of roughly 25,000 albums and a known-item workflow. The project plan calls for album search as the first step in discovery; it does not record a separate comparison of search algorithms.

## Tradeoffs

- **Strengths:** Predictable results; case-insensitive; matches both title and artist; returns a small, bounded list. New catalog records are searchable immediately after ingestion.
- **Limitations:** No spelling correction, stemming, synonym handling, or relevance ranking. A short query can match many albums, while only the first 24 alphabetically appear. An exact title match receives no special priority over a weak substring match. Because the pattern begins with `%`, a conventional prefix index alone cannot satisfy this search efficiently at much larger catalog sizes.
- **What it is for:** Finding a name the user already has in mind. It does not infer taste or recommend musically related albums.

## Source pointers

- [`backend/src/crate_backend/api/routes/albums.py`](../../backend/src/crate_backend/api/routes/albums.py), lines 18–55: query, ordering, and limit.
- [`frontend/app/api/search/route.ts`](../../frontend/app/api/search/route.ts), lines 3–23: browser-facing proxy.
- [`frontend/app/page.tsx`](../../frontend/app/page.tsx), lines 236–257: submitted-query behavior.

"""Record each catalog album's Wikidata id and English Wikipedia title from
the MusicBrainz release-group dump (Phase 4, Milestone 1).

Design: docs/superpowers/specs/2026-09-26-tfidf-text-recommender-design.md

Run with: uv run python -m crate_backend.scripts.link_wikidata

Safe to re-run: every catalog album's two link columns are overwritten
from the dump, so links removed upstream are cleared too.
"""

import asyncio
from pathlib import Path

from sqlalchemy import select

from crate_backend.core.config import get_settings
from crate_backend.db.session import async_session_factory
from crate_backend.models.catalog import Album
from crate_backend.musicbrainz.dump_reader import stream_jsonl_from_tar
from crate_backend.wikipedia.links import WikiLinks, parse_wiki_links

_NO_LINKS = WikiLinks()


def _percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.1f}%" if whole else "n/a"


async def link_albums(dump_dir: Path) -> None:
    async with async_session_factory() as session:
        albums = (
            await session.scalars(
                select(Album).where(Album.musicbrainz_release_group_id.is_not(None))
            )
        ).all()
        by_mbid = {album.musicbrainz_release_group_id: album for album in albums}
        print(
            f"Scanning release groups for links to {len(by_mbid)} catalog albums "
            "(streams the whole dump; takes several minutes)..."
        )

        links: dict[str, WikiLinks] = {}
        for record in stream_jsonl_from_tar(
            dump_dir / "release-group.tar.xz", "mbdump/release-group"
        ):
            if record.get("id") in by_mbid:
                links[record["id"]] = parse_wiki_links(record)

        for mbid, album in by_mbid.items():
            found = links.get(mbid, _NO_LINKS)
            album.wikidata_id = found.wikidata_id
            album.wikipedia_title = found.wikipedia_title
        await session.commit()

    total = len(by_mbid)
    wikidata = sum(1 for found in links.values() if found.wikidata_id)
    enwiki = sum(1 for found in links.values() if found.wikipedia_title)
    either = sum(1 for found in links.values() if found.wikidata_id or found.wikipedia_title)
    print(
        f"Linked {total} albums: Wikidata {wikidata}, English Wikipedia {enwiki}, "
        f"either {either} ({_percent(either, total)}); "
        f"{total - len(links)} not found in the dump."
    )


def main() -> None:
    asyncio.run(link_albums(Path(get_settings().musicbrainz_dump_dir)))


if __name__ == "__main__":
    main()

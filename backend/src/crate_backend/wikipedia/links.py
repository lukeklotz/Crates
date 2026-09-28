"""Read Wikidata and English Wikipedia links from a MusicBrainz
release-group record's URL relations."""

import re
from typing import Any, NamedTuple
from urllib.parse import unquote, urlsplit

_QID_PATH = re.compile(r"^/(?:wiki|entity)/(Q\d+)$")
_ENWIKI_HOSTS = frozenset({"en.wikipedia.org", "en.m.wikipedia.org"})
_WIKI_PATH_PREFIX = "/wiki/"
# Album.wikipedia_title's column length.
_MAX_TITLE_LENGTH = 500


class WikiLinks(NamedTuple):
    wikidata_id: str | None = None
    wikipedia_title: str | None = None


def _wikidata_id(url: str) -> str | None:
    match = _QID_PATH.match(urlsplit(url).path)
    return match.group(1) if match else None


def _enwiki_title(url: str) -> str | None:
    """The article title from an English Wikipedia URL, percent-decoded with
    underscores kept (the API accepts them). urlsplit drops ?query and
    #fragment from the path."""
    parts = urlsplit(url)
    if parts.hostname not in _ENWIKI_HOSTS or not parts.path.startswith(_WIKI_PATH_PREFIX):
        return None
    title = unquote(parts.path[len(_WIKI_PATH_PREFIX) :])
    if not title or len(title) > _MAX_TITLE_LENGTH:
        return None
    return title


def parse_wiki_links(record: dict[str, Any]) -> WikiLinks:
    """The first Wikidata id and first English Wikipedia title among the
    record's relations. Non-English Wikipedia links are ignored."""
    wikidata_id = wikipedia_title = None
    for relation in record.get("relations") or []:
        url = (relation.get("url") or {}).get("resource")
        if not isinstance(url, str):
            continue
        if relation.get("type") == "wikidata" and wikidata_id is None:
            wikidata_id = _wikidata_id(url)
        elif relation.get("type") == "wikipedia" and wikipedia_title is None:
            wikipedia_title = _enwiki_title(url)
    return WikiLinks(wikidata_id, wikipedia_title)

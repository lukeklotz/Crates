from crate_backend.wikipedia.links import WikiLinks, parse_wiki_links


def _relation(rel_type: str, url: str) -> dict:
    return {"type": rel_type, "target-type": "url", "url": {"id": "x", "resource": url}}


def _record(*relations: dict) -> dict:
    return {"id": "test-rg", "relations": list(relations)}


def test_wikidata_relation_gives_the_q_id():
    links = parse_wiki_links(
        _record(_relation("wikidata", "https://www.wikidata.org/wiki/Q24965303"))
    )
    assert links == WikiLinks(wikidata_id="Q24965303", wikipedia_title=None)


def test_english_wikipedia_relation_gives_the_title_with_underscores_kept():
    links = parse_wiki_links(
        _record(_relation("wikipedia", "https://en.wikipedia.org/wiki/Kid_A"))
    )
    assert links == WikiLinks(wikidata_id=None, wikipedia_title="Kid_A")


def test_both_relations_are_read():
    links = parse_wiki_links(
        _record(
            _relation("wikidata", "https://www.wikidata.org/wiki/Q1"),
            _relation("wikipedia", "https://en.wikipedia.org/wiki/Kid_A"),
        )
    )
    assert links == WikiLinks("Q1", "Kid_A")


def test_non_english_wikipedia_is_ignored():
    links = parse_wiki_links(
        _record(_relation("wikipedia", "https://de.wikipedia.org/wiki/Mittendrin_(Album)"))
    )
    assert links == WikiLinks()


def test_english_link_after_a_non_english_one_is_still_found():
    links = parse_wiki_links(
        _record(
            _relation("wikipedia", "https://de.wikipedia.org/wiki/Kid_A"),
            _relation("wikipedia", "https://en.wikipedia.org/wiki/Kid_A"),
        )
    )
    assert links.wikipedia_title == "Kid_A"


def test_percent_encoding_is_decoded():
    links = parse_wiki_links(
        _record(
            _relation(
                "wikipedia",
                "https://en.wikipedia.org/wiki/Sgt._Pepper%27s_Lonely_Hearts_Club_Band",
            )
        )
    )
    assert links.wikipedia_title == "Sgt._Pepper's_Lonely_Hearts_Club_Band"


def test_fragment_and_query_are_dropped():
    links = parse_wiki_links(
        _record(_relation("wikipedia", "https://en.wikipedia.org/wiki/Kid_A?x=1#Reception"))
    )
    assert links.wikipedia_title == "Kid_A"


def test_mobile_host_and_http_scheme_are_accepted():
    links = parse_wiki_links(
        _record(_relation("wikipedia", "http://en.m.wikipedia.org/wiki/Kid_A"))
    )
    assert links.wikipedia_title == "Kid_A"


def test_wikidata_entity_url_form_is_accepted():
    links = parse_wiki_links(_record(_relation("wikidata", "http://www.wikidata.org/entity/Q42")))
    assert links.wikidata_id == "Q42"


def test_malformed_wikidata_url_gives_no_id():
    links = parse_wiki_links(
        _record(_relation("wikidata", "https://www.wikidata.org/wiki/Special:Search"))
    )
    assert links == WikiLinks()


def test_other_relation_types_are_ignored():
    links = parse_wiki_links(_record(_relation("discogs", "https://www.discogs.com/master/1")))
    assert links == WikiLinks()


def test_no_relations_or_null_relations():
    assert parse_wiki_links({"id": "test-rg"}) == WikiLinks()
    assert parse_wiki_links({"id": "test-rg", "relations": None}) == WikiLinks()


def test_relation_without_a_url_is_skipped():
    assert parse_wiki_links(_record({"type": "wikidata", "target-type": "url"})) == WikiLinks()


def test_title_longer_than_the_column_is_dropped():
    long_title = "A" * 501
    links = parse_wiki_links(
        _record(_relation("wikipedia", f"https://en.wikipedia.org/wiki/{long_title}"))
    )
    assert links.wikipedia_title is None

import httpx
import pytest

from crate_backend.wikipedia import client


@pytest.fixture
def sleeps(monkeypatch) -> list[float]:
    recorded: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(client, "_sleep", fake_sleep)
    return recorded


def _client(responses: list) -> tuple[httpx.AsyncClient, list[httpx.Request]]:
    """Client whose transport returns (or raises) `responses` in order,
    repeating the last one."""
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        item = responses[min(len(requests), len(responses)) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requests


def _entity(qid: str, title: str | None) -> dict:
    sitelinks = {"enwiki": {"site": "enwiki", "title": title, "badges": []}} if title else {}
    return {"type": "item", "id": qid, "sitelinks": sitelinks}


def _entities(*entities: dict) -> httpx.Response:
    return httpx.Response(200, json={"entities": {e["id"]: e for e in entities}, "success": 1})


def _page(
    title: str = "Kid A",
    extract: str = "Kid A is an album.\n\n\n== Background ==\nText.",
    revision: int = 1376615480,
    redirects: list | None = None,
) -> httpx.Response:
    query: dict = {
        "pages": [
            {"pageid": 170770, "ns": 0, "title": title, "lastrevid": revision, "extract": extract}
        ]
    }
    if redirects is not None:
        query["redirects"] = redirects
    return httpx.Response(200, json={"batchcomplete": True, "query": query})


def _pages(*pages: dict) -> httpx.Response:
    return httpx.Response(200, json={"batchcomplete": True, "query": {"pages": list(pages)}})


# --- user agent -------------------------------------------------------------


def test_user_agent_names_the_client_and_contact():
    agent = client.user_agent("someone@example.test")
    assert agent.startswith("CrateBackend/")
    assert "someone@example.test" in agent


# --- resolve_enwiki_titles ---------------------------------------------------


async def test_resolves_english_titles_and_sends_one_batched_request(sleeps):
    ac, requests = _client([_entities(_entity("Q1", "Kid A"), _entity("Q2", "OK Computer"))])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1", "Q2"])
    assert titles == {"Q1": "Kid A", "Q2": "OK Computer"}
    assert len(requests) == 1
    params = requests[0].url.params
    assert params["action"] == "wbgetentities"
    assert params["ids"] == "Q1|Q2"
    assert params["props"] == "sitelinks"
    assert params["sitefilter"] == "enwiki"
    assert str(requests[0].url).startswith(client.WIKIDATA_API_URL)


async def test_item_without_english_sitelink_is_none(sleeps):
    ac, _ = _client([_entities(_entity("Q15074489", None))])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q15074489"])
    assert titles == {"Q15074489": None}


async def test_deleted_item_in_a_batch_is_none(sleeps):
    ac, _ = _client([_entities(_entity("Q1", "Kid A"), {"id": "Q3", "missing": ""})])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1", "Q3"])
    assert titles == {"Q1": "Kid A", "Q3": None}


async def test_unknown_id_is_answered_none_and_the_rest_are_asked_again(sleeps):
    no_such = httpx.Response(
        200,
        json={
            "error": {
                "code": "no-such-entity",
                "id": "Q999999999999",
                "info": "Could not find an entity",
            }
        },
    )
    ac, requests = _client([no_such, _entities(_entity("Q1", "Kid A"))])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1", "Q999999999999"])
    assert titles == {"Q1": "Kid A", "Q999999999999": None}
    assert requests[1].url.params["ids"] == "Q1"
    assert sleeps == []


async def test_redirected_item_is_answered_under_the_requested_id(sleeps):
    merged = {**_entity("Q20", "Kid A"), "redirects": {"from": "Q10", "to": "Q20"}}
    ac, _ = _client([httpx.Response(200, json={"entities": {"Q20": merged}, "success": 1})])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q10"])
    assert titles == {"Q10": "Kid A"}


async def test_requested_id_absent_from_a_good_response_is_left_unresolved(sleeps):
    # Unexplained silence is not a definitive "no article": retry it next run.
    ac, _ = _client([_entities(_entity("Q1", "Kid A"))])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1", "Q2"])
    assert titles == {"Q1": "Kid A"}


async def test_resolve_retries_503_then_succeeds(sleeps):
    ac, _ = _client([httpx.Response(503), _entities(_entity("Q1", "Kid A"))])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1"])
    assert titles == {"Q1": "Kid A"}
    assert sleeps == [1.0]


async def test_resolve_gives_up_with_every_id_unresolved(sleeps):
    ac, requests = _client([httpx.Response(503)])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1", "Q2"])
    assert titles == {}
    assert len(requests) == client.MAX_RETRIES + 1
    assert sleeps == [1.0, 2.0, 4.0, 8.0, 16.0]


async def test_other_api_error_leaves_ids_unresolved(sleeps):
    ac, _ = _client(
        [httpx.Response(200, json={"error": {"code": "ratelimited", "info": "slow down"}})]
    )
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1"])
    assert titles == {}


async def test_html_maintenance_page_leaves_ids_unresolved(sleeps):
    ac, _ = _client([httpx.Response(200, text="<html>maintenance</html>")])
    async with ac:
        titles = await client.resolve_enwiki_titles(ac, ["Q1"])
    assert titles == {}


async def test_more_than_fifty_ids_is_rejected(sleeps):
    ac, requests = _client([_entities()])
    async with ac:
        with pytest.raises(ValueError):
            await client.resolve_enwiki_titles(ac, [f"Q{i}" for i in range(51)])
    assert requests == []


# --- fetch_article -----------------------------------------------------------


async def test_found_article_returns_text_title_and_revision(sleeps):
    ac, requests = _client([_page()])
    async with ac:
        result = await client.fetch_article(ac, "Kid_A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.title == "Kid A"
    assert result.revision_id == 1376615480
    assert result.text.startswith("Kid A is an album.")
    assert "== Background ==" in result.text
    assert result.redirected is False
    params = requests[0].url.params
    assert params["titles"] == "Kid_A"
    assert params["prop"] == "extracts|info"
    assert params["explaintext"] == "1"
    assert params["redirects"] == "1"
    assert params["formatversion"] == "2"
    assert str(requests[0].url).startswith(client.WIKIPEDIA_API_URL)


async def test_followed_redirect_is_reported_with_the_final_title(sleeps):
    ac, _ = _client([_page(title="Foobar", redirects=[{"from": "Foo", "to": "Foobar"}])])
    async with ac:
        result = await client.fetch_article(ac, "Foo")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.title == "Foobar"
    assert result.redirected is True


async def test_missing_page_is_missing(sleeps):
    ac, requests = _client([_pages({"ns": 0, "title": "Zzzz no such album qqq", "missing": True})])
    async with ac:
        result = await client.fetch_article(ac, "Zzzz_no_such_album_qqq")
    assert result.outcome is client.FetchOutcome.MISSING
    assert len(requests) == 1


async def test_invalid_title_is_missing(sleeps):
    ac, _ = _client(
        [_pages({"title": "Bar[", "invalid": True, "invalidreason": "invalid characters"})]
    )
    async with ac:
        result = await client.fetch_article(ac, "Bar[")
    assert result.outcome is client.FetchOutcome.MISSING


async def test_blank_extract_is_found_with_no_text(sleeps):
    ac, _ = _client([_page(extract="  \n")])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.text is None


async def test_page_without_an_extract_is_found_with_no_text(sleeps):
    ac, _ = _client([_pages({"pageid": 1, "ns": 0, "title": "Kid A", "lastrevid": 5})])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.text is None
    assert result.revision_id == 5


async def test_article_429_is_retried(sleeps):
    ac, requests = _client([httpx.Response(429), _page()])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert len(requests) == 2


async def test_article_network_error_is_retried(sleeps):
    ac, _ = _client([httpx.ConnectError("connection reset"), _page()])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND


async def test_article_gives_up_as_failed(sleeps):
    ac, requests = _client([httpx.Response(502)])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED
    assert len(requests) == client.MAX_RETRIES + 1


async def test_backoff_is_capped(monkeypatch, sleeps):
    monkeypatch.setattr(client, "MAX_RETRIES", 8)
    ac, _ = _client([httpx.Response(503)])
    async with ac:
        await client.fetch_article(ac, "Kid A")
    assert max(sleeps) == client.MAX_BACKOFF_SECONDS


async def test_html_maintenance_page_is_failed_not_missing(sleeps):
    ac, _ = _client([httpx.Response(200, text="<html>maintenance</html>")])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED


async def test_forbidden_is_failed_not_missing(sleeps):
    # Wikimedia answers 403 to clients whose User-Agent breaks its policy.
    ac, requests = _client([httpx.Response(403, text="Please set a user-agent")])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED
    assert len(requests) == 1


async def test_unexpected_json_shape_is_failed(sleeps):
    ac, _ = _client([httpx.Response(200, json={"batchcomplete": True})])
    async with ac:
        result = await client.fetch_article(ac, "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED

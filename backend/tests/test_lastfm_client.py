import httpx
import pytest

from crate_backend.lastfm import client

pytestmark = pytest.mark.asyncio


@pytest.fixture
def sleeps(monkeypatch) -> list[float]:
    recorded: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(client, "_sleep", fake_sleep)
    return recorded


def _client(responses: list) -> tuple[httpx.AsyncClient, list[httpx.Request]]:
    """Client whose transport returns (or raises) `responses` in order."""
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        item = responses[min(len(requests), len(responses)) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requests


def _found_response(listeners: int = 12345, artist: str = "Radiohead", title: str = "Kid A"):
    return httpx.Response(
        200, json={"album": {"name": title, "artist": artist, "listeners": str(listeners)}}
    )


async def test_found_album_returns_listeners_artist_and_title(sleeps):
    ac, requests = _client([_found_response(listeners=999)])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert result.listeners == 999
    assert result.artist == "Radiohead"
    assert result.title == "Kid A"
    params = requests[0].url.params
    assert params["method"] == "album.getinfo"
    assert params["api_key"] == "test-key"
    assert params["artist"] == "Radiohead"
    assert params["album"] == "Kid A"


async def test_album_not_found_error_means_not_found_without_retrying(sleeps):
    ac, requests = _client([httpx.Response(404, json={"error": 6, "message": "Album not found"})])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Nobody", "Nothing")
    assert result.outcome is client.FetchOutcome.NOT_FOUND
    assert len(requests) == 1


async def test_404_status_means_not_found_without_retrying(sleeps):
    ac, requests = _client([httpx.Response(404)])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Nobody", "Nothing")
    assert result.outcome is client.FetchOutcome.NOT_FOUND
    assert len(requests) == 1


async def test_non_numeric_listeners_means_not_found(sleeps):
    ac, _ = _client(
        [httpx.Response(200, json={"album": {"name": "Kid A", "artist": "Radiohead", "listeners": "n/a"}})]
    )
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.NOT_FOUND


async def test_429_retries_with_backoff_then_succeeds(sleeps):
    ac, requests = _client([httpx.Response(429), httpx.Response(429), _found_response()])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert len(requests) == 3
    assert sleeps == [1.0, 2.0]


async def test_network_error_is_retried(sleeps):
    ac, _ = _client([httpx.ConnectError("connection reset"), _found_response()])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND


async def test_gives_up_after_max_retries_and_reports_failed(sleeps):
    ac, requests = _client([httpx.Response(503)])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED
    assert len(requests) == client.MAX_RETRIES + 1
    assert sleeps == [1.0, 2.0, 4.0, 8.0, 16.0]


async def test_backoff_is_capped(monkeypatch, sleeps):
    monkeypatch.setattr(client, "MAX_RETRIES", 8)
    ac, _ = _client([httpx.Response(503)])
    async with ac:
        await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert max(sleeps) == client.MAX_BACKOFF_SECONDS


async def test_invalid_api_key_raises_instead_of_recording_no_match(sleeps):
    ac, requests = _client([httpx.Response(403, json={"error": 10, "message": "Invalid API key"})])
    async with ac:
        with pytest.raises(client.LastfmKeyRejected):
            await client.fetch_album_info(ac, "bad-key", "Radiohead", "Kid A")
    assert len(requests) == 1


async def test_suspended_api_key_in_a_200_body_raises(sleeps):
    ac, _ = _client([httpx.Response(200, json={"error": 26, "message": "Suspended API key"})])
    async with ac:
        with pytest.raises(client.LastfmKeyRejected):
            await client.fetch_album_info(ac, "bad-key", "Radiohead", "Kid A")


async def test_temporary_error_body_is_retried(sleeps):
    ac, requests = _client(
        [httpx.Response(200, json={"error": 16, "message": "Temporary error"}), _found_response()]
    )
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FOUND
    assert len(requests) == 2
    assert sleeps == [1.0]


async def test_rate_limit_error_body_gives_up_as_failed(sleeps):
    ac, _ = _client([httpx.Response(200, json={"error": 29, "message": "Rate limit exceeded"})])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED


async def test_unrecognized_body_is_failed_not_a_definitive_no_match(sleeps):
    ac, _ = _client([httpx.Response(200, json={})])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED


async def test_non_json_body_is_failed_not_a_definitive_no_match(sleeps):
    ac, _ = _client([httpx.Response(200, text="<html>maintenance</html>")])
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.FAILED


async def test_non_string_artist_is_not_found_instead_of_crashing(sleeps):
    ac, _ = _client(
        [httpx.Response(200, json={"album": {"name": "Kid A", "artist": {"name": "Radiohead"}, "listeners": "5"}})]
    )
    async with ac:
        result = await client.fetch_album_info(ac, "test-key", "Radiohead", "Kid A")
    assert result.outcome is client.FetchOutcome.NOT_FOUND

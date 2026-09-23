import httpx
import pytest

from crate_backend.musicbrainz import cover_art

pytestmark = pytest.mark.asyncio


@pytest.fixture
def sleeps(monkeypatch) -> list[float]:
    recorded: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(cover_art, "_sleep", fake_sleep)
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


async def test_redirect_means_art_exists_and_is_not_followed(sleeps):
    client, requests = _client(
        [httpx.Response(307, headers={"location": "https://archive.org/huge-image.jpg"})]
    )
    async with client:
        result = await cover_art.fetch_cover_art_url(client, "test-mbid")
    assert result == cover_art.front_cover_url("test-mbid")
    assert len(requests) == 1


async def test_200_means_art_exists(sleeps):
    client, _ = _client([httpx.Response(200)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is not None


async def test_404_returns_none_without_retrying(sleeps):
    client, requests = _client([httpx.Response(404)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is None
    assert len(requests) == 1


async def test_other_client_error_returns_none_without_raising(sleeps):
    client, requests = _client([httpx.Response(400)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is None
    assert len(requests) == 1


async def test_429_retries_with_backoff(sleeps):
    client, requests = _client([httpx.Response(429), httpx.Response(429), httpx.Response(307)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is not None
    assert len(requests) == 3
    assert sleeps == [1.0, 2.0]


async def test_network_error_is_retried(sleeps):
    client, _ = _client([httpx.ConnectError("connection reset"), httpx.Response(307)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is not None


async def test_gives_up_after_max_retries(sleeps):
    client, requests = _client([httpx.Response(503)])
    async with client:
        assert await cover_art.fetch_cover_art_url(client, "test-mbid") is None
    assert len(requests) == cover_art.MAX_RETRIES + 1
    assert sleeps == [1.0, 2.0, 4.0, 8.0, 16.0]


async def test_backoff_is_capped(monkeypatch, sleeps):
    monkeypatch.setattr(cover_art, "MAX_RETRIES", 8)
    client, _ = _client([httpx.Response(503)])
    async with client:
        await cover_art.fetch_cover_art_url(client, "test-mbid")
    assert max(sleeps) == cover_art.MAX_BACKOFF_SECONDS


async def test_iter_cover_art_paces_requests(sleeps):
    client, _ = _client([httpx.Response(404)])
    async with client:
        results = [item async for item in cover_art.iter_cover_art(client, ["a", "b"])]
    assert results == [("a", None), ("b", None)]
    assert sleeps == [cover_art.REQUEST_INTERVAL_SECONDS] * 2

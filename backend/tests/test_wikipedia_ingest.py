import httpx
import pytest
from sqlalchemy import select

from crate_backend.models.album_text import AlbumText
from crate_backend.models.catalog import Album
from crate_backend.wikipedia import ingest
from crate_backend.wikipedia.client import ArticleResult, FetchOutcome

pytestmark = pytest.mark.asyncio

_KID_A = ArticleResult(
    FetchOutcome.FOUND, title="Kid A", revision_id=1376615480, text="Kid A is an album."
)


@pytest.fixture
def fetch_returns(monkeypatch):
    """Make ingest's article fetch return `result`; records each title asked for."""
    calls: list[str] = []

    def install(result: ArticleResult) -> list[str]:
        async def fake_fetch(client, title):
            calls.append(title)
            return result

        monkeypatch.setattr(ingest, "fetch_article", fake_fetch)
        return calls

    return install


def _redirect(title: str, text: str, revision_id: int = 1) -> ArticleResult:
    return ArticleResult(
        FetchOutcome.FOUND, title=title, revision_id=revision_id, text=text, redirected=True
    )


async def _album(db_session, **overrides) -> Album:
    fields = {"title": "Kid A", "artist_name": "Radiohead"}
    fields.update(overrides)
    album = Album(**fields)
    db_session.add(album)
    await db_session.flush()
    return album


async def _rows(db_session, album_id) -> list[AlbumText]:
    return list(await db_session.scalars(select(AlbumText).where(AlbumText.album_id == album_id)))


async def _sync(db_session, album, titles=None):
    return await ingest.sync_album_text(db_session, httpx.AsyncClient(), album, titles or {})


async def test_found_article_is_stored_with_fetched_at(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikidata_id="Q900000001")

    row = await _sync(db_session, album, {"Q900000001": "Kid A"})

    assert calls == ["Kid A"]
    assert row.source == "wikipedia"
    assert row.article_title == "Kid A"
    assert row.revision_id == 1376615480
    assert row.text == "Kid A is an album."
    assert row.fetched_at is not None


async def test_wikidata_title_is_preferred_over_the_direct_link(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikidata_id="Q900000001", wikipedia_title="Kid_A_(album)")

    await _sync(db_session, album, {"Q900000001": "Kid A"})

    assert calls == ["Kid A"]


async def test_direct_link_is_used_when_wikidata_has_no_english_article(
    db_session, fetch_returns
):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikidata_id="Q900000001", wikipedia_title="Kid_A")

    await _sync(db_session, album, {"Q900000001": None})

    assert calls == ["Kid_A"]


async def test_direct_link_only_album_is_fetched(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikipedia_title="Kid_A")

    row = await _sync(db_session, album)

    assert calls == ["Kid_A"]
    assert row.text == "Kid A is an album."


async def test_no_english_article_is_recorded_without_a_request(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikidata_id="Q900000001")

    row = await _sync(db_session, album, {"Q900000001": None})

    assert calls == []
    assert row.text is None
    assert row.fetched_at is not None


async def test_unresolved_wikidata_id_is_left_for_retry(db_session, fetch_returns):
    calls = fetch_returns(_KID_A)
    album = await _album(db_session, wikidata_id="Q900000001", wikipedia_title="Kid_A")

    row = await _sync(db_session, album, {})

    assert calls == []
    assert row.fetched_at is None


async def test_missing_article_is_definitive(db_session, fetch_returns):
    fetch_returns(ArticleResult(FetchOutcome.MISSING))
    album = await _album(db_session, wikipedia_title="Gone")

    row = await _sync(db_session, album)

    assert row.text is None
    assert row.article_title is None
    assert row.fetched_at is not None


async def test_failed_fetch_is_left_for_retry(db_session, fetch_returns):
    fetch_returns(ArticleResult(FetchOutcome.FAILED))
    album = await _album(db_session, wikipedia_title="Kid_A")

    row = await _sync(db_session, album)

    assert row.fetched_at is None
    assert row.text is None


async def test_redirect_to_the_artist_article_stores_no_text(db_session, fetch_returns):
    fetch_returns(_redirect("Radiohead", "Radiohead are an English rock band."))
    album = await _album(db_session, wikipedia_title="Some_Minor_Album")

    row = await _sync(db_session, album)

    assert row.text is None
    assert row.revision_id is None
    assert row.article_title == "Radiohead"
    assert row.fetched_at is not None


async def test_redirect_to_artist_with_disambiguator_or_discography_stores_no_text(
    db_session, fetch_returns
):
    album = await _album(db_session, artist_name="Low", wikipedia_title="Some_EP")
    for target in ("Low (band)", "Low discography"):
        fetch_returns(_redirect(target, "Band text."))
        row = await _sync(db_session, album)
        assert row.text is None, target


async def test_redirect_to_a_differently_named_album_article_keeps_text(
    db_session, fetch_returns
):
    fetch_returns(_redirect("Kid A Mnesia", "Kid A Mnesia is a reissue.", revision_id=2))
    album = await _album(db_session, wikipedia_title="Kid_A_Mnesia_(album)")

    row = await _sync(db_session, album)

    assert row.text == "Kid A Mnesia is a reissue."


async def test_article_named_like_the_artist_without_a_redirect_keeps_text(
    db_session, fetch_returns
):
    # Self-titled albums: Wikidata can point straight at an article that
    # shares the artist's name.
    fetch_returns(
        ArticleResult(FetchOutcome.FOUND, title="Radiohead", revision_id=3, text="Album text.")
    )
    album = await _album(db_session, wikidata_id="Q900000001")

    row = await _sync(db_session, album, {"Q900000001": "Radiohead"})

    assert row.text == "Album text."


async def test_retry_updates_the_existing_row(db_session, fetch_returns):
    album = await _album(db_session, wikipedia_title="Kid_A")
    fetch_returns(ArticleResult(FetchOutcome.FAILED))
    await _sync(db_session, album)
    fetch_returns(_KID_A)

    await _sync(db_session, album)

    rows = await _rows(db_session, album.id)
    assert len(rows) == 1
    assert rows[0].text == "Kid A is an album."
    assert rows[0].fetched_at is not None


async def test_overlong_final_title_is_truncated_to_the_column(db_session, fetch_returns):
    fetch_returns(ArticleResult(FetchOutcome.FOUND, title="T" * 600, revision_id=4, text="x"))
    album = await _album(db_session, wikipedia_title="Kid_A")

    row = await _sync(db_session, album)

    assert len(row.article_title) == 500


async def test_redirect_to_a_self_titled_album_article_keeps_text(db_session, fetch_returns):
    # "Weezer (Blue Album)" strips to "weezer" but describes the album, not the band.
    fetch_returns(_redirect("Weezer (Blue Album)", "Weezer is the debut album.", revision_id=5))
    album = await _album(
        db_session, title="Weezer", artist_name="Weezer", wikipedia_title="Weezer_(1994_album)"
    )

    row = await _sync(db_session, album)

    assert row.text == "Weezer is the debut album."

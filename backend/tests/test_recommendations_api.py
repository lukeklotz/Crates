import uuid

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select

from crate_backend.api.routes import recommendations as recommendations_route
from crate_backend.db.session import get_session
from crate_backend.main import app
from crate_backend.models.catalog import Album, AlbumTag, Tag
from crate_backend.recommend.tfidf import AlbumDoc, build_model

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client(db_session):
    """An open client (an httpx client can't be reopened, and some tests
    post twice)."""

    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session
    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            yield ac
    finally:
        app.dependency_overrides.pop(get_session, None)


async def _album(db_session, title: str, *tag_names: str, **fields) -> Album:
    album = Album(title=title, artist_name="Fixture Artist", **fields)
    db_session.add(album)
    await db_session.flush()
    for name in tag_names:
        tag = Tag(name=f"zzfixture-api-{name}")
        db_session.add(tag)
        await db_session.flush()
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()
    return album


async def _link(db_session, album: Album, *tag_names: str) -> None:
    """Give `album` tags that already exist (created by _album)."""
    for name in tag_names:
        tag = await db_session.scalar(select(Tag).where(Tag.name == f"zzfixture-api-{name}"))
        db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id))
    await db_session.flush()


async def _post(client, **body):
    return await client.post("/recommendations", json=body)


@pytest.fixture
def use_model(monkeypatch):
    """Serve the given model (or None: no model file built) for tfidf requests."""

    def use(model):
        monkeypatch.setattr(recommendations_route, "get_tfidf_model", lambda: model)

    return use


def _doc(album: Album, *terms: str, text: str = "") -> AlbumDoc:
    return AlbumDoc(
        album_id=album.id, title=album.title, term_votes={t: 1 for t in terms}, text=text
    )


def _model(*docs: AlbumDoc):
    return build_model(list(docs), min_df=1, max_df=1.0)


async def test_returns_ranked_albums_with_shared_terms(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    match = await _album(db_session, "Match", release_year=1999, cover_art_url="https://x.test/c")
    await _link(db_session, match, "a", "b")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    body = response.json()
    assert body["reason"] is None
    assert body["approach"] == "overlap"
    assert body["model_version"] is None
    assert body["results"] == [
        {
            "id": str(match.id),
            "title": "Match",
            "artist_name": "Fixture Artist",
            "release_year": 1999,
            "cover_art_url": "https://x.test/c",
            "score": pytest.approx(1.0),
            "shared_terms": ["zzfixture-api-a", "zzfixture-api-b"],
            "shared_text_terms": [],
        }
    ]


async def test_limit_is_respected(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    for i in range(4):
        await _link(db_session, await _album(db_session, f"Candidate {i}"), "a")

    response = await _post(client, album_ids=[str(seed.id)], limit=2)

    assert len(response.json()["results"]) == 2


async def test_duplicate_seed_ids_are_collapsed(client, db_session):
    seed = await _album(db_session, "Seed", "a", "b")
    await _link(db_session, await _album(db_session, "Partial"), "a")

    once = (await _post(client, album_ids=[str(seed.id)])).json()
    twice = (await _post(client, album_ids=[str(seed.id), str(seed.id)])).json()

    assert twice == once
    assert twice["results"][0]["score"] == pytest.approx(1 / 2)


async def test_unknown_album_ids_are_404_and_listed(client, db_session):
    seed = await _album(db_session, "Seed", "a")
    missing = str(uuid.uuid4())

    response = await _post(client, album_ids=[str(seed.id), missing])

    assert response.status_code == 404
    assert response.json()["detail"]["missing"] == [missing]


@pytest.mark.parametrize(
    "body",
    [
        {"album_ids": []},
        {"album_ids": [str(uuid.uuid4()) for _ in range(51)]},
        {"album_ids": ["not-a-uuid"]},
        {"album_ids": [str(uuid.uuid4())], "limit": 0},
        {"album_ids": [str(uuid.uuid4())], "limit": 51},
        {"album_ids": [str(uuid.uuid4())], "approach": "bogus"},
    ],
)
async def test_invalid_input_is_422(client, body):
    response = await _post(client, **body)

    assert response.status_code == 422


async def test_seeds_without_terms_explain_the_empty_result(client, db_session):
    seed = await _album(db_session, "Untagged Seed")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200
    assert response.json() == {
        "approach": "overlap",
        "model_version": None,
        "results": [],
        "reason": "seeds_have_no_terms",
    }


async def test_tagged_seed_with_no_matches_has_no_reason(client, db_session):
    seed = await _album(db_session, "Lonely Seed", "lonely")

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.json() == {
        "approach": "overlap",
        "model_version": None,
        "results": [],
        "reason": None,
    }


async def test_tfidf_ranks_from_the_model_and_explains_with_text(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    match = await _album(db_session, "Match", release_year=1999)
    model = _model(
        _doc(seed, "jazz", text="modal saxophone"),
        _doc(match, "jazz", text="modal saxophone suite"),
    )
    use_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 200
    body = response.json()
    assert body["approach"] == "tfidf"
    assert body["model_version"] == model.metadata["model_version"]
    assert body["reason"] is None
    [result] = body["results"]
    assert result["id"] == str(match.id)
    assert result["title"] == "Match"
    assert result["release_year"] == 1999
    assert result["shared_terms"] == ["jazz"]
    assert sorted(result["shared_text_terms"]) == ["modal", "modal saxophone", "saxophone"]


async def test_tfidf_without_a_built_model_is_503(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    use_model(None)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 503
    assert response.json() == {"detail": "TF-IDF model not built"}


async def test_overlap_works_without_a_built_model(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    use_model(None)

    response = await _post(client, album_ids=[str(seed.id)])

    assert response.status_code == 200


async def test_seeds_missing_from_the_model_explain_the_empty_result(client, db_session, use_model):
    seed = await _album(db_session, "New Seed", "a")
    older = await _album(db_session, "Older Album", "b")
    model = _model(_doc(older, "jazz"))
    use_model(model)

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.json() == {
        "approach": "tfidf",
        "model_version": model.metadata["model_version"],
        "results": [],
        "reason": "seeds_not_in_model",
    }


async def test_tfidf_seeds_without_terms_keep_their_reason(client, db_session, use_model):
    seed = await _album(db_session, "Untagged Seed")
    other = await _album(db_session, "Tagged Album", "a")
    # A model needs at least one term in the catalog to fit.
    use_model(_model(_doc(seed), _doc(other, "jazz")))

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.json()["reason"] == "seeds_have_no_terms"


async def test_albums_removed_since_the_model_was_built_are_skipped(client, db_session, use_model):
    seed = await _album(db_session, "Seed", "a")
    kept = await _album(db_session, "Kept")
    gone = AlbumDoc(album_id=uuid.uuid4(), title="Gone", term_votes={"jazz": 1})
    use_model(_model(_doc(seed, "jazz"), _doc(kept, "jazz"), gone))

    response = await _post(client, album_ids=[str(seed.id)], approach="tfidf")

    assert response.status_code == 200
    assert [r["id"] for r in response.json()["results"]] == [str(kept.id)]

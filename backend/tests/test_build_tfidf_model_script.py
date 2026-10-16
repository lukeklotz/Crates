import uuid
from datetime import UTC, datetime

import pytest

from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Genre, Tag
from crate_backend.scripts.build_tfidf_model import load_album_docs, parse_args

ARTICLE = (
    "Lead about modal saxophone.\n\n"
    "== Critical reception ==\nCritics loved it.\n\n"
    "== Personnel ==\nElvin Jones – drums\n\n"
    "== Track listing ==\nSong – 3:00"
)


async def _fixture_albums(db_session) -> tuple[Album, Album]:
    album = Album(title="Fixture Build Album", artist_name="Fixture Artist")
    bare = Album(title="Fixture Bare Album", artist_name="Fixture Artist")
    genre = Genre(musicbrainz_id=str(uuid.uuid4()), name="Zzfixture-Build-Post-Bop")
    tag = Tag(name="zzfixture build post bop")
    db_session.add_all([album, bare, genre, tag])
    await db_session.flush()
    now = datetime.now(UTC)
    db_session.add_all(
        [
            AlbumGenre(album_id=album.id, genre_id=genre.id, count=3),
            AlbumTag(album_id=album.id, tag_id=tag.id, count=5),
            AlbumText(album_id=album.id, source=WIKIPEDIA_SOURCE, text=ARTICLE, fetched_at=now),
            AlbumText(album_id=bare.id, source=WIKIPEDIA_SOURCE, text=None, fetched_at=now),
        ]
    )
    await db_session.flush()
    return album, bare


async def test_load_album_docs_merges_votes_and_cleans_text(db_session):
    album, bare = await _fixture_albums(db_session)

    docs = {d.album_id: d for d in await load_album_docs(db_session, only=[album.id, bare.id])}

    assert set(docs) == {album.id, bare.id}
    assert docs[album.id].title == "Fixture Build Album"
    assert docs[album.id].term_votes == {"zzfixture build post bop": 5}
    assert docs[album.id].text == (
        "Lead about modal saxophone.\n\nCritics loved it.\n\nElvin Jones – drums"
    )
    assert docs[bare.id].term_votes == {}
    assert docs[bare.id].text == ""


async def test_load_album_docs_can_drop_reception_and_personnel(db_session):
    album, _ = await _fixture_albums(db_session)

    [doc] = await load_album_docs(
        db_session, drop_reception=True, drop_personnel=True, only=[album.id]
    )

    assert doc.text == "Lead about modal saxophone."


def test_parse_args_defaults():
    args = parse_args([])

    assert args.alpha == 0.6
    assert not args.no_bigrams and not args.no_reception and not args.no_personnel
    assert args.max_features is None and args.out is None
    assert not args.sound_phrases


@pytest.mark.parametrize("alpha", ["-0.1", "1.5"])
def test_parse_args_rejects_alpha_outside_zero_to_one(alpha):
    with pytest.raises(SystemExit):
        parse_args(["--alpha", alpha])


def test_sound_phrases_is_off_by_default_and_read_when_given():
    assert not parse_args([]).sound_phrases
    assert parse_args(["--sound-phrases", "--no-reception"]).sound_phrases


@pytest.mark.parametrize("flags", [["--no-bigrams"], ["--max-features", "1000"]])
def test_sound_phrases_rejects_article_only_flags(flags):
    with pytest.raises(SystemExit):
        parse_args(["--sound-phrases", *flags])


def test_extract_phrases_reads_prose_and_joins_known_tags():
    from crate_backend.recommend.tfidf import AlbumDoc
    from crate_backend.scripts.build_tfidf_model import extract_phrases

    docs = [
        AlbumDoc(uuid.uuid4(), "A", {"acid jazz": 3}, text="It is an acid jazz record."),
        AlbumDoc(uuid.uuid4(), "B", {}, text="Elvin Jones – drums"),
        AlbumDoc(uuid.uuid4(), "C", {}, text=""),
    ]

    phrases, metadata = extract_phrases(docs)

    assert phrases == [["acid jazz"], [], []]
    assert metadata["spacy_version"] == "3.8.7"
    assert metadata["spacy_model"] == "en_core_web_sm-3.8.0"

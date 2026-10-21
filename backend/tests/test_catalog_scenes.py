import pytest

from crate_backend.models.album_text import WIKIPEDIA_SOURCE, AlbumText
from crate_backend.models.catalog import Album, AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.scenes.catalog import load_catalog_albums
from tests.scene_fixtures import minimal_config

pytestmark = pytest.mark.asyncio


async def test_load_catalog_albums_matches_scenes(db_session):
    artist = Artist(name="Test Scene Artist", musicbrainz_id="test-scene-artist")
    tag = Tag(name="test-scene-shoegaze-unique")
    genre = Genre(musicbrainz_id="test-scene-genre", name="Dream Pop")
    db_session.add_all([artist, tag, genre])
    await db_session.flush()
    placed = Album(
        title="Placed",
        artist_name="Test Scene Artist",
        primary_artist_id=artist.id,
        release_year=1991,
        musicbrainz_release_group_id="test-scene-rg-1",
        popularity=0.4,
    )
    bare = Album(title="Bare", release_year=1991)
    db_session.add_all([placed, bare])
    await db_session.flush()
    db_session.add_all(
        [
            AlbumTag(album_id=placed.id, tag_id=tag.id, count=3),
            AlbumGenre(album_id=placed.id, genre_id=genre.id, count=2),
            AlbumText(album_id=placed.id, source=WIKIPEDIA_SOURCE, text="An article."),
            AlbumText(album_id=bare.id, source=WIKIPEDIA_SOURCE, text=None),
        ]
    )
    await db_session.flush()

    config = minimal_config()
    albums = {a.album_id: a for a in await load_catalog_albums(db_session, config)}

    found = albums[placed.id]
    assert found.musicbrainz_id == "test-scene-rg-1"
    assert found.primary_artist_id == "test-scene-artist"
    assert found.terms == {"test scene shoegaze unique": 3, "dream pop": 2}
    assert found.match.home == "d"
    assert found.has_text is True
    assert found.popularity == 0.4
    assert found.year == 1991

    assert albums[bare.id].match is None
    assert albums[bare.id].has_text is False
    assert albums[bare.id].primary_artist_id is None

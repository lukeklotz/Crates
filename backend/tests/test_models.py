import pytest
from sqlalchemy.exc import IntegrityError

from crate_backend.models import (
    Album,
    AlbumGroup,
    CanvasAlbumInstance,
    GroupAlbumMembership,
    GroupSettings,
    User,
    Workspace,
)
from crate_backend.models.artist_relationship import ArtistRelationship
from crate_backend.models.catalog import AlbumGenre, AlbumTag, Artist, Genre, Tag
from crate_backend.models.group import PopularityPreference

pytestmark = pytest.mark.asyncio


async def _seed_group_with_two_albums(db_session):
    user = User(email="listener@example.com", hashed_password="hashed")
    db_session.add(user)
    await db_session.flush()

    workspace = Workspace(user_id=user.id)
    db_session.add(workspace)
    await db_session.flush()

    album_one = Album(title="Illinois", artist_name="Sufjan Stevens")
    album_two = Album(title="The Age of Adz", artist_name="Sufjan Stevens")
    db_session.add_all([album_one, album_two])
    await db_session.flush()

    instance_one = CanvasAlbumInstance(workspace_id=workspace.id, album_id=album_one.id)
    instance_two = CanvasAlbumInstance(workspace_id=workspace.id, album_id=album_two.id)
    db_session.add_all([instance_one, instance_two])
    await db_session.flush()

    group = AlbumGroup(workspace_id=workspace.id, name="Rainy evening")
    db_session.add(group)
    await db_session.flush()

    db_session.add(
        GroupSettings(group_id=group.id, popularity_preference=PopularityPreference.LESSER_KNOWN)
    )
    db_session.add(
        GroupAlbumMembership(group_id=group.id, canvas_instance_id=instance_one.id, user_id=user.id)
    )
    db_session.add(
        GroupAlbumMembership(group_id=group.id, canvas_instance_id=instance_two.id, user_id=user.id)
    )
    await db_session.commit()
    return group, user, instance_one


async def test_group_of_albums_round_trip(db_session):
    group, _user, _instance = await _seed_group_with_two_albums(db_session)

    loaded = await db_session.get(AlbumGroup, group.id)
    await db_session.refresh(loaded, attribute_names=["memberships", "settings"])

    assert len(loaded.memberships) == 2
    assert loaded.settings.popularity_preference == PopularityPreference.LESSER_KNOWN


async def test_album_cannot_appear_twice_in_the_same_group(db_session):
    group, user, instance = await _seed_group_with_two_albums(db_session)

    db_session.add(
        GroupAlbumMembership(group_id=group.id, canvas_instance_id=instance.id, user_id=user.id)
    )
    with pytest.raises(IntegrityError):
        await db_session.commit()


async def test_album_genre_and_tag_round_trip(db_session):
    album = Album(title="Test Album", artist_name="Test Artist")
    genre = Genre(musicbrainz_id="test-genre-round-trip", name="test-genre-round-trip")
    tag = Tag(name="test-tag-round-trip")
    db_session.add_all([album, genre, tag])
    await db_session.flush()

    db_session.add(AlbumGenre(album_id=album.id, genre_id=genre.id, count=5))
    db_session.add(AlbumTag(album_id=album.id, tag_id=tag.id, count=3))
    await db_session.commit()

    loaded = await db_session.get(Album, album.id)
    await db_session.refresh(loaded, attribute_names=["genres", "tags"])
    assert [g.count for g in loaded.genres] == [5]
    assert [t.count for t in loaded.tags] == [3]


async def test_album_genre_is_unique_per_album_and_genre(db_session):
    album = Album(title="Test Album", artist_name="Test Artist")
    genre = Genre(musicbrainz_id="test-genre-unique", name="test-genre-unique")
    db_session.add_all([album, genre])
    await db_session.flush()

    db_session.add(AlbumGenre(album_id=album.id, genre_id=genre.id, count=1))
    await db_session.flush()
    db_session.add(AlbumGenre(album_id=album.id, genre_id=genre.id, count=2))

    with pytest.raises(IntegrityError):
        await db_session.commit()


async def test_artist_relationship_round_trip(db_session):
    member = Artist(name="Test Member", musicbrainz_id="test-artist-member")
    band = Artist(name="Test Band", musicbrainz_id="test-artist-band")
    db_session.add_all([member, band])
    await db_session.flush()

    edge = ArtistRelationship(
        artist_id=member.id, related_artist_id=band.id, relationship_type="member of band"
    )
    db_session.add(edge)
    await db_session.commit()

    loaded = await db_session.get(ArtistRelationship, edge.id)
    assert loaded.relationship_type == "member of band"
    assert loaded.related_artist_id == band.id


async def test_artist_relationship_is_unique_per_pair_and_type(db_session):
    a = Artist(name="Test Artist A", musicbrainz_id="test-artist-a")
    b = Artist(name="Test Artist B", musicbrainz_id="test-artist-b")
    db_session.add_all([a, b])
    await db_session.flush()

    db_session.add(
        ArtistRelationship(artist_id=a.id, related_artist_id=b.id, relationship_type="collaboration")
    )
    await db_session.flush()
    db_session.add(
        ArtistRelationship(artist_id=a.id, related_artist_id=b.id, relationship_type="collaboration")
    )

    with pytest.raises(IntegrityError):
        await db_session.commit()


async def test_popularity_signal_defaults_and_relationship(db_session):
    from crate_backend.models.popularity import PopularitySignal

    album = Album(title="Test Album", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()

    signal = PopularitySignal(album_id=album.id)
    db_session.add(signal)
    await db_session.commit()
    await db_session.refresh(signal)

    assert signal.lastfm_listeners is None
    assert signal.lastfm_fetched_at is None
    assert signal.sandbox_add_count == 0
    assert signal.album_id == album.id


async def test_popularity_signal_is_unique_per_album(db_session):
    from crate_backend.models.popularity import PopularitySignal

    album = Album(title="Test Album", artist_name="Test Artist")
    db_session.add(album)
    await db_session.flush()
    db_session.add_all([PopularitySignal(album_id=album.id), PopularitySignal(album_id=album.id)])

    with pytest.raises(IntegrityError):
        await db_session.flush()

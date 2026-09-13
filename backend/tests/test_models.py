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

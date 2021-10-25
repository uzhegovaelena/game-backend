import pytest

from games import game
from games.game import add_new_game_record, get_number_of_games
from users import user
from users.user import create_new_user
from users.user import get_user_id


async def mock_select_user_id(db, email: str):
    if email == "bob@gmail.com":
        return 1

    return None


async def mock_add_user(db, email: str):
    if isinstance(email, str):
        return 2

    return None


async def mock_add_game(db, user_id: int):
    return 1


async def mock_select_number_of_games(db, user_id: int):
    if user_id == 1:
        return 5

    return 1


class TestForPlayGame:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("email, expected", [("bob@gmail.com", 1), ("mary@gmail.com", None)])
    async def test_get_user_id(self, monkeypatch, email, expected):
        monkeypatch.setattr(user, "select_user_id", mock_select_user_id)

        user_id = await get_user_id(db={}, email=email)

        assert user_id == expected

    @pytest.mark.asyncio
    @pytest.mark.parametrize("email, expected", [("mary@gmail.com", 2), (123, None)])
    async def test_create_new_user(self, monkeypatch, email, expected):
        monkeypatch.setattr(user, "add_user", mock_add_user)

        user_id = await create_new_user(db={}, email=email)

        assert user_id == expected

    @pytest.mark.asyncio
    async def test_add_new_game_record(self, monkeypatch):
        monkeypatch.setattr(game, "add_game", mock_add_game)

        user_id = await add_new_game_record(db={}, user_id=1)

        assert user_id == 1

    @pytest.mark.asyncio
    @pytest.mark.parametrize("user_id, expected", [(1, 5), (2, 1)])
    async def test_get_number_of_games(self, monkeypatch, user_id, expected):
        monkeypatch.setattr(game, "select_number_of_games", mock_select_number_of_games)

        user_id = await get_number_of_games(db={}, user_id=user_id)

        assert user_id == expected

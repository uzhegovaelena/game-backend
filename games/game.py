from db.game import add_game
from db.game import select_number_of_games


async def add_new_game_record(*, db, user_id):
    game_id = await add_game(db, user_id)

    return game_id

async def get_number_of_games(*, db, user_id):
    number_of_games = await select_number_of_games(db, user_id)

    return number_of_games

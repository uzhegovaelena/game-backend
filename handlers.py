from aiohttp import web

from games.game import add_new_game_record
from games.game import get_number_of_games
from users.user import create_new_user
from users.user import get_user_id


async def play_game(request):
    response = {}

    db = request.app["db"]

    body = await request.json()

    email = body.get("email")

    if not email:
        response["message"] = "Required param 'email' is not found"

        return web.json_response(response, 500)

    user_id = await get_user_id(db=db, email=email)

    if not user_id:
        user_id = await create_new_user(db=db, email=email)

        message = "Email is not found. User created."
    else:
        message = "Email is found."

    game_id = await add_new_game_record(db=db, user_id=user_id)

    if not game_id:
        response["message"] = "Something went wrong with adding new games record"

        return web.json_response(response, 500)

    number_of_games = await get_number_of_games(db=db, user_id=user_id)

    response["message"] = message
    response["number_of_games"] = number_of_games

    return web.json_response(response)

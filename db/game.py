async def add_game(db, user_id):
    async with db.acquire() as connection:
        result = await connection.fetchrow(
            """
            INSERT INTO games (
                user_id
            )
            VALUES (
                $1
            )
            RETURNING game_id
            """,
            user_id,
        )

        game_id = result.get("game_id")

        return game_id


async def select_number_of_games(db, user_id):
    async with db.acquire() as connection:
        result = await connection.fetchrow(
            """
            SELECT count(game_name) AS number_of_games
            FROM games
            WHERE user_id = $1
            """,
            user_id,
        )

        number_of_games = result.get("number_of_games")

        return number_of_games

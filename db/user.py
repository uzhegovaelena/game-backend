async def add_user(db, email):
    async with db.acquire() as connection:
        result = await connection.fetchrow(
            """
            INSERT INTO users (
                email
            )
            VALUES (
                $1
            )
            RETURNING user_id
            """,
            email,
        )

        user_id = result.get("user_id")

        return user_id


async def select_user_id(db, email):
    async with db.acquire() as connection:
        user_id = None

        result = await connection.fetchrow(
            """
            SELECT user_id
            FROM users
            WHERE email = $1
            """,
            email,
        )

        if result:
            user_id = result.get("user_id")

        return user_id

from db.user import add_user
from db.user import select_user_id


async def get_user_id(*, db, email):
    user_id = await select_user_id(db, email)

    return user_id


async def create_new_user(*, db, email):
    user_id = None

    if isinstance(email, str):
        user_id = await add_user(db, email)

    return user_id

import aiosqlite
import os

DATABASE_PATH = f"{os.path.realpath(os.path.dirname(__file__))}/../database/database.db"

def ping():
    """
    Not sure this is really necessary, but could be nice to have.
    """

    async def ping():
        return

    async def insert_user_ping_count(user_id: int, server_id: int, count: int) -> bool:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            async with db.execute(
                "INSERT INTO user_ping_count (user_id, server_id, count) VALUES ?, ?, ?)",
                (
                    user_id,
                    server_id,
                    count
                )  
            ) as cursor:
                result = await cursor.fetchone()
                return result[0]


    async def update_user_ping_count(user_id: int, server_id: int, count: int) -> bool:
            async with aiosqlite.connect(DATABASE_PATH) as db:
                async with db.execute(
                    "UPDATE user_ping_count SET user_id=?, server_id=?, count=?)",
                    (
                        user_id,
                        server_id,
                        count
                    )
                ) as cursor:
                    result = await cursor.fetchone()
                    return result[0]


    async def get_user_ping_count(user_id: int, server_id: int) -> int:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            async with db.execute(
                "SELECT ping_count FROM user_ping_count WHERE user_id = ? AND server_id = ?)",
                (
                    user_id,
                    server_id
                ),
            ) as cursor:
                result = await cursor.fetchone()
                return result


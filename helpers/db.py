
import os
import aiosqlite
import datetime
import logging

logger = logging.getLogger("gracybot")

DATABASE_PATH = f"{os.path.realpath(os.path.dirname(__file__))}/../database/database.db"

class db():
    """
    Tossing around a database abastraction layer. Not sure if this is going to be useful or necessary yet.
    """

    async def read(query: str) -> dict:
        """
        Not sure this will work.
        """
        async with aiosqlite.connect(DATABASE_PATH) as db:
            try:
                async with db.execute(
                    query
                ) as cursor:
                    result =  await cursor.fetchall()
            except:
                logger.exception(Exception)
                return Exception
            else:
                return result
            
    async def write():
        return
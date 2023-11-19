import asyncpg
import asyncio
from database.create_sql import *
from config_data.config import Config, load_config

async def main():
    config: Config = load_config()
    connection = await asyncpg.connect(user=config.db.db_user, password=config.db.db_password,
                                     database=config.db.database, host=config.db.db_host,
                                     port=5432)
    statement = CREATE_EXERCISES_TABLE
    status = await connection.execute(statement)
    print(status)
    await connection.close()
asyncio.run(main())
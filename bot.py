import asyncio

import asyncpg
from aiogram import Bot, Dispatcher
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu
from handlers import user_handlers
from middlewares.dbmiddleware import DbSession


logger = logging.getLogger(__name__)

async def create_pool():
    config: Config = load_config()
    return await asyncpg.create_pool(user=config.db.db_user, password=config.db.db_password,
                                     database=config.db.database, host=config.db.db_host,
                                     port=5432, command_timeout=60)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')
    config: Config = load_config()
    storage: MemoryStorage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    pool_connect = await create_pool()
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.update.middleware.register(DbSession(pool_connect))

    await set_main_menu(bot)
    # await db_start()

    dp.include_router(user_handlers.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
import asyncio
from aiogram import Bot, Dispatcher
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu
from handlers import user_handlers
from database.database import db_start

logger = logging.getLogger(__name__)

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
    dp: Dispatcher = Dispatcher(storage=storage)

    await set_main_menu(bot)
    await db_start()

    dp.include_router(user_handlers.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
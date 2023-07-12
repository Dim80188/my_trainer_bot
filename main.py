from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv
import os
from datetime import datetime

storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)

async def on_startup(_):
    await db.db_start()
    print('Bot is running')

class NewOrder(StatesGroup):
    # training = State()
    # statistic = State()
    name = State()
    repet = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await db.cmd_start_db(message.from_user.id)
    await message.answer(f'{message.from_user.first_name}, добро пожаловать! Это бот для записи тренировок.'
                         f'Пожалуйста, выбери режим работы - Внести данные о новой тренировке или Посмотреть прошлые тренировки',
                         reply_markup=kb.main)

@dp.message_handler(text=['Записать данные тренировки', 'Записать еще упражненние'])
async def add_training(message: types.Message):
    await NewOrder.name.set()
    await message.answer('Выберите упражнение', reply_markup=kb.repetitions_list)

@dp.message_handler(state=NewOrder.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user'] = message.from_user.id
        data['date'] = datetime.now().date()
        if message.text == 'Подтягивания':
            data['name'] = message.text
        else:
            message.answer('Вы ввели неверные данные. Пожалуйста, исправьте', reply_markup=kb.repetitions_list)
    await message.answer('Напишите количество повторений')
    await NewOrder.next()

@dp.message_handler(state=NewOrder.repet)
async def add_repetitions(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['repetitions'] = message.text
    await db.add_exerc(state)
    await message.answer('Упражненние записано', reply_markup=kb.exercises_status)
    await state.finish()



@dp.message_handler()
async def answer(message:types.Message):
    await message.reply('Я не понимаю')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
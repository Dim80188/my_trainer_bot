from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message
from database.database import cmd_start_db, add_exerc
from keyboards.keyboard_utils import write_show, more_end
from keyboards.keyboards_repetitions import repetitions_kb, rep_kb
from lexicon.lexicon_ru import LEXICON
from datetime import datetime

router: Router = Router()

class NewOrder(StatesGroup):
    start_training = State()
    name = State()
    repeat = State()

# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await cmd_start_db(message.from_user.id)
    await message.answer(LEXICON['/start'], reply_markup=write_show)

# Этот хэндлер будет срабатывать на команду '/cancel' в любых состояниях
# кроме состояния по умолчанию и отключать машину состояний
@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer('Вы прервали запись данных.\n\nВведенные и не сохраненные данные удалены', reply_markup=write_show)
    await state.clear()


# Этот хэндлер будет срабатывать на команду 'write_training' -
# отвечать клавиатурой с упражнениями
@router.message(Text(text=[LEXICON['write_training'], LEXICON['more_repet']]), StateFilter(default_state))
async def add_training(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=repetitions_kb)
    await state.set_state(NewOrder.name)

# Этот хэндлер будет записывать в базу данных имя пользователя, дату и упражнение
@router.message(Text(text=[LEXICON['pull_ups'], LEXICON['push_ups'], LEXICON['jump']]), StateFilter(NewOrder.name))
async def add_name(message: Message, state: FSMContext):
    await state.update_data(user=message.from_user.id)
    await state.update_data(date=datetime.now().date())
    await state.update_data(name=message.text)

    await message.answer('Напишите количество повторений')
    await state.set_state(NewOrder.repeat)

@router.message(StateFilter(NewOrder.repeat))
async def add_repetitions(message: Message, state: FSMContext):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    await add_exerc(data)
    await message.answer('Упражнение записано', reply_markup=more_end) #записать еще упражнение. закончить тренировку
    await state.clear()

@router.message(Text(text=LEXICON['end_training']), StateFilter(default_state))
async def end_training(message: Message):
    await message.answer('Тренировка окончена. Упражнения записаны', reply_markup=write_show)


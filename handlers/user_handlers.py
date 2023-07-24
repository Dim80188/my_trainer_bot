from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message
from database.database import cmd_start_db, add_exerc
from keyboards.keyboard_utils import write_show, more_end, more_end_repet, training_no_training
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb, chest_kb
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS
from states.states import NewOrder, MuscleGroup, Approaches
from datetime import datetime

router: Router = Router()

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

@router.message(Text(text=LEXICON['start_training']), StateFilter(default_state))
async def change_training(message: Message, state: FSMContext):
    await message.answer('Вы выбрали начать тренировку', reply_markup=training_no_training) # выбор группы мышц или отменить выбор
    await state.set_state(MuscleGroup.change_muscle)


# Этот хэндлер реагирует на выбор начала тренировки
@router.message(Text(text=[LEXICON['training'], LEXICON['more_approach']]), StateFilter(MuscleGroup.change_muscle, Approaches.more_repet))
async def muscle_group_selection(message: Message, state: FSMContext):
    await message.answer('Выберите группу мышц', reply_markup=muscle_group_kb)
    await state.set_state(NewOrder.start_training)

# этот хэндлер реагирует на выбор спины. Отвечает клавиатурой с упражнениями
@router.message(Text(text=LEXICON_MUSCLE['back']), StateFilter(NewOrder.start_training))
async def back_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=back_kb)
    await state.set_state(MuscleGroup.back)

@router.message(Text(text=LEXICON_MUSCLE['chest']), StateFilter(NewOrder.start_training))
async def chest_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=chest_kb)
    await state.set_state(MuscleGroup.chest)

@router.message(Text(text=[LEXICON_REPETITIONS['pull_ups'], LEXICON_REPETITIONS['wide_grip_pull_ups'],
                           LEXICON_REPETITIONS['parallel_grip_pull_ups'], LEXICON_REPETITIONS['australian_pull_ups'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.back))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user=message.from_user.id)
    await state.update_data(date=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(Text(text=[LEXICON_REPETITIONS['push_ups_on'], LEXICON_REPETITIONS['push_ups'],
                           LEXICON_REPETITIONS['top_push_ups'], LEXICON_REPETITIONS['bench_press'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.chest))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user=message.from_user.id)
    await state.update_data(date=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(Approaches.start_repet))
async def write_approaches(message: Message, state: FSMContext):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    await add_exerc(data)
    await message.answer('Упражнение записано. Продолжаем?', reply_markup=more_end_repet)
    await state.set_state(Approaches.more_repet)

# Хэндлер обрабатывает согласие на новый подход. Переносит в другое состояние
# @router.message(Text(text=LEXICON['more_approach']), StateFilter(Approaches.more_repet))
# async def more_approach(message: Message, state: FSMContext):
#     await state.set_state(MuscleGroup.change_muscle)

# Хэндлер обрабатывает отказ от нового подхода. Завершает тренировку
@router.message(Text(text=LEXICON['end_repet']), StateFilter(Approaches.more_repet))
async def end_repet(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы закончили тренировку', reply_markup=write_show)




# Этот хэндлер будет срабатывать на команду 'write_training' -
# отвечать клавиатурой с упражнениями
# @router.message(Text(text=[LEXICON['write_training'], LEXICON['more_repet']]), StateFilter(default_state))
# async def add_training(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=repetitions_kb)
#     await state.set_state(NewOrder.name)

# Этот хэндлер будет записывать в базу данных имя пользователя, дату и упражнение
# @router.message(Text(text=[LEXICON['pull_ups'], LEXICON['push_ups'], LEXICON['jump']]), StateFilter(NewOrder.name))
# async def add_name(message: Message, state: FSMContext):
#     await state.update_data(user=message.from_user.id)
#     await state.update_data(date=datetime.now().date())
#     await state.update_data(name=message.text)
#
#     await message.answer('Напишите количество повторений')
#     await state.set_state(NewOrder.repeat)
#
# @router.message(StateFilter(NewOrder.repeat))
# async def add_repetitions(message: Message, state: FSMContext):
#     await state.update_data(repetitions=message.text)
#     data = await state.get_data()
#     await add_exerc(data)
#     await message.answer('Упражнение записано', reply_markup=more_end) #записать еще упражнение. закончить тренировку
#     await state.clear()




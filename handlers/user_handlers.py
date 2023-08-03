from aiogram import Router

from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from database.database import Request
from keyboards.keyboard_utils import write_show, more_end, more_end_repet_workout, training_no_training, activity_kb

from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_ACTIVITY
from states.states import NewOrder, MuscleGroup, Approaches, Show_statisitc, Activity
from services.simple_calendar import calendar_callback_filter, SimpleCalendar
from datetime import datetime, date

router: Router = Router()

# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    # await cmd_start_db(message.from_user.id)
    await message.answer(LEXICON['/start'], reply_markup=write_show)

# Этот хэндлер будет срабатывать на команду '/cancel' в любых состояниях
# кроме состояния по умолчанию и отключать машину состояний
@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer('Вы прервали запись данных.\n\nВведенные и не сохраненные данные удалены', reply_markup=write_show)
    await state.clear()

@router.message(Text(text=LEXICON['start_training']), StateFilter(default_state))
async def change_training(message: Message, state: FSMContext):
    await message.answer('Вы выбрали начать тренировку. Выберите активность', reply_markup=activity_kb) # выбор группы мышц или отменить выбор
    await state.set_state(Activity.activity_change)

# Хэндлер обрабатывает отказ от нового подхода. Завершает тренировку
@router.message(Text(text=LEXICON['end_repet']), StateFilter(Approaches.more_repet_workout, Approaches.more_repet_gym))
async def end_repet(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы закончили тренировку', reply_markup=write_show)

# Хэндлер обрабатывает команду на просмотр статистики и предлагает клавиатуру с началом периода
@router.message(Text(text=LEXICON['show_statistic']), StateFilter(default_state))
async def show_statistic_func(message: Message, state: FSMContext):
    await message.answer('Вы выбрали просмотр статистики\n\nВыберете начало периода', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Show_statisitc.st_period)

@router.callback_query(calendar_callback_filter, StateFilter(Show_statisitc.st_period))
async def start_period_change(callback_query: CallbackQuery, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}\n\nВыберите окончание периода',
                                            reply_markup=await SimpleCalendar().start_calendar())

        # print(date.date(), type(date))
        date = date.date()

        await state.update_data(start_period = date)
        await state.set_state(Show_statisitc.end_period)

@router.message(StateFilter(Show_statisitc.st_period))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=await SimpleCalendar().start_calendar())

@router.callback_query(calendar_callback_filter, StateFilter(Show_statisitc.end_period))
async def end_period_change(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(end_period = date.date())
        period = await state.get_data()

        period_id = callback_query.message.chat.id


        read = await request.sql_read(period_id, period)
        for ret in read:
            await callback_query.message.answer(f'Дата {ret[1]}. Упр. {ret[2]}. Кол {ret[3]}\n')
        await state.clear()
        await callback_query.message.answer('Статистика приведена.\n\nВыберите дальнейшие действия', reply_markup=write_show)

@router.message(StateFilter(Show_statisitc.end_period))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=await SimpleCalendar().start_calendar())








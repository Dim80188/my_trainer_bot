from aiogram import Router

from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show_kb, activity_kb
from services.simple_calendar import calendar_callback_filter, SimpleCalendar
from states.states import Show_statistic, Delete_data
from database.database import Request
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON

router: Router = Router()

# реагирует на команду старт, предлагает 2 варианта действий - тренировка и просмотр статистики
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Выбери действие', reply_markup=write_show_kb)

@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer('Вы прервали запись данных.\n\nВведенные и не сохраненные данные удалены\n\n'
                         'Выберите дальнейшие действия', reply_markup=write_show_kb)
    await state.clear()


# Отрабатываю выбор удалить, определяю дату записи
@router.message(Command(commands='delete'))
async def process_delete_command_state(message: Message, state: FSMContext):
    await message.answer('Вы выбрали удалить запись.\nВыберите дату', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Delete_data.change_date)

# Получаю дату записи, вывожу все записи за эту дату с кнопочкой "удалить"
@router.callback_query(calendar_callback_filter, StateFilter(Delete_data.change_date))
async def show_deletion_data(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(day_deletion_data=date.date())
        period = await state.get_data()
        period_id = callback_query.from_user.id
        read = await request.sql_read_one_day(period_id, period)
        for ret in read:
            if ret[5] == 0.0:
                await callback_query.message.answer(f'Дата {ret[2]}. Упр. {ret[3]}. Кол {ret[4]}.\n', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Удалить', callback_data=f'del {ret[0]}')],]))

            else:
                weight_for_read = float(ret[5])
                await callback_query.message.answer(f'Дата {ret[2]}. Упр. {ret[3]}. Кол {ret[4]}. Вес {round(weight_for_read, 2)}\n', reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Удалить', callback_data=f'del {ret[0]}')], ]))
    await state.set_state(Delete_data.change_data)

@router.callback_query(lambda x: x.data and x.data.startswith('del '), StateFilter(Delete_data.change_data))
async def del_callback_run(callback: CallbackQuery, state: FSMContext, request: Request):
    data_1 = int(callback.data.replace('del ', ''))
    await request.sql_delete_command(data_1)
    await callback.message.answer('Запись удалена.\n\nВыберите дальнейшие действия', reply_markup=write_show_kb)
    await state.clear()


# реагирует на команду тренироваться и выбирает активность
@router.callback_query(Text(text=['training']))
async def change_training(callback: CallbackQuery):
    await callback.message.answer(text='Вы выбрали тренироваться.\nВыберите активность',
                                  reply_markup=activity_kb)
    await callback.answer()

@router.callback_query(Text(text=['end_training']))
async def end_training(callback: CallbackQuery):
    await callback.message.answer('Вы закончили тренировку\n\nВыберите дальнейшие действия', reply_markup=write_show_kb)


@router.callback_query(Text(text=['statistic']))
async def show_statistic_func(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы выбрали просмотр статистики\n\nВыберете начало периода', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(Show_statistic.start_period)

@router.callback_query(calendar_callback_filter, StateFilter(Show_statistic.start_period))
async def start_period_change(callback_query: CallbackQuery, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}\n\nВыберите окончание периода',
                                            reply_markup=await SimpleCalendar().start_calendar())

        date = date.date()
        await state.update_data(start_period=date)
        await state.set_state(Show_statistic.end_period)

@router.callback_query(calendar_callback_filter, StateFilter(Show_statistic.end_period))
async def end_period_change(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(end_period=date.date())
        period = await state.get_data()
        period_id = callback_query.from_user.id
        read = await request.sql_read(period_id, period)

        for ret in read:
            if ret[5] == 0.0:
                await callback_query.message.answer(f'Дата {ret[2]}. Упр. {ret[3]}. Кол {ret[4]}.\n')
            else:
                weight_for_read = float(ret[5])
                await callback_query.message.answer(f'Дата {ret[2]}. Упр. {ret[3]}. Кол {ret[4]}. Вес {round(weight_for_read, 2)}\n')
        await state.clear()
        await callback_query.message.answer('Статистика приведена.\n\nВыберите дальнейшие действия', reply_markup=write_show_kb)










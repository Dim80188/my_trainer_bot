from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from database.database import Request
from keyboards.keyboard_utils import write_show, more_end, more_end_repet, training_no_training
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb, chest_kb
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS
from states.states import NewOrder, MuscleGroup, Approaches, Show_statisitc
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
    await message.answer('Вы выбрали начать тренировку', reply_markup=training_no_training) # выбор группы мышц или отменить выбор
    await state.set_state(MuscleGroup.changed_muscle)


# Этот хэндлер реагирует на выбор начала тренировки
@router.message(Text(text=[LEXICON['training'], LEXICON['more_approach']]), StateFilter(MuscleGroup.changed_muscle, Approaches.more_repet))
async def muscle_group_selection(message: Message, state: FSMContext):
    await message.answer('Выберите группу мышц', reply_markup=muscle_group_kb)
    await state.set_state(NewOrder.start_training)

# этот хэндлер реагирует на выбор спины. Отвечает клавиатурой с упражнениями
@router.message(Text(text=LEXICON_MUSCLE['back']), StateFilter(NewOrder.start_training))
async def back_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=back_kb)
    await state.set_state(MuscleGroup.changed_muscle)

@router.message(Text(text=LEXICON_MUSCLE['chest']), StateFilter(NewOrder.start_training))
async def chest_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=chest_kb)
    await state.set_state(MuscleGroup.changed_muscle)

@router.message(Text(text=[LEXICON_REPETITIONS['pull_ups'], LEXICON_REPETITIONS['wide_grip_pull_ups'],
                           LEXICON_REPETITIONS['parallel_grip_pull_ups'], LEXICON_REPETITIONS['australian_pull_ups'],
                           LEXICON_REPETITIONS['push_ups_on'], LEXICON_REPETITIONS['push_ups'],
                            LEXICON_REPETITIONS['top_push_ups'], LEXICON_REPETITIONS['bench_press'],
                            LEXICON['more_approach']]), StateFilter(MuscleGroup.changed_muscle))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)



@router.message(StateFilter(Approaches.start_repet))
async def write_approaches(message: Message, state: FSMContext, request: Request):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    await request.add_exerc(data)
    await message.answer('Упражнение записано. Продолжаем?', reply_markup=more_end_repet)
    await state.set_state(Approaches.more_repet)



# Хэндлер обрабатывает отказ от нового подхода. Завершает тренировку
@router.message(Text(text=LEXICON['end_repet']), StateFilter(Approaches.more_repet))
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

@router.callback_query(calendar_callback_filter, StateFilter(Show_statisitc.end_period))
async def end_period_change(callback_query: CallbackQuery, state: FSMContext, request: Request):
    selected, date = await SimpleCalendar().process_selection(callback_query)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        await state.update_data(end_period = date.date())
        period = await state.get_data()

        read = await request.sql_read(period)
        for ret in read:
            await callback_query.message.answer(f'Дата {ret[1]}. Упр. {ret[2]}. Кол {ret[3]}\n')
        await state.clear()
        await callback_query.message.answer('Статистика приведена.\n\nВыберите дальнейшие действия', reply_markup=write_show)










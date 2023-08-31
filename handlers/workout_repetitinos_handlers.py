from aiogram import Router
from aiogram.filters import Command, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb_workout, chest_kb_workout, shoulders_kb_workout, biceps_kb_workout, triceps_kb_workout, press_kb_workout, thigh_kb_workout, lower_leg_kb_workout
from keyboards.keyboard_utils import more_end_repet_workout
from lexicon.lexicon_ru import LEXICON_MUSCLE, LEXICON_REPETITIONS_BACK, LEXICON_REPETITIONS_CHEST, LEXICON_REPETITIONS_SHOULDERS, LEXICON_REPETITIONS_BICEPS, LEXICON_REPETITIONS_TRICEPS, LEXICON_REPETITIONS_PRESS, LEXICON_REPETITIONS_THIGH, LEXICON_REPETITIONS_LOWER_LEG
from states.states import Training
from datetime import datetime, date
from database.database import Request

router: Router = Router()

# выбираю группу мышц
@router.callback_query(Text(text=['workout']))
async def muscle_group_selection(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали воркаут.\nВыберите группу мышц',
                                  reply_markup=muscle_group_kb)
    await state.set_state(Training.change_workout)

# выбираю группу мышц
@router.callback_query(Text(text=['back']), StateFilter(Training.change_workout))
async def back_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=back_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['pull_ups', 'wide_grip_pull_ups', 'parallel_grip_pull_ups', 'australian_pull_ups', 'curved_bar_pull_ups']),
                       StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_BACK[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)



@router.callback_query(Text(text=['chest']), StateFilter(Training.change_workout))
async def chest_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=chest_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['push_ups_on', 'push_ups', 'top_push_ups']), StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_CHEST[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)

@router.callback_query(Text(text=['shoulders']), StateFilter(Training.change_workout))
async def shoulders_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=shoulders_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['bench_press_standing']), StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_SHOULDERS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)

@router.callback_query(Text(text=['biceps']), StateFilter(Training.change_workout))
async def biceps_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=biceps_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['reverse_grip_pull_ups']), StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_BICEPS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)

@router.callback_query(Text(text=['triceps']), StateFilter(Training.change_workout))
async def triceps_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=triceps_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['push_ups_between_benches', 'narrow_grip_push-ups']), StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_TRICEPS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)

@router.callback_query(Text(text=['press']), StateFilter(Training.change_workout))
async def press_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=press_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['torso_lift', 'leg_lift', 'twisting']), StateFilter(Training.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_PRESS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)

@router.callback_query(Text(text=['thigh']), StateFilter(Training.change_workout))
async def thigh_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=thigh_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['sit_ups', 'squats_on_one_leg', 'jumping']), StateFilter(Training.change_exercises))
async def write_repetitions(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_THIGH[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)


@router.callback_query(Text(text=['lower_leg']), StateFilter(Training.change_workout))
async def lower_leg_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите уражнение', reply_markup=lower_leg_kb_workout)
    await state.set_state(Training.change_exercises)

@router.callback_query(Text(text=['rise_on_toes']), StateFilter(Training.change_exercises))
async def write_repetitions(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_LOWER_LEG[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training.change_number_of_repetitions)



@router.message(StateFilter(Training.change_number_of_repetitions))
async def write_approaches(message: Message, state: FSMContext, request: Request):
    await state.update_data(repetitions=message.text)
    await state.update_data(weight='0')
    data = await state.get_data()
    repetit = data['repetitions']
    if repetit.isdigit():
        await request.add_exerc(data)
        await message.answer('Упражнение записано. Продолжаем?', reply_markup=more_end_repet_workout)
    else:
        await message.answer('Количество повторений должно быть числом.\n'
                             'Пожалуйста, введите данные заново', reply_markup=muscle_group_kb)
        await state.set_state(Training.change_workout)





from aiogram import Router
from aiogram.filters import Command, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb_gym, chest_kb_gym, shoulders_kb_gym, biceps_kb_gym, triceps_kb_gym, press_kb_gym, thigh_kb_gym, lower_leg_kb_gym
from keyboards.keyboard_utils import more_end_repet_workout
from lexicon.lexicon_ru import LEXICON_REPETITIONS_BACK, LEXICON_REPETITIONS_CHEST, LEXICON_REPETITIONS_SHOULDERS, LEXICON_REPETITIONS_BICEPS, LEXICON_REPETITIONS_TRICEPS, LEXICON_REPETITIONS_PRESS, LEXICON_REPETITIONS_THIGH, LEXICON_REPETITIONS_LOWER_LEG
from states.states import Training_gym
from datetime import datetime, date
from database.database import Request

router: Router = Router()

@router.callback_query(Text(text=['gym']))
async def muscle_group_selection(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали занятие в зале.\nВыберите группу мышц',
                                  reply_markup=muscle_group_kb)
    await state.set_state(Training_gym.change_gym)

@router.callback_query(Text(text=['back']), StateFilter(Training_gym.change_gym))
async def back_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=back_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['pull_ups', 'wide_grip_pull_ups', 'parallel_grip_pull_ups', 'australian_pull_ups',
                                  'curved_bar_pull_ups', 'bent_over_row', 'bent_over_dumbbell_row', 'upper_block_pull',
                                  'lower_block_pull', 'deadlift', 'deadlift_st', 'sumo_deadlift', 'shrugs', 'hyperextension']),
                       StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_BACK[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['chest']), StateFilter(Training_gym.change_gym))
async def chest_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=chest_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['push_ups_on', 'bench_press', 'incline_bench_press', 'dumbbell_laying',
                                  'head_up_dumbbell_raises', 'mixing_hands_on_the_simulator']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_CHEST[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['shoulders']), StateFilter(Training_gym.change_gym))
async def shoulders_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=shoulders_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['bench_press_standing', 'bench_press_sitting', 'chin_pull', 'swing_forward',
                                  'swing_to_the_side', 'tilt_swing']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_SHOULDERS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['biceps']), StateFilter(Training_gym.change_gym))
async def biceps_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=biceps_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['reverse_grip_pull_ups', 'curling_arms_for_biceps', 'barbell_curl', 'curling_arms_with_dumbbells',
                                  'sitting_dumbbell_сurl', 'curls_with_dumbbells_sitting_on_an_incline_bench',
                                  'barbell_curl_on_scott_bench', 'curling_arms_with_a_dumbbell_on_a_scott_bench',
                                  'bending_the_arms_with_a_curved_neck_on_the_scott_bench', 'bending_arms_with_a_curved_neck',
                                  'concentrated_curls']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_BICEPS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['triceps']), StateFilter(Training_gym.change_gym))
async def triceps_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=triceps_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['push_ups_between_benches', 'french_bench_press', 'standing_french_bench_press',
                                  'dumbbell_french_press', 'narrow_grip_bench_press', 'extension_of_arms_on_the_block',
                                  'extension_of_arms_on_the_block_with_a_reverse_grip', 'extension_of_arms_on_the_block_with_one_hand',
                                  'concentrated_extension']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_TRICEPS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['press']), StateFilter(Training_gym.change_gym))
async def press_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=press_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['torso_lift', 'leg_lift', 'twisting']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_PRESS[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['thigh']), StateFilter(Training_gym.change_gym))
async def thigh_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=thigh_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['sit_ups', 'leg_press', 'leg_extension', 'leg_curl']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_THIGH[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)

@router.callback_query(Text(text=['lower_leg']), StateFilter(Training_gym.change_gym))
async def lower_leg_repetitions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите упражнение', reply_markup=lower_leg_kb_gym)
    await state.set_state(Training_gym.change_exercises)

@router.callback_query(Text(text=['rise_on_toes', 'lifting_on_socks_sitting']), StateFilter(Training_gym.change_exercises))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_REPETITIONS_LOWER_LEG[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_gym.change_number_of_repetitions)


@router.message(StateFilter(Training_gym.change_number_of_repetitions))
async def write_approaches(message: Message, state: FSMContext, request: Request):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    repetit = data['repetitions']
    if repetit.isdigit():
        await message.answer('Запишите вес')
        await state.set_state(Training_gym.change_number_of_weight)
    else:
        await message.answer('Количество повторений должно быть числом.\n'
                                  'Пожалуйста, введите данные заново', reply_markup=muscle_group_kb)
        await state.set_state(Training_gym.change_gym)


@router.message(StateFilter(Training_gym.change_number_of_weight))
async def write_weight(message: Message, state: FSMContext, request: Request):
    weight = message.text
    if ',' in weight:
        weight_in_base = weight.replace(',', '.')
    else:
        weight_in_base = weight
    weight_1 = weight_in_base.replace('.', '')
    if weight_1.isdigit():
        await state.update_data(weight=message.text)
        data = await state.get_data()
        await request.add_exerc(data)
        await message.answer('Упражнение записано. Продолжаем?', reply_markup=more_end_repet_workout)
    else:
        await message.answer('Вес должен быть числом.\n'
                              'Пожалуйста, введите данные заново', reply_markup=muscle_group_kb)
        await state.set_state(Training_gym.change_gym)















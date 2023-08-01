from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show, more_end, more_end_repet, training_no_training
from keyboards.keyboards_repetitions import muscle_group_kb
from keyboards.workout_repetitions import back_kb, chest_kb, shoulders_kb, biceps_kb, triceps_kb, press_kb, thigh_kb, lower_leg_kb
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS
from states.states import NewOrder, MuscleGroup, Approaches, Show_statisitc
from datetime import datetime, date

router: Router = Router()

@router.message(Text(text=LEXICON_MUSCLE['back']), StateFilter(NewOrder.start_training))
async def back_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=back_kb)
    await state.set_state(MuscleGroup.back)

@router.message(Text(text=[LEXICON_REPETITIONS['pull_ups'], LEXICON_REPETITIONS['wide_grip_pull_ups'],
                           LEXICON_REPETITIONS['parallel_grip_pull_ups'], LEXICON_REPETITIONS['australian_pull_ups'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.back))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.back))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=back_kb)

@router.message(Text(text=LEXICON_MUSCLE['chest']), StateFilter(NewOrder.start_training))
async def chest_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=chest_kb)
    await state.set_state(MuscleGroup.chest)

@router.message(Text(text=[LEXICON_REPETITIONS['push_ups_on'], LEXICON_REPETITIONS['push_ups'],
                           LEXICON_REPETITIONS['top_push_ups'], LEXICON_REPETITIONS['bench_press'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.chest))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.chest))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=chest_kb)


@router.message(Text(text=LEXICON_MUSCLE['shoulders']), StateFilter(NewOrder.start_training))
async def shoulders_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=shoulders_kb)
    await state.set_state(MuscleGroup.shoulders)

@router.message(Text(text=[LEXICON_REPETITIONS['bench_press_standing'], LEXICON_REPETITIONS['bench_press_sitting'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.shoulders))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.shoulders))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=shoulders_kb)

@router.message(Text(text=LEXICON_MUSCLE['biceps']), StateFilter(NewOrder.start_training))
async def biceps_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=biceps_kb)
    await state.set_state(MuscleGroup.biceps)

@router.message(Text(text=[LEXICON_REPETITIONS['reverse_grip_pull_ups'], LEXICON_REPETITIONS['curling_arms_for_biceps'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.biceps))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.biceps))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=biceps_kb)

@router.message(Text(text=LEXICON_MUSCLE['triceps']), StateFilter(NewOrder.start_training))
async def triceps_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=triceps_kb)
    await state.set_state(MuscleGroup.triceps)

@router.message(Text(text=[LEXICON_REPETITIONS['push_ups_between_benches'], LEXICON['more_approach']]), StateFilter(MuscleGroup.triceps))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.triceps))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=triceps_kb)

@router.message(Text(text=LEXICON_MUSCLE['press']), StateFilter(NewOrder.start_training))
async def press_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=press_kb)
    await state.set_state(MuscleGroup.press)

@router.message(Text(text=[LEXICON_REPETITIONS['torso_lift'],
                           LEXICON_REPETITIONS['leg_lift'], LEXICON_REPETITIONS['twisting'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.press))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.press))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=press_kb)

@router.message(Text(text=LEXICON_MUSCLE['thigh']), StateFilter(NewOrder.start_training))
async def thigh_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=thigh_kb)
    await state.set_state(MuscleGroup.thigh)

@router.message(Text(text=[LEXICON_REPETITIONS['sit_ups'], LEXICON_REPETITIONS['jumping'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.thigh))
async def write_repetitions(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)

@router.message(StateFilter(MuscleGroup.thigh))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=thigh_kb)


@router.message(Text(text=LEXICON_MUSCLE['lower_leg']), StateFilter(NewOrder.start_training))
async def thigh_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=lower_leg_kb)
    await state.set_state(MuscleGroup.lower_leg)


@router.message(Text(text=[LEXICON_REPETITIONS['rise_on_toes'],
                           LEXICON['more_approach']]), StateFilter(MuscleGroup.lower_leg))
async def write_repetitions(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet)


@router.message(StateFilter(MuscleGroup.lower_leg))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=lower_leg_kb)


@router.message(StateFilter(NewOrder.start_training))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=muscle_group_kb)

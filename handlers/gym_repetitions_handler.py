from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show, more_end, more_end_repet_gym, training_no_training
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb_gym, chest_kb_workout, shoulders_kb_workout, biceps_kb_workout, triceps_kb_workout, press_kb, thigh_kb_workout, lower_leg_kb_workout

from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS_PRESS, LEXICON_REPETITIONS_THIGH, LEXICON_REPETITIONS_TRICEPS, LEXICON_REPETITIONS_BACK, LEXICON_REPETITIONS_BICEPS, LEXICON_REPETITIONS_CHEST, LEXICON_REPETITIONS_SHOULDERS, LEXICON_REPETITIONS_lOWER_LEG, LEXICON_ACTIVITY
from states.states import NewOrder, MuscleGroup, Approaches, Activity, Change_muscle
from datetime import datetime, date
from database.database import Request

router: Router = Router()


@router.message(Text(text=[LEXICON_ACTIVITY['gym'], LEXICON['more_approach_gym']]),
                StateFilter(Activity.activity_change, Approaches.more_repet_gym))
async def muscle_group_selection(message: Message, state: FSMContext):
    await message.answer('Выберите группу мышц', reply_markup=muscle_group_kb)
    await state.set_state(Change_muscle.change_muscle_gym)





@router.message(Text(text=LEXICON_MUSCLE['back']), StateFilter(Change_muscle.change_muscle_gym))
async def back_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=back_kb_gym)
    await state.set_state(MuscleGroup.back_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_BACK['pull_ups'], LEXICON_REPETITIONS_BACK['wide_grip_pull_ups'],
                           LEXICON_REPETITIONS_BACK['parallel_grip_pull_ups'], LEXICON_REPETITIONS_BACK['curved_bar_pull_ups'],
                           LEXICON_REPETITIONS_BACK['bent_over_row'], LEXICON_REPETITIONS_BACK['bent_over_dumbbell_row'],
                           LEXICON_REPETITIONS_BACK['upper_block_pull'], LEXICON_REPETITIONS_BACK['lower_block_pull'],
                           LEXICON_REPETITIONS_BACK['deadlift'], LEXICON_REPETITIONS_BACK['deadlift_st'],
                           LEXICON_REPETITIONS_BACK['sumo_deadlift'], LEXICON_REPETITIONS_BACK['shrugs'],
                           LEXICON_REPETITIONS_BACK['hyperextension'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.back_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.back))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=back_kb_gym)

@router.message(Text(text=LEXICON_MUSCLE['chest']), Change_muscle.change_muscle_gym)
async def chest_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=chest_kb_gym)
    await state.set_state(MuscleGroup.chest)

@router.message(Text(text=[LEXICON_REPETITIONS_CHEST['push_ups_on'], LEXICON_REPETITIONS_CHEST['push_ups'],
                           LEXICON_REPETITIONS_CHEST['top_push_ups'], LEXICON_REPETITIONS_CHEST['bench_press'],
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
                         'отправьте команду /cancel', reply_markup=chest_kb_workout)

#
# @router.message(Text(text=LEXICON_MUSCLE['shoulders']), StateFilter(Change_muscle.change_muscle_workout))
# async def shoulders_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=shoulders_kb_workout)
#     await state.set_state(MuscleGroup.shoulders)
#
# @router.message(Text(text=[LEXICON_REPETITIONS_SHOULDERS['bench_press_standing'], LEXICON_REPETITIONS_SHOULDERS['bench_press_sitting'],
#                            LEXICON['more_approach']]), StateFilter(MuscleGroup.shoulders))
# async def write_repetition(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
# @router.message(StateFilter(MuscleGroup.shoulders))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=shoulders_kb_workout)
#
# @router.message(Text(text=LEXICON_MUSCLE['biceps']), StateFilter(Change_muscle.change_muscle_workout))
# async def biceps_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=biceps_kb_workout)
#     await state.set_state(MuscleGroup.biceps)
#
# @router.message(Text(text=[LEXICON_REPETITIONS_BICEPS['reverse_grip_pull_ups'], LEXICON_REPETITIONS_BICEPS['curling_arms_for_biceps'],
#                            LEXICON['more_approach']]), StateFilter(MuscleGroup.biceps))
# async def write_repetition(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
# @router.message(StateFilter(MuscleGroup.biceps))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=biceps_kb_workout)
#
# @router.message(Text(text=LEXICON_MUSCLE['triceps']), StateFilter(Change_muscle.change_muscle_workout))
# async def triceps_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=triceps_kb_workout)
#     await state.set_state(MuscleGroup.triceps)
#
# @router.message(Text(text=[LEXICON_REPETITIONS_TRICEPS['push_ups_between_benches'], LEXICON['more_approach']]), StateFilter(MuscleGroup.triceps))
# async def write_repetition(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
# @router.message(StateFilter(MuscleGroup.triceps))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=triceps_kb_workout)
#
# @router.message(Text(text=LEXICON_MUSCLE['press']), StateFilter(Change_muscle.change_muscle_workout))
# async def press_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=press_kb)
#     await state.set_state(MuscleGroup.press)
#
# @router.message(Text(text=[LEXICON_REPETITIONS_PRESS['torso_lift'],
#                            LEXICON_REPETITIONS_PRESS['leg_lift'], LEXICON_REPETITIONS_PRESS['twisting'],
#                            LEXICON['more_approach']]), StateFilter(MuscleGroup.press))
# async def write_repetition(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
# @router.message(StateFilter(MuscleGroup.press))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=press_kb)
#
# @router.message(Text(text=LEXICON_MUSCLE['thigh']), StateFilter(Change_muscle.change_muscle_workout))
# async def thigh_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=thigh_kb_workout)
#     await state.set_state(MuscleGroup.thigh)
#
# @router.message(Text(text=[LEXICON_REPETITIONS_THIGH['sit_ups'], LEXICON_REPETITIONS_THIGH['jumping'],
#                            LEXICON['more_approach']]), StateFilter(MuscleGroup.thigh))
# async def write_repetitions(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
# @router.message(StateFilter(MuscleGroup.thigh))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=thigh_kb_workout)
#
#
# @router.message(Text(text=LEXICON_MUSCLE['lower_leg']), StateFilter(Change_muscle.change_muscle_workout))
# async def thigh_repetitions(message: Message, state: FSMContext):
#     await message.answer('Выберите упражнение', reply_markup=lower_leg_kb_workout)
#     await state.set_state(MuscleGroup.lower_leg)
#
#
# @router.message(Text(text=[LEXICON_REPETITIONS_lOWER_LEG['rise_on_toes'],
#                            LEXICON['more_approach']]), StateFilter(MuscleGroup.lower_leg))
# async def write_repetitions(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(date_train=datetime.now().date())
#     await state.update_data(name=message.text)
#     await message.answer('Запишите количество повторений')
#     await state.set_state(Approaches.start_repet)
#
#
# @router.message(StateFilter(MuscleGroup.lower_leg))
# async def warning_not_change(message: Message):
#     await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
#                          'Если вы хотите прервать ввод данных - '
#                          'отправьте команду /cancel', reply_markup=lower_leg_kb_workout)

@router.message(StateFilter(Approaches.start_repet_gym))
async def write_approaches(message: Message, state: FSMContext, request: Request):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    repetit = data['repetitions']

    if repetit.isdigit():
        await request.add_exerc(data)
        await message.answer('Упражнение записано. Продолжаем?', reply_markup=more_end_repet_gym)
        await state.set_state(Approaches.more_repet_gym)
    else:
        await message.answer('Количество повторений должно быть числом.\n'
                             'Пожалуйста, введите данные заново', reply_markup=muscle_group_kb)
        await state.set_state(Change_muscle.change_muscle_workout)




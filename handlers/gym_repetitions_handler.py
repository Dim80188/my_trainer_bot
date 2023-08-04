from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard_utils import write_show, more_end, more_end_repet_gym, training_no_training
from keyboards.keyboards_repetitions import muscle_group_kb, back_kb_gym, chest_kb_gym, shoulders_kb_gym, biceps_kb_gym, triceps_kb_gym, press_kb_gym, thigh_kb_gym, lower_leg_kb_gym

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

@router.message(StateFilter(MuscleGroup.back_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=back_kb_gym)

@router.message(Text(text=LEXICON_MUSCLE['chest']), Change_muscle.change_muscle_gym)
async def chest_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=chest_kb_gym)
    await state.set_state(MuscleGroup.chest_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_CHEST['push_ups_on'], LEXICON_REPETITIONS_CHEST['push_ups'],
                           LEXICON_REPETITIONS_CHEST['top_push_ups'], LEXICON_REPETITIONS_CHEST['bench_press'],
                           LEXICON_REPETITIONS_CHEST['incline_bench_press'], LEXICON_REPETITIONS_CHEST['dumbbell_laying'],
                           LEXICON_REPETITIONS_CHEST['head_up_dumbbell_raises'], LEXICON_REPETITIONS_CHEST['mixing_hands_on_the_simulator'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.chest_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.chest_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=chest_kb_gym)


@router.message(Text(text=LEXICON_MUSCLE['shoulders']), StateFilter(Change_muscle.change_muscle_gym))
async def shoulders_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=shoulders_kb_gym)
    await state.set_state(MuscleGroup.shoulders_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_SHOULDERS['bench_press_standing'], LEXICON_REPETITIONS_SHOULDERS['bench_press_sitting'],
                           LEXICON_REPETITIONS_SHOULDERS['chin_pull'], LEXICON_REPETITIONS_SHOULDERS['swing_forward'],
                           LEXICON_REPETITIONS_SHOULDERS['swing_to_the_side'], LEXICON_REPETITIONS_SHOULDERS['tilt_swing'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.shoulders_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.shoulders_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=shoulders_kb_gym)

@router.message(Text(text=LEXICON_MUSCLE['biceps']), StateFilter(Change_muscle.change_muscle_gym))
async def biceps_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=biceps_kb_gym)
    await state.set_state(MuscleGroup.biceps_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_BICEPS['reverse_grip_pull_ups'], LEXICON_REPETITIONS_BICEPS['curling_arms_for_biceps'],
                           LEXICON_REPETITIONS_BICEPS['barbell_curl'], LEXICON_REPETITIONS_BICEPS['curling_arms_with_dumbbells'],
                           LEXICON_REPETITIONS_BICEPS['sitting_dumbbell_сurl'], LEXICON_REPETITIONS_BICEPS['curls_with_dumbbells_sitting_on_an_incline_bench'],
                           LEXICON_REPETITIONS_BICEPS['barbell_curl_on_scott_bench'], LEXICON_REPETITIONS_BICEPS['curling_arms_with_a_dumbbell_on_a_scott_bench'],
                           LEXICON_REPETITIONS_BICEPS['bending_the_arms_with_a_curved_neck_on_the_scott_bench'], LEXICON_REPETITIONS_BICEPS['bending_arms_with_a_curved_neck'],
                           LEXICON_REPETITIONS_BICEPS['concentrated_curls'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.biceps_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.biceps_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=biceps_kb_gym)
#
@router.message(Text(text=LEXICON_MUSCLE['triceps']), StateFilter(Change_muscle.change_muscle_gym))
async def triceps_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=triceps_kb_gym)
    await state.set_state(MuscleGroup.triceps_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_TRICEPS['push_ups_between_benches'], LEXICON_REPETITIONS_TRICEPS['french_bench_press'],
                           LEXICON_REPETITIONS_TRICEPS['standing_french_bench_press'], LEXICON_REPETITIONS_TRICEPS['dumbbell_french_press'],
                           LEXICON_REPETITIONS_TRICEPS['narrow_grip_bench_press'], LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block'],
                           LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_a_reverse_grip'], LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_one_hand'],
                           LEXICON_REPETITIONS_TRICEPS['concentrated_extension'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.triceps_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.triceps_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=triceps_kb_gym)

@router.message(Text(text=LEXICON_MUSCLE['press']), StateFilter(Change_muscle.change_muscle_gym))
async def press_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=press_kb_gym)
    await state.set_state(MuscleGroup.press_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_PRESS['torso_lift'],
                           LEXICON_REPETITIONS_PRESS['leg_lift'], LEXICON_REPETITIONS_PRESS['twisting'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.press_gym))
async def write_repetition(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.press_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=press_kb_gym)

@router.message(Text(text=LEXICON_MUSCLE['thigh']), StateFilter(Change_muscle.change_muscle_gym))
async def thigh_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=thigh_kb_gym)
    await state.set_state(MuscleGroup.thigh_gym)

@router.message(Text(text=[LEXICON_REPETITIONS_THIGH['sit_ups'], LEXICON_REPETITIONS_THIGH['leg_press'],
                           LEXICON_REPETITIONS_THIGH['leg_extension'], LEXICON_REPETITIONS_THIGH['leg_curl'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.thigh_gym))
async def write_repetitions(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)

@router.message(StateFilter(MuscleGroup.thigh_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=thigh_kb_gym)


@router.message(Text(text=LEXICON_MUSCLE['lower_leg']), StateFilter(Change_muscle.change_muscle_gym))
async def thigh_repetitions(message: Message, state: FSMContext):
    await message.answer('Выберите упражнение', reply_markup=lower_leg_kb_gym)
    await state.set_state(MuscleGroup.lower_leg_gym)


@router.message(Text(text=[LEXICON_REPETITIONS_lOWER_LEG['rise_on_toes'], LEXICON_REPETITIONS_lOWER_LEG['lifting_on_socks_sitting'],
                           LEXICON['more_approach_gym']]), StateFilter(MuscleGroup.lower_leg_gym))
async def write_repetitions(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=message.text)
    await message.answer('Запишите количество повторений')
    await state.set_state(Approaches.start_repet_gym)


@router.message(StateFilter(MuscleGroup.lower_leg_gym))
async def warning_not_change(message: Message):
    await message.answer('Пожалуйста, воспользуйтесь кнопками!\n\n'
                         'Если вы хотите прервать ввод данных - '
                         'отправьте команду /cancel', reply_markup=lower_leg_kb_gym)

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
        await state.set_state(Change_muscle.change_muscle_gym)




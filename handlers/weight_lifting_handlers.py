from aiogram import Router
from aiogram.filters import Text, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards_repetitions import weight_lifting_kb
from states.states import Training_weight_lift
from datetime import datetime, date
from lexicon.lexicon_ru import LEXICON_WEIGHT_LIFTING_REPETIT
from database.database import Request
from keyboards.keyboard_utils import more_end_repet_workout

router: Router = Router()

@router.callback_query(Text(text=['weight_lifting']))
async def repetitions_selection(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали гири.\nВыберите упражнение',
                                  reply_markup=weight_lifting_kb)
    await state.set_state(Training_weight_lift.change_weight)

@router.callback_query(Text(text=['push_with_two_hands', 'push_with_one_hand', 'chest_push_with_both_hands',
                                  'chest_thrust_with_one_hand', 'two_hand_press', 'one_hand_press',
                                  'chest_press_with_two_hands', 'chest_press_with_one_hand', 'schwung',
                                  'two_handed_jerk', 'jerk_with_one_hand', 'chest_lift','sit_ups',
                                  'swing_kettlebell_forward']), StateFilter(Training_weight_lift.change_weight))
async def write_repetition(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_id=callback.from_user.id)
    await state.update_data(date_train=datetime.now().date())
    await state.update_data(name=LEXICON_WEIGHT_LIFTING_REPETIT[callback.data])
    await callback.message.answer('Запишите количество повторений')
    await state.set_state(Training_weight_lift.change_number_of_repetitions)

@router.message(StateFilter(Training_weight_lift.change_number_of_repetitions))
async def write_approaches(message: Message, state: FSMContext):
    await state.update_data(repetitions=message.text)
    data = await state.get_data()
    repetit = data['repetitions']
    if repetit.isdigit():
        await message.answer('Запишите вес')
        await state.set_state(Training_weight_lift.change_number_of_weight)
    else:
        await message.answer('Количество повторений должно быть числом.\n'
                             'Пожалуйста, введите данные заново', reply_markup=weight_lifting_kb)


@router.message(StateFilter(Training_weight_lift.change_number_of_weight))
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
                              'Пожалуйста, введите данные заново', reply_markup=weight_lifting_kb)
        # await state.set_state(Training_weight_lift.change_gym)
















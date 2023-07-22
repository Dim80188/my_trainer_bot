from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS

button_back: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['back'])
button_chest: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['chest'])
button_shoulders: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['shoulders'])
button_biceps: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['biceps'])
button_triceps: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['triceps'])
button_press: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['press'])
button_thigh: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['thigh'])
button_lower_leg: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['lower_leg'])

muscle_group_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
muscle_group_builder.row(button_back, button_chest, button_shoulders, button_biceps, button_triceps,
                         button_press, button_thigh,button_lower_leg, width=2)
muscle_group_kb: ReplyKeyboardMarkup = muscle_group_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['pull_ups'])
button_wide_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['wide_grip_pull_ups'])
button_parallel_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['parallel_grip_pull_ups'])
button_australian_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['australian_pull_ups'])

back_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
back_builder.row(button_pull_ups, button_wide_grip_pull_ups, button_parallel_grip_pull_ups, button_australian_pull_ups, width=2)
back_kb: ReplyKeyboardMarkup = back_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_push_ups_on: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['push_ups_on'])
button_push_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['push_ups'])
button_top_push_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['top_push_ups'])
button_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['bench_press'])

chest_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
chest_builder.row(button_push_ups_on, button_push_ups, button_top_push_ups, button_bench_press, width=2)
chest_kb: ReplyKeyboardMarkup = chest_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# button_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON['pull_ups'])
# button_push_ups: KeyboardButton = KeyboardButton(text=LEXICON['push_ups'])
# button_jump: KeyboardButton = KeyboardButton(text=LEXICON['jump'])
#
# repetititons_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# repetititons_builder.row(button_pull_ups, button_push_ups, button_jump, width=2)
#
# repetitions_kb: ReplyKeyboardMarkup = repetititons_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)
#
# button_yes: KeyboardButton = KeyboardButton(text=LEXICON['yes'])
# rep_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# rep_builder.row(button_yes)
# rep_kb: ReplyKeyboardMarkup = rep_builder.as_markup(resize_keyboard=True)



# repetitions_list = ReplyKeyboardMarkup(resize_keyboard=True)
# repetitions_list.add('Подтягивания').add('Отжимания').add('Прыжки')
#
# exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
# exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


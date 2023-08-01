from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS



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

button_bench_press_standing: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['bench_press_standing'])
button_bench_press_sitting: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['bench_press_sitting'])

shoulders_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
shoulders_builder.row(button_bench_press_sitting, button_bench_press_standing)
shoulders_kb: ReplyKeyboardMarkup = shoulders_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_reverse_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['reverse_grip_pull_ups'])
button_curling_arms_for_biceps: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['curling_arms_for_biceps'])

biceps_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
biceps_builder.row(button_curling_arms_for_biceps, button_reverse_grip_pull_ups)
biceps_kb: ReplyKeyboardMarkup = biceps_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


button_push_ups_between_benches: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['push_ups_between_benches'])

triceps_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
triceps_builder.row(button_push_ups_between_benches)
triceps_kb: ReplyKeyboardMarkup = triceps_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_torso_lift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['torso_lift'])
button_leg_lift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['leg_lift'])
button_twisting: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['twisting'])

press_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
press_builder.row(button_twisting, button_leg_lift, button_torso_lift)
press_kb: ReplyKeyboardMarkup = press_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_sit_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['sit_ups'])
button_jumping: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['jumping'])

thigh_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
thigh_builder.row(button_jumping, button_sit_ups)
thigh_kb: ReplyKeyboardMarkup = thigh_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_rise_on_toes: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS['rise_on_toes'])
lower_leg_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
lower_leg_builder.row(button_rise_on_toes)
lower_leg_kb: ReplyKeyboardMarkup = lower_leg_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

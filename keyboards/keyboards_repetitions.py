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


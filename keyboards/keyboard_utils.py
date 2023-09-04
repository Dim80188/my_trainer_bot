from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON, LEXICON_ACTIVITY
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_write: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['start_training'],
    callback_data='training'
)

button_show: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['show_statistic'],
    callback_data='statistic'
)

write_show_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
write_show_builder.row(button_write, button_show, width=1)
write_show_kb: InlineKeyboardMarkup = write_show_builder.as_markup()

button_weight_lifting: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_ACTIVITY['weight_lifting'],
    callback_data='weight_lifting'
)
button_workout: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_ACTIVITY['workout'],
    callback_data='workout'
)
button_gym: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_ACTIVITY['gym'],
    callback_data='gym'
)
activity_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
activity_builder.row(button_weight_lifting, button_workout, button_gym, width=1)
activity_kb: InlineKeyboardMarkup = activity_builder.as_markup()

button_more_workout: InlineKeyboardButton = InlineKeyboardButton(
    text='Продолжаем воркаут',
    callback_data='workout'
)
button_more_gym: InlineKeyboardButton = InlineKeyboardButton(
    text='Продолжаем зал',
    callback_data='gym'
)
button_more_weight_lifting: InlineKeyboardButton = InlineKeyboardButton(
    text='Продолжаем гири',
    callback_data='weight_lifting'
)

button_end_workout: InlineKeyboardButton = InlineKeyboardButton(
    text='Заканчиваем',
    callback_data='end_training'
)
more_end_repet_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
more_end_repet_builder.row(button_more_workout, button_more_gym, button_more_weight_lifting, button_end_workout, width=1)
more_end_repet_workout: InlineKeyboardMarkup = more_end_repet_builder.as_markup()














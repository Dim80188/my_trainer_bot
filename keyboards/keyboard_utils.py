from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON

button_write: KeyboardButton = KeyboardButton(text=LEXICON['start_training'])
button_show: KeyboardButton = KeyboardButton(text=LEXICON['show_statistic'])

write_show_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
write_show_builder.row(button_show, button_write, width=1)

write_show: ReplyKeyboardMarkup = write_show_builder.as_markup(resize_keyboard=True)

# кнопки записать еще подход или окончить упражнение
button_more_approach: KeyboardButton = KeyboardButton(text=LEXICON['more_approach'])
button_end_repet: KeyboardButton = KeyboardButton(text=LEXICON['end_repet'])

more_end_repet_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
more_end_repet_builder.row(button_more_approach, button_end_repet, width=1)
more_end_repet: ReplyKeyboardMarkup = more_end_repet_builder.as_markup(resize_keyboard=True)

# кнопки записать еще упраженниe или окончить тренировку
button_more: KeyboardButton = KeyboardButton(text=LEXICON['more_repet'])
button_end: KeyboardButton = KeyboardButton(text=LEXICON['end_training'])

more_end_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
more_end_builder.row(button_more, button_end, width=1)
more_end: ReplyKeyboardMarkup = more_end_builder.as_markup(resize_keyboard=True)

# exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
# exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


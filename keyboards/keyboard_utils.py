from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON

button_write: KeyboardButton = KeyboardButton(text=LEXICON['write_training'])
button_show: KeyboardButton = KeyboardButton(text=LEXICON['show_statistic'])

write_show_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
write_show_builder.row(button_show, button_write, width=1)

write_show: ReplyKeyboardMarkup = write_show_builder.as_markup(resize_keyboard=True)

# main = ReplyKeyboardMarkup(resize_keyboard=True)
# main.add('Записать данные тренировки').add('Вывести данные по тренировке')
#
# repetitions_list = ReplyKeyboardMarkup(resize_keyboard=True)
# repetitions_list.add('Подтягивания').add('Отжимания').add('Прыжки')
#
# exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
# exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


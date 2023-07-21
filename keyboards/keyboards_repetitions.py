from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON

button_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON['pull_ups'])
button_push_ups: KeyboardButton = KeyboardButton(text=LEXICON['push_ups'])
button_jump: KeyboardButton = KeyboardButton(text=LEXICON['jump'])

repetititons_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
repetititons_builder.row(button_push_ups, button_push_ups, button_jump, width=2)

repetitions_kb: ReplyKeyboardMarkup = repetititons_builder.as_markup(resize_keyboard=True)

button_yes: KeyboardButton = KeyboardButton(text=LEXICON['yes'])
rep_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
rep_builder.row(button_yes)
rep_kb: ReplyKeyboardMarkup = rep_builder.as_markup(resize_keyboard=True)



# repetitions_list = ReplyKeyboardMarkup(resize_keyboard=True)
# repetitions_list.add('Подтягивания').add('Отжимания').add('Прыжки')
#
# exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
# exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


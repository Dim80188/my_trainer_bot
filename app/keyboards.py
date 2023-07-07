from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Записать данные тренировки').add('Вывести данные по тренировке')

repetitions_list = ReplyKeyboardMarkup(resize_keyboard=True)
repetitions_list.add('Подтягивания').add('Отжимания').add('Прыжки')

exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


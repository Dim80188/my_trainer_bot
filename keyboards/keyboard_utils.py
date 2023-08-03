from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON, LEXICON_ACTIVITY

button_write: KeyboardButton = KeyboardButton(text=LEXICON['start_training'])
button_show: KeyboardButton = KeyboardButton(text=LEXICON['show_statistic'])

write_show_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
write_show_builder.row(button_show, button_write, width=1)

write_show: ReplyKeyboardMarkup = write_show_builder.as_markup(resize_keyboard=True)

# конпки да и нет
button_training: KeyboardButton = KeyboardButton(text=LEXICON['training'])
button_no_training: KeyboardButton = KeyboardButton(text=LEXICON['no_training'])
training_no_training_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
training_no_training_builder.row(button_training, button_no_training, width=1)
training_no_training: ReplyKeyboardMarkup = training_no_training_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# кнопки активности
button_aerobic: KeyboardButton = KeyboardButton(text=LEXICON_ACTIVITY['aerobic'])
button_workout: KeyboardButton = KeyboardButton(text=LEXICON_ACTIVITY['workout'])
button_gym: KeyboardButton = KeyboardButton(text=LEXICON_ACTIVITY['gym'])
activity_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
activity_builder.row(button_aerobic, button_gym, button_workout, width=1)
activity_kb: ReplyKeyboardMarkup = activity_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)


# кнопки записать еще подход или окончить упражнение
button_more_approach_workout: KeyboardButton = KeyboardButton(text=LEXICON['more_approach_workout'])
button_more_approach_gym: KeyboardButton = KeyboardButton(text=LEXICON['more_approach_gym'])
button_end_repet: KeyboardButton = KeyboardButton(text=LEXICON['end_repet'])

more_end_repet_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
more_end_repet_builder_workout.row(button_more_approach_workout, button_end_repet, width=1)
more_end_repet_workout: ReplyKeyboardMarkup = more_end_repet_builder_workout.as_markup(resize_keyboard=True)

more_end_repet_builder_gym: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
more_end_repet_builder_gym.row(button_more_approach_gym, button_end_repet, width=1)
more_end_repet_gym: ReplyKeyboardMarkup = more_end_repet_builder_gym.as_markup(resize_keyboard=True)

# кнопки записать еще упраженниe или окончить тренировку
button_more: KeyboardButton = KeyboardButton(text=LEXICON['more_repet'])
button_end: KeyboardButton = KeyboardButton(text=LEXICON['end_training'])

more_end_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
more_end_builder.row(button_more, button_end, width=1)
more_end: ReplyKeyboardMarkup = more_end_builder.as_markup(resize_keyboard=True)

# exercises_status = ReplyKeyboardMarkup(resize_keyboard=True)
# exercises_status.add('Записать еще упражненние').add('Окончить тренировку')


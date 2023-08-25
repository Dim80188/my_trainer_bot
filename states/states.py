from aiogram.filters.state import StatesGroup, State

class Training(StatesGroup):
    change_workout = State()
    change_exercises = State()
    change_number_of_repetitions = State()

class Training_gym(StatesGroup):
    change_gym = State()
    change_exercises = State()
    change_number_of_repetitions = State()
    change_number_of_weight = State()

class Show_statistic(StatesGroup):
    start_period = State()
    end_period = State()
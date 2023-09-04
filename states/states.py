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

class Training_weight_lift(StatesGroup):
    change_weight = State()
    change_number_of_repetitions = State()
    change_number_of_weight = State()

class Show_statistic(StatesGroup):
    start_period = State()
    end_period = State()

class Delete_data(StatesGroup):
    change_date = State()
    change_data = State()
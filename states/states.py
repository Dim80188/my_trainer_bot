from aiogram.filters.state import StatesGroup, State

class NewOrder(StatesGroup):
    start_training = State()
    show_statistic = State()
    # name = State()
    # repeat = State()

class MuscleGroup(StatesGroup):
    changed_muscle = State()
    back = State()
    chest = State()
    shoulders = State()
    biceps = State()
    triceps = State()
    press = State()
    thigh = State()
    lower_leg = State()


class Approaches(StatesGroup):
    start_repet = State()
    more_repet = State()
    end_repet = State()

class Show_statisitc(StatesGroup):
    st_period = State()
    end_period = State()

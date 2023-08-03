from aiogram.filters.state import StatesGroup, State

class NewOrder(StatesGroup):
    start_training = State()
    show_statistic = State()


class Activity(StatesGroup):
    activity_change = State()

class Change_muscle(StatesGroup):
    change_muscle_workout = State()
    change_muscle_gym = State()


class MuscleGroup(StatesGroup):
    changed_muscle = State()
    back = State()
    back_gym = State()
    chest = State()
    chest_gym = State()
    shoulders = State()
    shoulders_gym = State()
    biceps = State()
    biceps_gym = State()
    triceps = State()
    triceps_gym = State()
    press = State()
    press_gym = State()
    thigh = State()
    thigh_gym = State()
    lower_leg = State()
    lower_leg_gym = State()


class Approaches(StatesGroup):
    start_repet_workout = State()
    start_repet_gym = State()
    more_repet_workout = State()
    more_repet_gym = State()
    end_repet = State()

class Show_statisitc(StatesGroup):
    st_period = State()
    end_period = State()

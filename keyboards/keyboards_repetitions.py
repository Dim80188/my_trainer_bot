from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON, LEXICON_MUSCLE, LEXICON_REPETITIONS_PRESS, LEXICON_REPETITIONS_THIGH, LEXICON_REPETITIONS_TRICEPS, LEXICON_REPETITIONS_BACK, LEXICON_REPETITIONS_BICEPS, LEXICON_REPETITIONS_CHEST, LEXICON_REPETITIONS_SHOULDERS, LEXICON_REPETITIONS_lOWER_LEG, LEXICON_ACTIVITY

button_back: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['back'])
button_chest: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['chest'])
button_shoulders: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['shoulders'])
button_biceps: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['biceps'])
button_triceps: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['triceps'])
button_press: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['press'])
button_thigh: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['thigh'])
button_lower_leg: KeyboardButton = KeyboardButton(text=LEXICON_MUSCLE['lower_leg'])

muscle_group_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
muscle_group_builder.row(button_back, button_chest, button_shoulders, button_biceps, button_triceps,
                         button_press, button_thigh,button_lower_leg, width=2)
muscle_group_kb: ReplyKeyboardMarkup = muscle_group_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['pull_ups'])
button_wide_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['wide_grip_pull_ups'])
button_parallel_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['parallel_grip_pull_ups'])
button_australian_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['australian_pull_ups'])
button_curved_bar_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['curved_bar_pull_ups'])
button_bent_over_row: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['bent_over_row'])
button_bent_over_dumbbell_row: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['bent_over_dumbbell_row'])
button_upper_block_pull: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['upper_block_pull'])
button_lower_block_pull: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['lower_block_pull'])
button_deadlift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['deadlift'])
button_deadlift_st: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['deadlift_st'])
button_sumo_deadlift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['sumo_deadlift'])
button_shrugs: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['shrugs'])
button_hyperextension: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BACK['hyperextension'])

back_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
back_builder_workout.row(button_pull_ups, button_wide_grip_pull_ups, button_parallel_grip_pull_ups, button_australian_pull_ups, width=2)
back_kb_workout: ReplyKeyboardMarkup = back_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)

back_builder_gym: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
back_builder_gym.row(button_pull_ups, button_wide_grip_pull_ups, button_parallel_grip_pull_ups, button_curved_bar_pull_ups,
                     button_bent_over_row, button_bent_over_dumbbell_row, button_upper_block_pull, button_lower_block_pull,
                     button_deadlift, button_deadlift_st, button_sumo_deadlift, button_shrugs, button_hyperextension)
back_kb_gym: ReplyKeyboardMarkup = back_builder_gym.as_markup(one_time_keyboard=True, resize_keyboard=True)


button_push_ups_on: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['push_ups_on'])
button_push_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['push_ups'])
button_top_push_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['top_push_ups'])
button_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['bench_press'])
button_incline_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['incline_bench_press'])
button_dumbbell_laying: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['dumbbell_laying'])
button_head_up_dumbbell_raises: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['head_up_dumbbell_raises'])
button_mixing_hands_on_the_simulator: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_CHEST['mixing_hands_on_the_simulator'])


chest_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
chest_builder_workout.row(button_push_ups_on, button_push_ups, button_top_push_ups, button_bench_press, width=2)
chest_kb_workout: ReplyKeyboardMarkup = chest_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_bench_press_standing: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['bench_press_standing'])
button_bench_press_sitting: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['bench_press_sitting'])
button_chin_pull: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['chin_pull'])
button_swing_forward: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['swing_forward'])
button_swing_to_the_side: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['swing_to_the_side'])
button_tilt_swing: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['tilt_swing'])

shoulders_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
shoulders_builder_workout.row(button_bench_press_sitting, button_bench_press_standing)
shoulders_kb_workout: ReplyKeyboardMarkup = shoulders_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_reverse_grip_pull_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['reverse_grip_pull_ups'])
button_curling_arms_for_biceps: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_for_biceps'])
button_barbell_curl: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['barbell_curl'])
button_curling_arms_with_dumbbells: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_with_dumbbells'])
button_sitting_dumbbell_сurl: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['sitting_dumbbell_сurl'])
button_curls_with_dumbbells_sitting_on_an_incline_bench: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curls_with_dumbbells_sitting_on_an_incline_bench'])
button_barbell_curl_on_scott_bench: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['barbell_curl_on_scott_bench'])
button_curling_arms_with_a_dumbbell_on_a_scott_bench: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_with_a_dumbbell_on_a_scott_bench'])
button_bending_the_arms_with_a_curved_neck_on_the_scott_bench: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['bending_the_arms_with_a_curved_neck_on_the_scott_bench'])
button_bending_arms_with_a_curved_neck: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['bending_arms_with_a_curved_neck'])
button_concentrated_curls: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_BICEPS['concentrated_curls'])


biceps_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
biceps_builder_workout.row(button_curling_arms_for_biceps, button_reverse_grip_pull_ups)
biceps_kb_workout: ReplyKeyboardMarkup = biceps_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)


button_push_ups_between_benches: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['push_ups_between_benches'])
button_french_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['french_bench_press'])
button_standing_french_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['standing_french_bench_press'])
button_dumbbell_french_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['dumbbell_french_press'])
button_narrow_grip_bench_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['narrow_grip_bench_press'])
button_extension_of_arms_on_the_block: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block'])
button_extension_of_arms_on_the_block_with_a_reverse_grip: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_a_reverse_grip'])
button_extension_of_arms_on_the_block_with_one_hand: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_one_hand'])
button_concentrated_extension: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['concentrated_extension'])

triceps_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
triceps_builder_workout.row(button_push_ups_between_benches)
triceps_kb_workout: ReplyKeyboardMarkup = triceps_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_torso_lift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_PRESS['torso_lift'])
button_leg_lift: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_PRESS['leg_lift'])
button_twisting: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_PRESS['twisting'])

press_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
press_builder.row(button_twisting, button_leg_lift, button_torso_lift)
press_kb: ReplyKeyboardMarkup = press_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_sit_ups: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['sit_ups'])
button_squats_on_one_leg: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['squats_on_one_leg'])
button_jumping: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['jumping'])
button_leg_press: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_press'])
button_leg_extension: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_extension'])
button_leg_curl: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_curl'])

thigh_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
thigh_builder_workout.row(button_jumping, button_sit_ups, button_squats_on_one_leg)
thigh_kb_workout: ReplyKeyboardMarkup = thigh_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)

button_rise_on_toes: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_lOWER_LEG['rise_on_toes'])
button_lifting_on_socks_sitting: KeyboardButton = KeyboardButton(text=LEXICON_REPETITIONS_lOWER_LEG['lifting_on_socks_sitting'])

lower_leg_builder_workout: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
lower_leg_builder_workout.row(button_rise_on_toes)
lower_leg_kb_workout: ReplyKeyboardMarkup = lower_leg_builder_workout.as_markup(one_time_keyboard=True, resize_keyboard=True)



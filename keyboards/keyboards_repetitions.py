from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import (LEXICON_MUSCLE, LEXICON_REPETITIONS_BACK, LEXICON_REPETITIONS_CHEST, LEXICON_REPETITIONS_SHOULDERS,
                                LEXICON_REPETITIONS_BICEPS, LEXICON_REPETITIONS_TRICEPS, LEXICON_REPETITIONS_PRESS,
                                LEXICON_REPETITIONS_LOWER_LEG, LEXICON_REPETITIONS_THIGH, LEXICON_WEIGHT_LIFTING_REPETIT)
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_back: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['back'],
    callback_data='back'
)
button_chest: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['chest'],
    callback_data='chest'
)
button_shoulders: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['shoulders'],
    callback_data='shoulders'
)
button_biceps: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['biceps'],
    callback_data='biceps'
)
button_triceps: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['triceps'],
    callback_data='triceps'
)
button_press: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['press'],
    callback_data='press'
)
button_thigh: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['thigh'],
    callback_data='thigh'
)
button_lower_leg: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_MUSCLE['lower_leg'],
    callback_data='lower_leg'
)
muscle_group_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
muscle_group_builder.row(button_back, button_chest, button_shoulders,
                         button_biceps, button_triceps, button_press, button_thigh,
                         button_lower_leg, width=2)
muscle_group_kb: InlineKeyboardMarkup = muscle_group_builder.as_markup()

button_pull_ups: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['pull_ups'],
    callback_data='pull_ups'
)
button_wide_grip_pull_ups: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['wide_grip_pull_ups'],
    callback_data='wide_grip_pull_ups'
)
button_parallel_grip_pull_ups: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['parallel_grip_pull_ups'],
    callback_data='parallel_grip_pull_ups')
button_australian_pull_ups: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['australian_pull_ups'],
    callback_data='australian_pull_ups')
button_curved_bar_pull_ups: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['curved_bar_pull_ups'],
    callback_data='urved_bar_pull_ups')
button_bent_over_row: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['bent_over_row'],
    callback_data='bent_over_row')
button_bent_over_dumbbell_row: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['bent_over_dumbbell_row'],
    callback_data='bent_over_dumbbell_row')
button_upper_block_pull: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['upper_block_pull'],
    callback_data='upper_block_pull')
button_lower_block_pull: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['lower_block_pull'],
    callback_data='lower_block_pull')
button_deadlift: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['deadlift'],
    callback_data='deadlift')
button_deadlift_st: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['deadlift_st'],
    callback_data='deadlift_st')
button_sumo_deadlift: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['sumo_deadlift'],
    callback_data='sumo_deadlift')
button_shrugs: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['shrugs'],
    callback_data='shrugs')
button_hyperextension: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_REPETITIONS_BACK['hyperextension'],
    callback_data='hyperextension')

back_builder_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
back_builder_workout.row(button_pull_ups, button_wide_grip_pull_ups, button_parallel_grip_pull_ups,
                         button_australian_pull_ups, button_curved_bar_pull_ups, width=1)
back_kb_workout: InlineKeyboardMarkup = back_builder_workout.as_markup()
back_builder_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
back_builder_gym.row(button_pull_ups, button_wide_grip_pull_ups, button_parallel_grip_pull_ups, button_australian_pull_ups,
                     button_curved_bar_pull_ups, button_bent_over_row, button_bent_over_dumbbell_row, button_upper_block_pull,
                     button_lower_block_pull, button_deadlift, button_deadlift_st, button_sumo_deadlift, button_shrugs, button_hyperextension, width=1)
back_kb_gym: InlineKeyboardMarkup = back_builder_gym.as_markup()


button_push_ups_on: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['push_ups_on'], callback_data='push_ups_on')
button_push_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['push_ups'], callback_data='push_ups')
button_top_push_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['top_push_ups'], callback_data='top_push_ups')
button_bench_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['bench_press'], callback_data='bench_press')
button_incline_bench_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['incline_bench_press'], callback_data='incline_bench_press')
button_dumbbell_laying: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['dumbbell_laying'], callback_data='dumbbell_laying')
button_head_up_dumbbell_raises: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['head_up_dumbbell_raises'], callback_data='head_up_dumbbell_raises')
button_mixing_hands_on_the_simulator: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_CHEST['mixing_hands_on_the_simulator'], callback_data='mixing_hands_on_the_simulator')

chest_builder_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
chest_builder_workout.row(button_push_ups_on, button_push_ups, button_top_push_ups, width=1)
chest_kb_workout: InlineKeyboardMarkup = chest_builder_workout.as_markup()
chest_builder_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
chest_builder_gym.row(button_push_ups_on, button_bench_press, button_incline_bench_press,
                      button_dumbbell_laying, button_head_up_dumbbell_raises,
                      button_mixing_hands_on_the_simulator, width=1)
chest_kb_gym: InlineKeyboardMarkup = chest_builder_gym.as_markup()


button_bench_press_standing: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['bench_press_standing'], callback_data='bench_press_standing')
button_bench_press_sitting: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['bench_press_sitting'], callback_data='bench_press_sitting')
button_chin_pull: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['chin_pull'], callback_data='chin_pull')
button_swing_forward: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['swing_forward'], callback_data='swing_forward')
button_swing_to_the_side: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['swing_to_the_side'], callback_data='swing_to_the_side')
button_tilt_swing: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_SHOULDERS['tilt_swing'], callback_data='tilt_swing')

shoulders_builders_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
shoulders_builders_workout.row(button_bench_press_standing)
shoulders_kb_workout: InlineKeyboardMarkup = shoulders_builders_workout.as_markup()

shoulders_builders_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
shoulders_builders_gym.row(button_bench_press_standing, button_bench_press_sitting, button_chin_pull, button_swing_forward,
                           button_swing_to_the_side, button_tilt_swing, width=1)
shoulders_kb_gym: InlineKeyboardMarkup = shoulders_builders_gym.as_markup()

button_reverse_grip_pull_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['reverse_grip_pull_ups'], callback_data='reverse_grip_pull_ups')
button_curling_arms_for_biceps: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_for_biceps'], callback_data='curling_arms_for_biceps')
button_barbell_curl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['barbell_curl'], callback_data='barbell_curl')
button_curling_arms_with_dumbbells: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_with_dumbbells'], callback_data='curling_arms_with_dumbbells')
button_sitting_dumbbell_сurl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['sitting_dumbbell_сurl'], callback_data='sitting_dumbbell_сurl')
button_curls_with_dumbbells_sitting_on_an_incline_bench: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curls_with_dumbbells_sitting_on_an_incline_bench'], callback_data='curls_with_dumbbells_sitting_on_an_incline_bench')
button_barbell_curl_on_scott_bench: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['barbell_curl_on_scott_bench'], callback_data='barbell_curl_on_scott_bench')
button_curling_arms_with_a_dumbbell_on_a_scott_bench: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['curling_arms_with_a_dumbbell_on_a_scott_bench'], callback_data='curling_arms_with_a_dumbbell_on_a_scott_bench')
button_bending_the_arms_with_a_curved_neck_on_the_scott_bench: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['bending_the_arms_with_a_curved_neck_on_the_scott_bench'], callback_data='bending_the_arms_with_a_curved_neck_on_the_scott_bench')
button_bending_arms_with_a_curved_neck: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['bending_arms_with_a_curved_neck'], callback_data='bending_arms_with_a_curved_neck')
button_concentrated_curls: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_BICEPS['concentrated_curls'], callback_data='concentrated_curls')

biceps_builders_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
biceps_builders_workout.row(button_reverse_grip_pull_ups)
biceps_kb_workout: InlineKeyboardMarkup = biceps_builders_workout.as_markup()

biceps_builders_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
biceps_builders_gym.row(button_reverse_grip_pull_ups, button_curling_arms_for_biceps, button_barbell_curl,
                        button_curling_arms_with_dumbbells, button_sitting_dumbbell_сurl, button_curls_with_dumbbells_sitting_on_an_incline_bench,
                        button_barbell_curl_on_scott_bench, button_curling_arms_with_a_dumbbell_on_a_scott_bench,
                        button_bending_the_arms_with_a_curved_neck_on_the_scott_bench, button_bending_arms_with_a_curved_neck,
                        button_concentrated_curls, width=1)
biceps_kb_gym: InlineKeyboardMarkup = biceps_builders_gym.as_markup()

button_push_ups_between_benches: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['push_ups_between_benches'], callback_data='push_ups_between_benches')
button_narrow_grip_push_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['narrow_grip_push-ups'], callback_data='narrow_grip_push-ups')
button_french_bench_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['french_bench_press'], callback_data='french_bench_press')
button_standing_french_bench_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['standing_french_bench_press'], callback_data='standing_french_bench_press')
button_dumbbell_french_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['dumbbell_french_press'], callback_data='dumbbell_french_press')
button_narrow_grip_bench_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['narrow_grip_bench_press'], callback_data='narrow_grip_bench_press')
button_extension_of_arms_on_the_block: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block'], callback_data='extension_of_arms_on_the_block')
button_extension_of_arms_on_the_block_with_a_reverse_grip: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_a_reverse_grip'], callback_data='extension_of_arms_on_the_block_with_a_reverse_grip')
button_extension_of_arms_on_the_block_with_one_hand: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['extension_of_arms_on_the_block_with_one_hand'], callback_data='extension_of_arms_on_the_block_with_one_hand')
button_concentrated_extension: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_TRICEPS['concentrated_extension'], callback_data='concentrated_extension')

triceps_builders_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
triceps_builders_workout.row(button_push_ups_between_benches, button_narrow_grip_push_ups, width=1)
triceps_kb_workout: InlineKeyboardMarkup = triceps_builders_workout.as_markup()

triceps_builders_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
triceps_builders_gym.row(button_push_ups_between_benches, button_french_bench_press, button_standing_french_bench_press,
                         button_dumbbell_french_press, button_narrow_grip_bench_press, button_extension_of_arms_on_the_block,
                         button_extension_of_arms_on_the_block_with_a_reverse_grip, button_extension_of_arms_on_the_block_with_one_hand,
                         button_concentrated_extension, width=1)
triceps_kb_gym: InlineKeyboardMarkup = triceps_builders_gym.as_markup()

button_torso_lift: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_PRESS['torso_lift'], callback_data='torso_lift')
button_leg_lift: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_PRESS['leg_lift'], callback_data='leg_lift')
button_twisting: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_PRESS['twisting'], callback_data='twisting')

press_builder_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
press_builder_workout.row(button_torso_lift, button_leg_lift, button_twisting, width=1)
press_kb_workout: InlineKeyboardMarkup = press_builder_workout.as_markup()

press_builder_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
press_builder_gym.row(button_torso_lift, button_leg_lift, button_twisting, width=1)
press_kb_gym: InlineKeyboardMarkup = press_builder_gym.as_markup()


button_sit_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['sit_ups'], callback_data='sit_ups')
button_squats_on_one_leg: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['squats_on_one_leg'], callback_data='squats_on_one_leg')
button_jumping: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['jumping'], callback_data='jumping')
button_leg_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_press'], callback_data='leg_press')
button_leg_extension: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_extension'], callback_data='leg_extension')
button_leg_curl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_THIGH['leg_curl'], callback_data='leg_curl')

thigh_builder_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
thigh_builder_workout.row(button_sit_ups, button_squats_on_one_leg, button_jumping, width=1)
thigh_kb_workout: InlineKeyboardMarkup = thigh_builder_workout.as_markup()

thigh_builder_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
thigh_builder_gym.row(button_sit_ups, button_leg_press, button_leg_extension, button_leg_curl, width=1)
thigh_kb_gym: InlineKeyboardMarkup = thigh_builder_gym.as_markup()

button_rise_on_toes: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_LOWER_LEG['rise_on_toes'], callback_data='rise_on_toes')
button_lifting_on_socks_sitting: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_REPETITIONS_LOWER_LEG['lifting_on_socks_sitting'], callback_data='lifting_on_socks_sitting')

lower_leg_builder_workout: InlineKeyboardBuilder = InlineKeyboardBuilder()
lower_leg_builder_workout.row(button_rise_on_toes)
lower_leg_kb_workout: InlineKeyboardMarkup = lower_leg_builder_workout.as_markup()

lower_leg_builder_gym: InlineKeyboardBuilder = InlineKeyboardBuilder()
lower_leg_builder_gym.row(button_rise_on_toes, button_lifting_on_socks_sitting, width=1)
lower_leg_kb_gym: InlineKeyboardMarkup = lower_leg_builder_gym.as_markup()

button_push_with_two_hands: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['push_with_two_hands'], callback_data='push_with_two_hands')
button_push_with_one_hand: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['push_with_one_hand'], callback_data='push_with_one_hand')
button_chest_push_with_both_hands: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['chest_push_with_both_hands'], callback_data='chest_push_with_both_hands')
button_chest_thrust_with_one_hand: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['chest_thrust_with_one_hand'], callback_data='chest_thrust_with_one_hand')
button_two_hand_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['two_hand_press'], callback_data='two_hand_press')
button_one_hand_press: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['one_hand_press'], callback_data='one_hand_press')
button_chest_press_with_two_hands: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['chest_press_with_two_hands'], callback_data='chest_press_with_two_hands')
button_chest_press_with_one_hand: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['chest_press_with_one_hand'], callback_data='chest_press_with_one_hand')
button_schwung: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['schwung'], callback_data='schwung')
button_two_handed_jerk: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['two_handed_jerk'], callback_data='two_handed_jerk')
button_jerk_with_one_hand: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['jerk_with_one_hand'], callback_data='jerk_with_one_hand')
button_chest_lift: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['chest_lift'], callback_data='chest_lift')
button_sit_ups: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['sit_ups'], callback_data='sit_ups')
button_swing_kettlebell_forward: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_WEIGHT_LIFTING_REPETIT['swing_kettlebell_forward'], callback_data='swing_kettlebell_forward')

weight_lifting_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
weight_lifting_builder.row(button_push_with_two_hands, button_push_with_one_hand, button_chest_push_with_both_hands, button_chest_thrust_with_one_hand,
                           button_two_hand_press, button_one_hand_press, button_chest_press_with_two_hands, button_chest_press_with_one_hand,
                           button_schwung, button_two_handed_jerk, button_jerk_with_one_hand, button_chest_lift, button_sit_ups, button_swing_kettlebell_forward, width=1)
weight_lifting_kb: InlineKeyboardMarkup = weight_lifting_builder.as_markup()
























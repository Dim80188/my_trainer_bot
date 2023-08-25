LEXICON: dict[str, str] = {
    '/start': '<b>Привет!</b>\n\nВ этом боте ты можешь вести тренировочный дневник.\n\nЧтобы посмотреть '
              'список доступных команд - набери /help',
    'start_training': 'Начать тренировку',
    'show_statistic': 'Вывести данные по тренировкам',
    'training': 'тренировку!',
    'no_training': 'тренировка не сейчас',
    'repetition': 'внести повторения',
    'more_approach_workout': 'продолжаем воркаут',
    'more_approach_gym': 'продолжаем тренажерку',
    'end_repet': 'нет, заканчиваем',
    'more_repet': 'записать новое упражнение',
    'end_training': 'окончить тренировку'
}

LEXICON_ACTIVITY: dict[str, str] = {
    'aerobic': 'аэробная',
    'workout': 'воркаут',
    'gym': 'тренажерный зал',
}


LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'запустить бота',
    '/help': 'получить справку о работе бота',
    '/cancel': 'прервать работу бота'
}

LEXICON_MUSCLE: dict[str, str] = {
    'back': 'спина',
    'chest': 'грудь',
    'shoulders': 'плечи',
    'biceps': 'бицепс',
    'triceps': 'трицепс',
    'press': 'пресс',
    'thigh': 'бедра',
    'lower_leg': 'голень'
}
LEXICON_REPETITIONS_BACK: dict[str, str] = {
    'pull_ups': 'подтягивания',
    'wide_grip_pull_ups': 'подтягивания широким хватом',
    'parallel_grip_pull_ups': 'подтягивания параллельным хватом',
    'australian_pull_ups': 'австралийские подтягивания',
    'curved_bar_pull_ups': 'подтягивания на изогнутом грифе',
    'bent_over_row': 'тяга штанги в наклоне ',
    'bent_over_dumbbell_row': 'тяга гантели в наклоне',
    'upper_block_pull': 'тяга верхнего блока',
    'lower_block_pull': 'тяга нижнего блока',
    'deadlift': 'мертвая тяга',
    'deadlift_st': 'становая тяга',
    'sumo_deadlift': 'тяга сумо',
    'shrugs': 'шраги',
    'hyperextension': 'гиперэкстензия',
}
LEXICON_REPETITIONS_CHEST: dict[str, str] = {
    'push_ups_on': 'отжимания на брусьях',
    'push_ups': 'отжимания',
    'top_push_ups': 'верхние отжимания',
    'bench_press': 'жим лежа',
    'incline_bench_press': 'жим лежа на наклонной скамье',
    'dumbbell_laying': 'разводки гантелями лежа',
    'head_up_dumbbell_raises': 'разводки гантелями головой вверх',
    'mixing_hands_on_the_simulator': 'сведение рук на тренажере',
}
LEXICON_REPETITIONS_SHOULDERS: dict[str, str] = {
    'bench_press_standing': 'жим стоя',
    'bench_press_sitting': 'жим сидя',
    'chin_pull': 'тяга к подбородку',
    'swing_forward': 'мах вперед',
    'swing_to_the_side': 'мах в стороны',
    'tilt_swing': 'махи в наклоне',
}
LEXICON_REPETITIONS_BICEPS: dict[str, str] = {
    'reverse_grip_pull_ups': 'подтягивания обратным хватом',
    'curling_arms_for_biceps': 'сгибание рук на бицепс',
    'barbell_curl': 'сгибание рук со штангой',
    'curling_arms_with_dumbbells': 'сгибание рук с гантелями',
    'sitting_dumbbell_сurl': 'сгибание рук с гантелями сидя',
    'curls_with_dumbbells_sitting_on_an_incline_bench': 'сгибание рук с гантелями сидя на наклонной скамье',
    'barbell_curl_on_scott_bench': 'сгибание рук со штангой на скамье скотта',
    'curling_arms_with_a_dumbbell_on_a_scott_bench': 'сгибание рук с гантелью на скамье скотта',
    'bending_the_arms_with_a_curved_neck_on_the_scott_bench': 'сгибание рук с изогнутым грифом на скамье скотта',
    'bending_arms_with_a_curved_neck': 'сгибание рук с изогнутым грифом',
    'concentrated_curls': 'концентрированные сгибания',
}
LEXICON_REPETITIONS_TRICEPS: dict[str, str] = {
    'push_ups_between_benches': 'отжимания между скамьями',
    'french_bench_press': 'французский жим со штангой лежа',
    'standing_french_bench_press': 'французский жим со штангой стоя',
    'dumbbell_french_press': 'французский жим с гантелью',
    'narrow_grip_bench_press': 'жим лежа узким хватом',
    'extension_of_arms_on_the_block': 'разгибание рук на блоке',
    'extension_of_arms_on_the_block_with_a_reverse_grip': 'разгибание рук на блоке обратным хватом',
    'extension_of_arms_on_the_block_with_one_hand': 'разгибание рук на блоке одной рукой',
    'concentrated_extension': 'концентрированное разгибание',
}
LEXICON_REPETITIONS_PRESS: dict[str, str] = {
    'torso_lift': 'подъем туловища',
    'leg_lift': 'подъем ног',
    'twisting': 'скручивания',
}
LEXICON_REPETITIONS_THIGH: dict[str, str] = {
    'sit_ups': 'приседания',
    'squats_on_one_leg': 'приседания на одной ноге',
    'jumping': 'прыжки',
    'leg_press': 'жим ногами',
    'leg_extension': 'разгибание ног',
    'leg_curl': 'сгибание ног',
}
LEXICON_REPETITIONS_LOWER_LEG: dict[str, str] = {
    'rise_on_toes': 'подъем на носки',
    'lifting_on_socks_sitting': 'подъем на носи сидя',
}

LEXICON_AEROBIC: dict[str, str] = {
    'run': 'бег',
    'a_ride_on_the_bicycle': 'езда на велосипеде',
    'swimming': 'плавание',

}
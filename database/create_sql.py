CREATE_EXERCISES_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS exercises(
        user_id bigint,
        date_train date,
        name text,
        repetitions integer,
        weight real
    );
    """
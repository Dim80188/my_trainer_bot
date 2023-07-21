import sqlite3 as sq

db = sq.connect('fit.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS exercises("
                "e_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "user INTEGER, "
                "date DATE, "
                "name TEXT, "
                "repetitions INTEGER)")
    db.commit()

async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()

async def add_exerc(data):

    cur.execute("INSERT INTO exercises (user, date, name, repetitions) VALUES (?, ?, ?, ?)",
                    (data['user'], data['date'], data['name'], data['repetitions']))
    db.commit()
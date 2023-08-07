from typing import List, Tuple, Any
import asyncpg
from asyncpg import Record
from datetime import datetime

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

# import sqlite3 as sq
#
#
# db = sq.connect('fit.db')
# cur = db.cursor()

# async def db_start():
#     cur.execute("CREATE TABLE IF NOT EXISTS accounts("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                 "tg_id INTEGER, "
#                 "cart_id TEXT)")
#     cur.execute("CREATE TABLE IF NOT EXISTS exercises("
#                 "e_id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                 "user INTEGER, "
#                 "date DATE, "
#                 "name TEXT, "
#                 "repetitions INTEGER)")
#     db.commit()

    # async def cmd_start_db(self, user_id):
    #     user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    #     if not user:
    #         cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
    #         db.commit()

    async def add_exerc(self, data):

        await self.connector.execute('''INSERT INTO exercises (user_id, date_train, name, repetitions, weight) VALUES ($1, $2, $3, $4, $5)''',
                                     data['user_id'], data['date_train'], data['name'], int(data['repetitions']), float(data['weight']))

    async def sql_read(self, period_id, period):
        sql_id = period_id
        sql_start = period['start_period']
        sql_end = period['end_period']
        # ret = cur.execute(f'SELECT * FROM exercises WHERE date == ({sql_start}) AND date <= ({sql_end})').fetchone()

        ret = await self.connector.fetch(f"SELECT * FROM exercises WHERE user_id = $1 AND date_train BETWEEN $2 AND $3", sql_id, sql_start, sql_end)
        return ret



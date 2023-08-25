import asyncpg

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_exerc(self, data):
        await self.connector.execute('''INSERT INTO exercises (user_id, date_train, name, repetitions, weight) VALUES ($1, $2, $3, $4, $5)''',
                                     data['user_id'], data['date_train'], data['name'], int(data['repetitions']), float(data['weight']))

    async def sql_read(self, period_id, period):
        sql_id = period_id
        sql_start = period['start_period']
        sql_end = period['end_period']
        ret = await self.connector.fetch(f"SELECT * FROM exercises WHERE user_id = $1 AND date_train BETWEEN $2 AND $3",
                                         sql_id, sql_start, sql_end)
        return ret





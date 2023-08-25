from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tb_bot: TgBot
    db: DatabaseConfig

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tb_bot=TgBot(token=env('BOT_TOKEN')),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))
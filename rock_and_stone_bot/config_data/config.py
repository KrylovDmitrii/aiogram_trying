import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    return Config(tg_bot=TgBot(os.getenv("BOT_TOKEN")))

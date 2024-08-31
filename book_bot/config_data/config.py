import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class Tg_bot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: Tg_bot


def load_config() -> Config:
    return Config(
        tg_bot=Tg_bot(
            token=os.getenv("BOT_TOKEN"),
            admin_id=int(os.getenv("ADMIN_ID"))
        )
    )

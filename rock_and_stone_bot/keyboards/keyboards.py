from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from rock_and_stone_bot.lexicon.lexicon_ru import LEXICON_RU

yes_button = KeyboardButton(text=LEXICON_RU.get('yes_button'))
nope_button = KeyboardButton(text=LEXICON_RU.get('no_button'))
stats_button = KeyboardButton(text=LEXICON_RU.get('stats_button'))

game_status = ReplyKeyboardBuilder()

game_status.row(yes_button, nope_button, stats_button, width=3)

game_status_kb: ReplyKeyboardMarkup = game_status.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

rock_button = KeyboardButton(text=LEXICON_RU.get('rock'))
paper_button = KeyboardButton(text=LEXICON_RU.get('paper'))
scissors_button = KeyboardButton(text=LEXICON_RU.get('scissors'))

game_items = ReplyKeyboardBuilder()

game_items.row(rock_button, paper_button, scissors_button, width=3)

game_items_kb: ReplyKeyboardMarkup = game_items.as_markup(
    resize_keyboard=True,
)

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from rock_and_stone_bot.lexicon.lexicon_ru import LEXICON_RU
from rock_and_stone_bot.keyboards.keyboards import game_status_kb, game_items_kb
from rock_and_stone_bot.services.services import get_bot_choice, get_winner

router = Router()

user_stats = {}


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU.get('/start'), reply_markup=game_status_kb)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU.get('/help'), reply_markup=game_status_kb)


@router.message(F.text == LEXICON_RU.get('stats_button'))
async def process_stats_command(message: Message):
    user_id = message.from_user.id
    stats = user_stats.get(user_id, {'wins': 0, 'losses': 0, 'draws': 0})
    await message.answer(
        text=f"Ваша статистика:\nПобеды: {stats['wins']}\n"
             f"Поражения: {stats['losses']}\nНичьи: {stats['draws']}\nХотите еще сыграть?",
        reply_markup=game_status_kb
    )


@router.message(F.text == LEXICON_RU.get('yes_button'))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU.get('yes'), reply_markup=game_items_kb)


@router.message(F.text == LEXICON_RU.get('no_button'))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU.get('no'))


@router.message(F.text.in_([LEXICON_RU.get('rock'), LEXICON_RU.get('paper'), LEXICON_RU.get('scissors')]))
async def process_game_answer(message: Message):
    bot_answer = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU.get('bot_choice')} - {LEXICON_RU.get(bot_answer)}")
    winner = get_winner(message.text, bot_answer)
    await message.answer(text=LEXICON_RU.get(winner), reply_markup=game_status_kb)

    user_id = message.from_user.id

    if user_id not in user_stats:
        user_stats[user_id] = {'wins': 0, 'losses': 0, 'draws': 0}

    if winner == 'user_won':
        user_stats[user_id]['wins'] += 1
    elif winner == 'bot_won':
        user_stats[user_id]['losses'] += 1
    else:
        user_stats[user_id]['draws'] += 1

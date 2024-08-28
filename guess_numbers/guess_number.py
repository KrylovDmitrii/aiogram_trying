import os
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

user_games = {}


class Number:
    def __init__(self):
        self.number = random.randrange(1, 101)
        self.attempts = 0
        self.status = True

    def guess_number(self, number):
        if self.number == number:
            self.status = False
            return "Поздравляю! Вы угадали число!"
        self.attempts += 1
        if self.attempts >= 5:
            self.status = False
            return f'Ваши 5 попыток истекли. Загаданное число было {self.number}. Начните новую игру командой /start'
        if number > self.number:
            return f'Мое число меньше\nУ вас  еще {5 - self.attempts} попыток'
        else:
            return f'Мое число больше\nУ вас  еще {5 - self.attempts} попыток'


@dp.message(Command(commands=['start']))
async def start_commands(message: Message):
    user_id = message.from_user.id
    user_games[user_id] = Number()
    await message.answer('Игра началась! Я загадал число от 1 до 100. Попробуйте угадать его. У вас есть 5 попыток.')


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Используйте команду /start для начала игры. Напишите число, чтобы сделать попытку.')


@dp.message()
async def guess_number(message: Message):
    user_id = message.from_user.id
    if user_id not in user_games:
        await message.answer('Для начала игры используйте команду /start')
        return
    try:
        curr_number = int(message.text)
        if curr_number not in range(1, 101):
            await message.answer('Число дожно быть от 1 до 11')
            return
    except ValueError:
        await message.answer('Пожалуйста, отправьте число.')
        return
    game = user_games[user_id]
    response = game.guess_number(curr_number)
    await message.answer(response)

    if game.attempts >= 5 or not game.status:
        del user_games[user_id]


if __name__ == '__main__':
    dp.run_polling(bot)



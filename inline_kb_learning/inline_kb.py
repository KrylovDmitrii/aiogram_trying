import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, BotCommand, CallbackQuery
from dotenv import load_dotenv

from inline_keyboards.url_kb import url_keyboard
from inline_keyboards.callback_kb import callback_keyboard

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
           "[%(asctime)s] - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

BOT_COMMANDS_RU: dict[str, str] = {
    '/start': 'start desription',
    '/url': 'url inline',
    '/callback': 'callback inline',
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in BOT_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Тест различных inline-кнопок')


@dp.message(Command(commands=['url']))
async def process_url_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=url_keyboard
    )


@dp.message(Command(commands=['callback']))
async def process_url_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "callback"',
        reply_markup=callback_keyboard
    )


@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer('big кнопка 2', show_alert=True)


async def main():
    await set_main_menu(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

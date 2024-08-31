import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаем свой класс фабрики коллбэков, указывая префикс
# и структуру callback_data
class GoodsCallbackFactory(CallbackData, prefix="goods"):
    category_id: int
    subcategory_id: int
    item_id: int


# Создаем объекты кнопок, с применением фабрики коллбэков
button_1 = InlineKeyboardButton(
    text='Категория 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    ).pack()
)

button_2 = InlineKeyboardButton(
    text='Категория 2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    ).pack()
)

markup = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая клавиатура',
        reply_markup=markup
    )


@dp.callback_query(GoodsCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(text=callback_data.pack())
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)

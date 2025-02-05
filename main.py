import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'Ваш токен'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Бойцы")
button2 = KeyboardButton("Карты")
keyboard.add(button1, button2)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выберите что хотите узнать:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["Бойцы", "Карты"])
async def handle_buttons(message: types.Message):
    if message.text == "Бойцы":
        await message.answer("Напишите имя бойца")
    elif message.text == "Карты":
        await message.answer("Напишите название карты")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram import F

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = 'ваш токен'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Диспетчер больше не принимает бота как аргумент

# Создаем клавиатуру с двумя кнопками
button1 = KeyboardButton(text="Бойцы")
button2 = KeyboardButton(text="Карты")
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button1, button2]],  # Кнопки передаются как список списков
    resize_keyboard=True  # Опционально: автоматическое изменение размера клавиатуры
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выберите что хотите узнать:", reply_markup=keyboard)

# Обработчик нажатия на кнопки
@dp.message(F.text.in_(["Бойцы", "Кнопка 2"]))  # Используем фильтр F
async def handle_buttons(message: types.Message):
    if message.text == "Бойцы":
        await message.answer("Напишите имя бойца.")
    elif message.text == "Кнопка 2":
        await message.answer("Напишите название карты.")

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)  # Используем метод run_polling для запуска бота

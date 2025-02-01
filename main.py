import asyncio

from aiogram.utils import executor

API_TOKEN = 'ваш токен'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Сборка бойцов", callback_data="button_pressed")
    keyboard.add(button)

    await message.answer("Привет! Выбери что хочешь узнать:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == "button_pressed")
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Кнопка нажата")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

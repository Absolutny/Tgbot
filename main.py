import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

Token = 'TOKEN'
dp = Dispatcher()
bot = Bot(token=Token)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Ку, выбери что хочешь узнать! {message.from_user.full_name}')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

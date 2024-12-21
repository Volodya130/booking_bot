import asyncio
import settings

from aiogram import Bot, Dispatcher
from aiogram.types import Message

async def echo(message: Message):
    await message.answer(message.text)



async def main():
    bot = Bot(token=settings.API_KEY)
    dp = Dispatcher()
    dp.message.register(echo)

    try:
        await dp.start_polling(bot)
    
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
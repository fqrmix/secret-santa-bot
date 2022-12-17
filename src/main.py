import asyncio
from aiogram import Bot, Dispatcher
from handlers import pollanswer, generation
from dotenv import load_dotenv
import os

load_dotenv()

# Запуск бота
async def main():
    bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))
    dp = Dispatcher()

    dp.include_router(pollanswer.router)
    dp.include_router(generation.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

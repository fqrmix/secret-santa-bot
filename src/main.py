import asyncio
from aiogram import Bot, Dispatcher
from handlers import pollanswer
from dotenv import load_dotenv
import os

load_dotenv()

# Запуск бота
async def main():
    bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))
    dp = Dispatcher()

    dp.include_router(pollanswer.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
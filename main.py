import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import config
from handlers import commands, messages


async def main():
    bot = Bot(token=config.token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    dp.include_routers(
        commands.router,
        messages.router
    )
    
    # логируем события и ошибки
    logging.basicConfig(level=logging.INFO)
    
    # отключаем доставку сохранённых сообщений во время отключения бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

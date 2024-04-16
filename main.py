import asyncio
from aiogram import Bot, Dispatcher, types, F

from app.handlers import router
from app.database.models import async_main
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode


async def main():
    await async_main()
    bot = Bot(token='7029766904:AAGAQ1RwINUlWLvmGPUQQquCT3ZJjqudlTE',default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

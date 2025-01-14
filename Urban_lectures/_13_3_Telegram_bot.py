from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '8118250237:AAFqYYfQaC6tE_JxQTkYTWObZjpnYauSz1Q'
bot = Bot(token=api)
dp = Dispatcher(
    bot=bot,
    storage=MemoryStorage(),
)


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
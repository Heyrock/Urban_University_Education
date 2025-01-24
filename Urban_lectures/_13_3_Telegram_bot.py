from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '8118250237:AAFqYYfQaC6tE_JxQTkYTWObZjpnYauSz1Q'
bot = Bot(token=api)
dp = Dispatcher(
    bot=bot,
    storage=MemoryStorage(),
)


@dp.message_handler(text = ['Urban', 'xxx'])
async def urban_msg(message):
    print('Мы получили сообщение Urban')
    await message.answer('Ответ на сообщение Urban или xxx')


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    print('Мы получили команду start')
    await message.answer('Ответ на команду start')


@dp.message_handler()
async def all_messages(message):
    print("Мы получили необработанное сообщение!")
    await message.answer(f'Зеркальный ответ {message.text}')
    await message.answer(message.text.upper())


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
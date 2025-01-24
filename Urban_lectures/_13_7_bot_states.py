import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
import asyncio

# настройка логирования в файл
logging.basicConfig(
    filename='_13_bot.log',
    filemode='w',
    level=logging.INFO,
    encoding='UTF8',
    format='%(asctime)s | '
           '%(name)s | '
           '%(message)s | '
)

# токен API
api = '8118250237:AAFqYYfQaC6tE_JxQTkYTWObZjpnYauSz1Q'
# Инициализация бота по токену API
bot = Bot(token=api)
# Инициализация хранилища в памяти
storage = MemoryStorage()
# Инициализация диспетчера с использованием бота и хранилища
dp = Dispatcher(
    bot=bot,
    storage=storage,
)
# установка middleware для хранения
dp.middleware.setup(LoggingMiddleware())


class UserState(StatesGroup):
    address = State()


@dp.message_handler(text=['заказ', 'order'])
async def order(message: types.Message):
    # print('Ждем ваш адрес')
    await message.answer('Ждем ваш адрес')
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(
        message: types.Message,
        state: FSMContext):
    # print(f'Вы указали адрес: {message.text}')
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f'Заказ будет отправлен по адресу: {data["first"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
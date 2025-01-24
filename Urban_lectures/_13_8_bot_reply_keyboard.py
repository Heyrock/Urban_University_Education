from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


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


# инициализация клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация кнопки
bt_info = KeyboardButton(text='Информация')
bt_begin = KeyboardButton(text='Начало')

# Добавление кнопки в клавиатуру
kb.add(bt_info, bt_begin)


# Вызов клавиатуры по команде /info
@dp.message_handler(commands=['info'])
async def info_kb(message: Message):
    await message.answer(
        text='Привет',
        reply_markup=kb,
    )


# обработка нажатия кнопки 'Информация'
@dp.message_handler(text=['Информация'])
async def info(message: Message):
    await message.answer(
        text='Вашему вниманию информация о боте'
    )


# обработка нажатия кнопки 'Начало'
@dp.message_handler(text=['Начало'])
async def info(message: Message):
    await message.answer(text='Мы начинаем КВН!')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )



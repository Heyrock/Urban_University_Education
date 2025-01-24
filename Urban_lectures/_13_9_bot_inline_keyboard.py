from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext


api = '8118250237:AAFqYYfQaC6tE_JxQTkYTWObZjpnYauSz1Q'
bot = Bot(token=api)
dp = Dispatcher(
    bot=bot,
    storage=MemoryStorage(),
)

# создание инлайн-клавиатуры
inl_kb = InlineKeyboardMarkup()
# создание инлайн-кнопок
inl_bt_info = InlineKeyboardButton(
    text='Информация',
    callback_data='inl_bt_info',
)
inl_bt_begin = InlineKeyboardButton(
    text='Начало',
    callback_data='inl_bt_begin',
)
# добавление кнопок в инлайн-клавиатуру
inl_kb.add(inl_bt_info, inl_bt_begin)


# Вызов инлайн-клавиатуры по команде /info
@dp.message_handler(commands=['info'])
async def info_inl_kb(message: Message):
    await message.answer(
        text='Привет!',
        reply_markup=inl_kb,
    )


# обработка нажатия инлайн-кнопки 'Информация'
@dp.callback_query_handler(text=['inl_bt_info'])
async def info(call: CallbackQuery):
    await call.message.answer(
        text='Вашему вниманию информация о боте',
    )
    await call.answer()


# обработка нажатия инлайн-кнопки 'Начало'
@dp.callback_query_handler(text=['inl_bt_begin'])
async def begin(call: CallbackQuery):
    await call.message.answer(
        text='Мы начинаем КВН'
    )
    await call.answer()


# создание реплай-клавиатуры типа "меню"
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Магазин, Вход')],
        [
            KeyboardButton(text='Налево'),
            KeyboardButton(text='Прямо'),
            KeyboardButton(text='Направо'),
        ],
        [KeyboardButton(text='Выход')]
    ],
    resize_keyboard=True,
)


# вызов реплай-клавиатуры командой /shop
@dp.message_handler(commands=['shop'])
async def shop_hdlr(message: Message):
    await message.answer(
        text='Добро пожаловать в магазин!',
        reply_markup=menu_kb,
    )


if __name__ == '__main__':
    print('Поехали!')
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )

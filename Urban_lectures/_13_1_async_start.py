import time
import asyncio


async def notification():
    time.sleep(1)
    print('до доставки осталось: 1 минута')


async def main():
    # await notification()
    # task = asyncio.create_task(notification())
    asyncio.create_task(notification())
    print('Собираемся в поездку')
    print('Кушаем')


asyncio.run(main())
# Собираемся в поездку
# Кушаем
# до доставки осталось: 1 минута

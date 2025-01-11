import time
import asyncio


async def notification():
    time.sleep(1)
    print('до доставки осталось: 1 минута')


async def main():
    # await notification()
    # task = asyncio.create_task(notification())
    print('Собираемся в поездку')
    asyncio.create_task(notification())
    print('Кушаем')


asyncio.run(main())
# asyncio.run(notification())
# Собираемся в поездку
# Кушаем
# до доставки осталось: 1 минута

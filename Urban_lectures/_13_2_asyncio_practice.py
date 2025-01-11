import time
import asyncio


async def get_temp():
    print('Первое показание')
    # time.sleep(1)
    await asyncio.sleep(1)
    print('25 C')

async def get_pres():
    print('Второе показание')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('101 kPa')

async def main():
    print('Старт')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_pres())
    await task1
    await task2
    print('Финиш')

start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Рабочее время = {round(finish - start, 2)} сек.')

# Старт
# Первое показание
# Второе показание
# 25 C
# 101 kPa
# Финиш
# Рабочее время = 2.0 сек.
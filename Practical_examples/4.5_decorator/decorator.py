from time import time


def check_time(f):
    def wrapper(lst):
        start = time()
        print(f'Начало: {start}')
        result = f(lst)
        end = time()
        print(f'Конец: {end}')
        print(f'Время выполнения: {end} - {start}')
        return result
    return wrapper

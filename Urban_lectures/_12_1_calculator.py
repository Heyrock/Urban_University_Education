import logging

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        logging.info(msg=f'Successful division: {a} / {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error(
            msg='No dividing by zero!',
            exc_info=True,
        )
        return 0


def sqrt(a):
    return a ** 0.5


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='_12_6_py.log',
        format='%(asctime)s | %(levelname)s | %(message)s',
    )
    div(10, 2)
# 2025-01-08 15:42:33,298 | INFO | Successful division: 10 / 2
    div(3, 0)

# 2025-01-08 15:43:41,482 | INFO | Successful division: 3 / 0
# 2025-01-08 15:43:41,482 | ERROR | No dividing by zero!
# Traceback (most recent call last):
#   File "C:\Users\���\Documents\Urban_1\Urban_lectures\_12_1_calculator.py", line 18, in div
#     return a / b
#            ~~^~~
# ZeroDivisionError: division by zero

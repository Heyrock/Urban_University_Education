import logging


def div(a, b):
    try:
        a / b
        logging.info(msg=f'Successful division: {a} / {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error(
            msg='No dividing by zero!',
            exc_info=True,
        )
        return 0


if __name__ == '__main__':
    # logging.debug('логгинг')
    # logging.info('логгинг')
    # logging.warning('логгинг')
    # logging.error('логгинг')
    # logging.critical('логгинг')

    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='_12_6_py.log',
        encoding='utf8',
        format='%(asctime)s | %(levelname)s | %(message)s',
    )
    print(div(10, 2)) # 5.0
    print(div(3, 0)) # 0

# 2025-01-08 15:42:33,298 | INFO | Successful division: 10 / 2
# 2025-01-08 15:43:41,482 | INFO | Successful division: 3 / 0
# 2025-01-08 15:43:41,482 | ERROR | No dividing by zero!
# Traceback (most recent call last):
#   File "C:\Users\���\Documents\Urban_1\Urban_lectures\_12_1_calculator.py", line 18, in div
#     return a / b
#            ~~^~~
# ZeroDivisionError: division by zero
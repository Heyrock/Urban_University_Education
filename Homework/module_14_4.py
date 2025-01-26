# Цель: научится использовать функции внутри запросов языка SQL и
# использовать их в решении задачи.
#
# Задача "Средний баланс пользователя":
#
# Для решения этой задачи вам понадобится решение предыдущей.
#
# Для решения необходимо дополнить существующий код:
# 1. Удалите из базы данных not_telegram.db запись с id = 6.
# 2. Подсчитать общее количество записей.
# 3. Посчитать сумму всех балансов.
# 4. Вывести в консоль средний баланс всех пользователя.
#
# Пример результата выполнения программы:
# Выполняемый код:
# # Код из предыдущего задания
# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
#
# Вывод на консоль:
# 700.0

import sqlite3

connection = sqlite3.connect('not_telegram.db')
# connection = sqlite3.connect('module_14_4_DB.db')
cursor = connection.cursor()

# # создание таблицы
# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS Users('
#     'id INTEGER PRIMARY KEY,'
#     'username TEXT NOT NULL,'
#     'email TEXT NOT NULL,'
#     'age INTEGER,'
#     'balance INTEGER NOT NULL'
#     ')'
# )
#
# # добавление 10 пользователей в таблицу
# for i in range(1, 11):
#     cursor.execute(
#         'INSERT INTO Users (username, email, age, balance) '
#         'VALUES (?, ?, ?, ?)',
#         (f'User{i}', f'example{i}@gmail.com', str(i * 10), '1000')
#     )
#
# # меняем каждому нечетному пользователю баланс на 500
# cursor.execute(
#     'UPDATE Users SET balance = ? WHERE id % 2 != 0',
#     ('500',)
# )
#
# # удаляем первого и каждого третьего за ним (1, 4, 7, 10)
# for i in range(1, 11, 3):
#     cursor.execute(
#         'DELETE FROM Users WHERE id = ?',
#         (str(i),)
#     )

# # Удаление пользователя с id=6
# cursor.execute(
#     'DELETE FROM Users WHERE id = ?',
#     ('6',)
# )

# Подсчёт кол-ва всех пользователей
cursor.execute(
    'SELECT COUNT(*) FROM Users'
)
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute(
    'SELECT SUM(balance) FROM Users'
)
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
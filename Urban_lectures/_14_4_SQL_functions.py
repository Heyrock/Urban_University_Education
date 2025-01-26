import sqlite3
import random

connection = sqlite3.connect('_14_3_database.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')

# for i in range(30):
#     cursor.execute(
#         'INSERT INTO Users(username, email, age) VALUES (?, ?, ?)',
#         (f'newuser{i}', f'{i}ex@gmail.com', str(random.randint(20, 60)))
#         )


# выбрать всех
# cursor.execute('SELECT * FROM Users')


# выбрать старше 29 лет
# cursor.execute(
#     'SELECT username, age FROM Users WHERE age > ?',
#     ('29',)
# )

# # посчитать количество ВСЕХ пользователей
# cursor.execute(
#     'SELECT COUNT(*) FROM Users'
# )
# print(cursor.fetchone()[0])
# # 30

# # посчитать количество пользователей старше 32
# cursor.execute(
#     'SELECT COUNT(*) FROM Users WHERE age > ?',
#     (32,)
# )
# print(cursor.fetchone()[0])
# # 23

# # посчитать сумму возрастов ВСЕХ пользователей
# cursor.execute(
#     'SELECT SUM(age) FROM Users'
# )
# total_age = print(*cursor.fetchone())
# # 1278

# # посчитать средний возраст всех пользователей
# cursor.execute(
#     'SELECT COUNT(*) FROM users'
# )
# total_num = cursor.fetchone()[0]
#
# cursor.execute(
#     'SELECT SUM(age) FROM Users'
# )
# total_age = cursor.fetchone()[0]
# avg_age = total_age / total_num
# print(avg_age)
# # 42.6

# # посчитать средний возраст всех пользователей через AVG
# cursor.execute(
#     'SELECT AVG(age) FROM Users'
# )
# avg_age = cursor.fetchone()[0]
# print(avg_age)
# # 42.6

# узнать минимальные и максимальные значения в поле
cursor.execute(
    'SELECT MIN(age) FROM Users'
)
min = cursor.fetchone()[0]

cursor.execute(
    'SELECT MAX(age) FROM Users'
)
max = cursor.fetchone()[0]

print(min, max)
# 22 59


connection.commit()
connection.close()


import sqlite3
import random

connection = sqlite3.connect('_14_3_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

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

# отсориторвать всех по возрасту
cursor.execute(
    'SELECT age, username FROM Users GROUP BY age'
)

users = cursor.fetchall()
print(len(users))

for user in users:
    print(user)

connection.commit()
connection.close()

# (22, 'newuser8')
# (27, 'newuser3')
# (29, 'newuser9')
# (30, 'newuser10')
# ...
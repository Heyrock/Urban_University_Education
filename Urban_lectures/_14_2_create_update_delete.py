import sqlite3

connection = sqlite3.connect(database='_14_1_database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
""")

cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_email ON Users(email)
''')

# cursor.execute(
#     'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
#     ('newuser', 'ex@gmail.com', '28')
# )

# добавить данные
# for i in range(10):
#     cursor.execute(
#         'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
#         (f'newuser - {i}', f'{i}ex@gmail.com', '28')
#     )

# изменить данные
# cursor.execute(
#     'UPDATE Users SET age = ? WHERE username = ?',
#     ('29', 'newuser')
# )

# удалить данные
cursor.execute(
    'DELETE FROM Users WHERE username = ?',
    ('newuser',)
)

connection.commit()
connection.close()

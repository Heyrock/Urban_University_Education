class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Database.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self):
        print(f'Запись в БД {data}')


db = Database('root', 1234, 80)
db2 = Database('root2', 5678, 40)
print(id(db))
# 2137649858320
print(id(db2))
# 2137649858320
print(db.__dict__)
# {'user': 'root2', 'psw': 5678, 'port': 40}
print(db2.__dict__)
# {'user': 'root2', 'psw': 5678, 'port': 40}
db.connect()
db2.connect()

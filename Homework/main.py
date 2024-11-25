class Cat:
    def __new__(cls, *args, **kwargs):
        print('1. Создание экземпляра класса Cat')
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        print('2. Инициализация созданного экземпляра класса Cat')
        self.name = name


cat = Cat.__new__(Cat)
Cat.__init__(cat, 'Кузя')

print(type(cat))
print(cat.name)
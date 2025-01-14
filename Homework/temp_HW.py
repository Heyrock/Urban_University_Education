import inspect


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj)
                       if not callable(getattr(obj, attr))
                       and not attr.startswith('__')],
        'methods': [method for method in dir(obj)
                    if callable(getattr(obj, method))
                    and not method.startswith('__')],
        # 'module': obj.__class__.__module__
        'module': type(obj).__module__
    }
    return info

# Взял класс из раннего задания
class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)



# Создание объекта
my_object = House('Hilton', 10)

# Интроспекция
object_info = introspection_info(my_object)
print(object_info)
# {'type': 'House', 'attributes': ['name', 'number_of_floors'],
# 'methods': ['go_to'], 'module': '__main__'}

number_info = introspection_info(42)
print(number_info)
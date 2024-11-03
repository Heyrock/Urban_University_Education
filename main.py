class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)


nums = [1, 2, 3]
personal = {'name': 'Eugen', 'age': 47}

user1 = User(*nums, **personal)
print(user1.args)
print(user1.name)
print(user1.age)

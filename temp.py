class A:
    def __init__(self, *arg):
        self.__a = arg

    @staticmethod
    def check(arg):
        lst = []
        return all(map(lambda x: x > 0, arg))

    @property
    def a_func(self):
        return self.__a

    @a_func.setter
    def a_func(self, *new_arg):
        if self.check(new_arg):
            self.__a = new_arg


class B(A):
    def __init__(self, arg):
        super().__init__(arg)


b = B(1) # expected type Tuple, got int instead
print(b.__dict__)
# {'_A__a': (1,)}
b.a_func = 15
print(b.a_func)

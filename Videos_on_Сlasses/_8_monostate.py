# class MyThreadData:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls, *args, **kwargs)
#             return cls.__instance
#
#
# td = MyThreadData()
# print(td.__dict__)


class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


td = ThreadData()
td1 = ThreadData()
td1.id = 3
td1.attr_new = 'new_attr'
print(td.__dict__)
# {'name': 'thread_1', 'data': {}, 'id': 3, 'attr_new': 'new_attr'}
print(td1.__dict__)
# {'name': 'thread_1', 'data': {}, 'id': 3, 'attr_new': 'new_attr'}
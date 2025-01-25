"""class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'

    class Meta:
        ordering = ['id']


print(Women.Meta.ordering)
# ['id']

w = Women()
print(w.Meta.ordering)
# ['id']"""

# --------------------

"""class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(f'{user}@{psw}')

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


w = Women('root', '1234')
print(w.__dict__)
# {'_user': 'root', '_psw': '1234', 'meta': <__main__.Women.Meta object at 0x0000025C5FF86150>}
print(w.meta.__dict__)
# {'_access': 'root@1234'}"""

# ------------------
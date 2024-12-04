class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('init MixInLog')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00 часов')

    def print_info(self):
        print('Info from MixinLog')

class NoteBook(Goods, MixinLog):
    # def print_info(self):
    #     MixinLog.print_info(self)
    pass


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
# Acer, 1.5, 30000
# n.save_sell_log()
# print(NoteBook.__mro__)
# (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>,
# <class 'object'>)
# MixinLog.print_info(n)
# Info from MixinLog
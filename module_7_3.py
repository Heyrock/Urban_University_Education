# Цель: применить на практике оператор with, вспомнить написание кода в
# парадигме ООП.
#
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt', 'file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество
# названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# 1) get_all_words - подготовительный метод, который возвращает словарь
# следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],
# 'file3.txt': ['word5', 'word6', 'word7']}
#
# Где:
# 1. 'file1.txt', 'file2.txt', 'file3.txt' - названия файлов.
# 2. ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] -
# слова, содержащиеся в этом файле.
#
# Алгоритм получения словаря такого вида в методе get_all_words:
# 1. Создайте пустой словарь all_words.
# 2. Переберите названия файлов и открывайте каждый из них, используя оператор with.
# 3. Для каждого файла считывайте единые строки, переводя их в нижний регистр
# (метод lower()).
# 4. Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - ']
# в строке. (тире обособлено пробелами, это не дефис в слове).
# 5. Разбейте эту строку на элементы списка методом split().
# (разбивается по умолчанию по пробелу)
# 6. В словарь all_words запишите полученные данные, ключ - название файла,
# значение - список из слов этого файла.
#
# 2) find(self, word) - метод, где word - искомое слово.
# Возвращает словарь, где ключ - название файла, значение - позиция первого
# такого слова в списке слов этого файла.
#
# 3) count(self, word) - метод, где word - искомое слово.
# Возвращает словарь, где ключ - название файла, значение - количество слова
# word в списке слов этого файла.
#
# В методах find и count пользуйтесь ранее написанным методом get_all_words для
# получения названия файла и списка его слов.
#
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно
# воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
#
#   # Логика методов find или count
#
# Пример результата выполнения программы:
# Представим, что файл 'module_7_3_test_file.txt' содержит следующий текст:
#
# Пример выполнения программы:
# finder2 = WordsFinder('module_7_3_test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# Вывод на консоль:
# {'module_7_3_test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его',
# 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'module_7_3_test_file.txt': 3}
# {'module_7_3_test_file.txt': 4}
#
# Запустите этот код с другими примерами предложенными здесь.
# Если решение верное, то результаты должны совпадать с предложенными.
# https://drive.google.com/drive/folders/1IJEynqs2lk-uP1wrVBpm_w3qnEQCCx6O
#
# Примечания:
# 1. Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# 2. Решайте задачу последовательно - написав один метод, проверьте результаты его
#  работы.

class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    @staticmethod
    def text_preparation(file):
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        text = file.read()
        text = ''.join([i for i in text.lower() if i not in symbols])
        words_lst = text.replace(' - ', '').strip().split()
        return words_lst

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf8') as file:
                all_words[file_name] = self.text_preparation(file)
        return all_words

    def find(self, word):
        result = []
        word = word.lower()
        all_words = self.get_all_words()
        for file in all_words:
            if word in all_words[file]:
                index = all_words[file].index(word)
                result.append({file: index + 1})
        return result

    def count(self, word):
        result = []
        word = word.lower()
        all_words = self.get_all_words()
        for file in all_words:
            if word in all_words[file]:
                word_qty = all_words[file].count(word)
                result.append({file: word_qty})
        return result

finder1 = WordsFinder('module_7_3_text.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

# Проверочный результат:
#
# {'module_7_3_text': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']}
# {'module_7_3_text': 2}
# {'module_7_3_text': 10}

# мой результат
# {'module_7_3_text': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']}
# [{'module_7_3_text': 2}]
# [{'module_7_3_text': 10}]
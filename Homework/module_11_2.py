# Цель: познакомиться с использованием сторонних библиотек в Python и
# применить их в различных задачах.
#
# Задача:
#
# 1. Выберите одну или несколько сторонних библиотек Python, например, requests,
# pandas, numpy, matplotlib, pillow.
# 2. После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их
# основными возможностями и функциями. К каждой библиотеке дана ссылка на
# документацию ниже.
#
# Если вы выбрали:
#
# 1. requests - запросить данные с сайта и вывести их в консоль.
# 2. pandas - считать данные из файла, выполнить простой анализ данных (на своё
# усмотрение) и вывести результаты в консоль.
# 3. numpy - создать массив чисел, выполнить математические операции с массивом
# и вывести результаты в консоль.
# 4. matplotlib - визуализировать данные с помощью библиотеки любым удобным для
# вас инструментом из библиотеки.
# 5. pillow - обработать изображение, например, изменить его размер, применить
# эффекты и сохранить в другой формат.
#
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые
# предоставила вам выбранная библиотека и как вы расширили возможности Python
# с её помощью.
#
# Примечания:
#
# 1. Можете выбрать не более 3-х библиотек для изучения.
# 2. Желательно продемонстрировать от 3-х функций/классов/методов/операций из
# каждой выбранной библиотеки.


# модуль requests

""" Честно украдено из старых конспектов.
    Я никогда не работал с сайтами, и без чужой подсказки не представляю,
    что и где в них можно брать.
    Но сама структура действий понятна"""

import requests
from pprint import pprint

API_KEY = 'dict.1.1.20231003T131408Z.8b308095a51a27ed.5487188eb70a2c7bbc75c84a878e12f9e67826e9'
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'


def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response


def lookup(lang, text, ui='ru'):
    response = requests.post(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response


langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список направлений перевода')
    exit(1)

langs = langs_response.json()
print('Выберите одно из доступных направлений перевода')
print(langs)
while (lang := input('Введите направление: ')) not in langs:
    print('Такого направления нет. Попробуйте ещё раз')

text = input('Введите слово или фразу для перевода: ')
lookup_response = lookup(lang, text)
if lookup_response.status_code != 200:
    print('Не удалось выполнить перевод:', lookup_response.text)
    exit(1)

pprint(lookup_response.json()['def'][0]['tr'][0]['text'])


# модуль numpy
import numpy as np

a = np.arange(1, 13).reshape(4, 3)
b = np.rot90(a)
c = np.rot90(a, -1)
print(b * c)


# модули pandas и matplotlib
import pandas as pd
import matplotlib.pyplot as plt


students = pd.read_csv('module_11_2_students_perdormance.csv')

agg_functions = {"math score": ["mean", "median"]}
print(students.groupby(["gender", "test preparation course"]).agg(agg_functions))

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()


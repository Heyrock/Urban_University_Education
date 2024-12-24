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


students = pd.read_csv('students_perdormance.csv')

agg_functions = {"math score": ["mean", "median"]}
print(students.groupby(["gender", "test preparation course"]).agg(agg_functions))

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()


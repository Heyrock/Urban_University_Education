import os
import time
from os.path import basename, dirname, abspath

for root, dirs, files in os.walk('.'):
    for file in files:
        # Абсолютный путь файла -> полный адрес директории -> замыкающий фрагмент
        # parent_dir = os.path.basename(os.path.dirname(os.path.abspath(file)))
        parent_dir = basename(dirname(abspath(file)))

        # вариант от корня
        # filepath = os.path.join(root, file)
        filepath = os.path.join(parent_dir, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')


import threading as th
from time import sleep, time
from datetime import timedelta


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.001)
            # sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


params = ((10, 'example1.txt'),
          (30, 'example2.txt'),
          (200, 'example3.txt'),
          (100, 'example4.txt')
          )

params_th = ((10, 'example5.txt'),
             (30, 'example6.txt'),
             (200, 'example7.txt'),
             (100, 'example8.txt')
             )

start = time()

for i in range(4):
    write_words(params[i][0], params[i][1])

print(f'Работа потоков {timedelta(seconds=(time() - start))}')


start_th = time()
threads = []

for i in range(4):
    thread = th.Thread(
        target=write_words,
        args=(params_th[i][0], params_th[i][1]),
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Работа потоков {timedelta(seconds=(time() - start_th))}')


import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as f:
        empty = False
        while not empty:
            line = f.readline()
            all_data.append(line)
            if not line:
                empty = True


# Пример результата выполнения программы:
filenames = [f'module_11_1_file_{number}.txt' for number in range(1, 5)]

# Линейный вызов
start_lin = datetime.datetime.now()
for file in filenames:
    read_info(file)
print(datetime.datetime.now() - start_lin, '(линейный)')
# 0:00:09.871931 (линейный)


# Многопроцессный
if __name__ == '__main__':
    start_mul = datetime.datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    print(datetime.datetime.now() - start_mul, '(многопроцессный)')
# 0:00:03.668743 (многопроцессный)

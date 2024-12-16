import datetime
import json
import operator
from functools import reduce
from threading import Thread

files = ['_10_4_file1.json', '_10_4_file2.json', '_10_4_file3.json', '_10_4_file4.json']

def operate(file):
    with open(file, 'r') as f:
        data = json.load(f)
        total_res.extend(data)


total_res = []
time_calc = []

def main():
    start_th = datetime.datetime.now()

    threads = []

    for file in files:
        th = Thread(
            target=operate,
            args=(file, )
        )
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    end_th = datetime.datetime.now()
    time_elapsed_th = end_th - start_th
    return time_elapsed_th

for i in range(100):
    time_calc.append(main())
    total_res = []


print(sum([calc.microseconds for calc in time_calc]) / len(time_calc))
# 58194.5
print(sum([calc.microseconds for calc in time_calc]))
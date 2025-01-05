import datetime
import json

# все .json файлы
files = ['_10_4_file1.json', '_10_4_file2.json', '_10_4_file3.json', '_10_4_file4.json']

# for file in files:
#     res = []
#     for _ in range(100_000):
#         res.append(randint(0, 10_000))
#     with open(file, 'w', encoding='utf-8') as f:
#         json.dump(res, f)

total_res = []
start = datetime.datetime.now()

for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        total_res.extend(data)

print(sum(total_res))
# 1998812832
end = datetime.datetime.now()
time_elapsed = end - start
print(time_elapsed)
# 0:00:00.076953
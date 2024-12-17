def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as f:
        empty = False
        while not empty:
            line = f.readline()
            all_data.append(line)
            if not line:
                empty = True
    print(all_data[:10])

read_info('module_11_1_file 1')


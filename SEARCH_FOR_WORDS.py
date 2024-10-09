import os

search_text = input('Введите текст поиска: ').lower()

# directories = 'Чужие решения. Шпаргалки'
directories = 'C:\\Users\\Ром\\Documents\\Urban_1'


# def find_file(cur_path, ending='.txt'):
def find_file(cur_path, ending=('.txt', '.py')):
    all_paths = []
    # список всех файлов .txt
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem.endswith(ending):
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, ending)
            if result:
                all_paths.extend(result)

    return all_paths


def search_for_text(path_to_file, text):
    # список всех файлов, в которых есть нужный текст
    results = []
    for path in path_to_file:
        with open(path, "r", encoding="utf8") as file:
            for line in file:
                if text in line.lower():
                    results.append(path)
                    break
    return results


# распечатка результатов
def print_out(all_paths):
    print('Нужный текст присутствует в файлах:')
    for path in all_paths:
        print(path)


all_txt_files = find_file(directories)

all_paths = search_for_text(all_txt_files, search_text)

print_out(all_paths)

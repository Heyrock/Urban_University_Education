import os
import shutil

# if os.path.exists('Testing'):
#     os.chdir('Testing')
# else:
#     os.mkdir('Testing')
#     os.chdir('Testing')
#
# print(os.getcwd())
# # C:\Users\Ром\Documents\Urban_1\Urban_lectures\Testing
# print(os.listdir())
# # ['first']

# for i in os.walk('.'):
#     print(i)

# ('.', ['first'], [])
# ('.\\first', ['second'], ['first_file.py'])
# ('.\\first\\second', ['third'], ['second_file.py'])
# ('.\\first\\second\\third', [], ['third_file.py'])

# files = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]

# os.startfile(files[1])
# запускается файл 'sample2.txt'
# print(os.stat(files[1]).st_size)
# # 91
# os.system('pip install random2')
# Successfully installed random2-1.0.2
# shutil.rmtree('Testing')

# import os
# from os.path import join, getsize
# for root, dirs, files in os.walk('.'):
#     print(root, "consumes", end=" ")
#     print(sum(getsize(join(root, name)) for name in files), end=" ")
#     print("bytes in", len(files), "non-directory files")
#     if 'CVS' in dirs:
#         dirs.remove('CVS')
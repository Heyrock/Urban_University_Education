import io
from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='UTF8')

print(file.readable()) # True
print(file.writable()) # False
print(file.seekable()) # True

print(file.name) # sample2.txt
print(file.buffer)
# <_io.BufferedReader name='sample2.txt'>

print(file.tell())
pprint(file.read())
print(file.tell())
print(file.closed) # False
file.close()
print(file.closed) # True





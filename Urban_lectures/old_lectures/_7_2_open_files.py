from pprint import pprint

name = ''
file = open(name, 'r')
print(file.tell())
print(file.seek(7))
pprint(file.read())
print(file.tell())
 #
file.close()


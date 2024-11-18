import re

symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
# symbols = [',', '.', '=', '!', '?', ';', ':']

line = 'dkjsdfhnjksd,,,,kjsfnsk - ldfj - s'

line = ''.join([i for i in line.lower() if i not in symbols])
line = line.replace(' - ', '')
print(line)
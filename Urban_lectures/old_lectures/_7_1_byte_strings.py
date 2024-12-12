a = 'hello'
chars = []
for i in a:
    chars.append(ord(i))
print(chars)
# [104, 101, 108, 108, 111]

my_str = ''
for i in chars:
    my_str += chr(i)

print(my_str)
# hello

print(hex(ord('h'))) # 0x68

bb = b'\x68'
print(type(bb))
# <class 'bytes'>
print(bb) # b'h'
print(bb.decode()) # h
from common import *

data = filemap(str, 'day03.txt')

def pri(c):
    if ord(c) <= ord('Z'):
        return 27 + ord(c) - ord('A')
    else:
        return 1 + ord(c) - ord('a')

s = 0
for i in data:
    h1 = i[:len(i)//2]
    h2 = i[len(i)//2:]

    c = (set(h1) & set(h2)).pop()
    s += pri(c)
print(s)

s = 0
for i in chunk(data, 3):
    b = (set(i[0]) & set(i[1]) & set(i[2])).pop()
    s += pri(b)
print(s)

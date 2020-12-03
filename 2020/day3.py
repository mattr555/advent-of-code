from common import *

def parse(s):
    return s

data = filemap(parse, 'day3.txt')

p2 = 1
for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    ct = 0
    while y < len(data):
        if data[y][x] == '#':
            ct += 1
        y += dy
        x += dx
        x %= len(data[0])
    
    # part 1
    if (dx, dy) == (3, 1):
        print(ct)
    # part 2
    p2 *= ct

print(p2)

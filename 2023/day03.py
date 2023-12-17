from common import *

def transform(x):
    return x

data = filemap(transform, 'day03.txt')
p1 = 0
gears = defaultdict(set)

for y in range(len(data)):
    x = 0
    while x < len(data[y]):
        v = data[y][x]
        if v.isdigit():
            endx = x
            while endx < len(data[y]) and data[y][endx].isdigit():
                endx += 1

            n = int(data[y][x:endx])

            symbol_found = False
            for tx in range(x, endx):
                for pt, v in neighbors(data, y, tx, diags=True):
                    if v != '.' and not v.isdigit():
                        symbol_found = True
                    if v == "*":
                        gears[pt].add(n)
            
            if symbol_found:
                p1 += n

            x = endx
        else:
            x += 1
print(p1)

p2 = 0
for i in gears.values():
    if len(i) == 2:
        p2 += product(i)
print(p2)
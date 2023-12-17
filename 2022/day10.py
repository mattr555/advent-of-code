from common import *

def transform(x):
    if x == 'noop':
        return None
    return int(x.split(' ')[1])

data = filemap(transform, 'day10.txt')

p1 = 0
grid = denseGrid(6, 40)
cc = 0
x = 1

def eval_at(cc, x):
    global p1
    if cc % 40 == 20:
        p1 += x * cc

    r = (cc-1) // 40
    c = (cc-1) % 40
    if abs(x-c) <= 1:
        grid[r][c] = DARK_SHADE
    else:
        grid[r][c] = ' '

for i in data:
    if i is None:
        eval_at(cc + 1, x)
        cc += 1
    else:
        eval_at(cc + 1, x)
        eval_at(cc + 2, x)
        cc += 2
        x += i

print(p1)
for row in grid:
    print(''.join(row))


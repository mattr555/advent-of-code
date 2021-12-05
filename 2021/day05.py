from common import *

def parse(l):
    o = []
    for pt in l.split(' -> '):
        x, y = map(int, pt.split(','))
        o.append((x, y))
    return o


data = filemap(parse, 'day05.txt')
grid_p1 = denseGrid(1000, 1000, 0)
grid_p2 = denseGrid(1000, 1000, 0)
for i in data:
    (x1, y1) = i[0]
    (x2, y2) = i[1]
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            grid_p1[x1][i] += 1
            grid_p2[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            grid_p1[i][y1] += 1
            grid_p2[i][y1] += 1
    else:
        x = x1
        y = y1
        while x != x2 and y != y2:
            grid_p2[x][y] += 1
            if x < x2:
                x += 1
            else:
                x -= 1
            if y < y2:
                y += 1
            else:
                y -= 1
        grid_p2[x][y] += 1


def ans(g):
    s = 0
    for r in g:
        for i in r:
            if i >= 2:
                s += 1
    return s

print(ans(grid_p1))
print(ans(grid_p2))

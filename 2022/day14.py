from common import *

maxx, maxy = 0, 0

def transform(x):
    global maxx, maxy, miny
    r = []
    for i in x.split(' -> '):
        a, b = i.split(',')
        a = int(a)
        b = int(b)
        maxx = max(a+1, maxx)
        maxy = max(b+1, maxy)
        r.append((int(a), int(b)))
    return r

data = filemap(transform, 'day14.txt')

grid = denseGrid(maxx+500, maxy+2, '.')
for line in data:
    for ix in range(1, len(line)):
        sx, sy = line[ix-1]
        ex, ey = line[ix]
        if sx != ex:
            for tx in range(min(sx, ex), max(sx, ex)+1):
                grid[tx][sy] = '#'
        elif sy != ey:
            for ty in range(min(sy, ey), max(sy, ey)+1):
                grid[sx][ty] = '#'
        else:
            assert False

grid2 = deepcopy(grid)

def sim(grid):
    done = False
    ct = 0
    while not done:
        sx, sy = 500, 0

        while True:
            while sy+1 < len(grid[0]) and grid[sx][sy+1] == '.':
                sy += 1
            if sy+1 >= len(grid[0]):
                done = True
                break
            if grid[sx-1][sy+1] == '.':
                sx -= 1
                sy += 1
            elif sx+1 >= len(grid):
                done = True
                break
            elif grid[sx+1][sy+1] == '.':
                sx += 1
                sy += 1
            else:
                grid[sx][sy] = 'o'
                ct += 1
                if sx == 500 and sy == 0:
                    done = True
                break
    return ct
print(sim(grid))

for x in range(len(grid2)):
    grid2[x][-1] = '#'

print(sim(grid2))
# print('\n'.join([''.join(x) for x in grid2]))



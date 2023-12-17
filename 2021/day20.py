from common import *

data = filemap(lambda x: x, 'day20.txt')
alg = data[0]
grid = data[2:]
oob = '.'

def do_step(grid, oob):
    new_grid = denseGrid(len(grid)+2, len(grid[0])+2)
    for x in range(len(new_grid)):
        for y in range(len(new_grid[0])):
            s = ''
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx = x+dx
                    ny = y+dy
                    if nx-1 < 0 or nx-1 > len(grid)-1 or \
                        ny-1 < 0 or ny-1 > len(grid[0]) -1:
                        s += oob
                    else:
                        s += grid[nx-1][ny-1]
            s = int(s.replace('.', '0').replace('#', '1'), 2)
            new_grid[x][y] = alg[s]
    if oob == '#':
        new_oob = alg[-1]
    else:
        new_oob = alg[0]
    return new_grid, new_oob

for i in range(50):
    grid, oob = do_step(grid, oob)
    if i == 2:
        print(sum(x.count('#') for x in grid))
print(sum(x.count('#') for x in grid))

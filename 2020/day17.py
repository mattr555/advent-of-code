from common import *

data = filemap(lambda x: x, 'day17.txt')

grid = set()
for x, xr in enumerate(data):
    for y, yr in enumerate(xr):
        if yr == '#':
            grid.add((x, y, 0))

def neighbors(grid, x, y, z):
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx == dy == dz == 0:
                    continue
                if (x+dx, y+dy, z+dz) in grid:
                    n += 1
    return n

for turn in range(1, 7):
    new_grid = set()
    for x in range(-turn, len(data) + turn):
        for y in range(-turn, len(data[0]) + turn):
            for z in range(-turn, turn+1):
                n = neighbors(grid, x, y, z)
                p = (x, y, z)
                if p in grid and (n == 2 or n == 3):
                    new_grid.add(p)
                elif p not in grid and (n == 3):
                    new_grid.add(p)
    grid = new_grid
print(len(grid))



grid = set()
for x, xr in enumerate(data):
    for y, yr in enumerate(xr):
        if yr == '#':
            grid.add((x, y, 0, 0))

def neighbors(grid, x, y, z, w):
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if dx == dy == dz  == dw == 0:
                        continue
                    if (x+dx, y+dy, z+dz, w+dw) in grid:
                        n += 1
    return n

for turn in range(1, 7):
    new_grid = set()
    for x in range(-turn, len(data) + turn):
        for y in range(-turn, len(data[0]) + turn):
            for z in range(-turn, turn+1):
                for w in range(-turn, turn+1):
                    n = neighbors(grid, x, y, z, w)
                    p = (x, y, z, w)
                    if p in grid and (n == 2 or n == 3):
                        new_grid.add(p)
                    elif p not in grid and (n == 3):
                        new_grid.add(p)
    grid = new_grid
print(len(grid))

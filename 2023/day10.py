from common import *

def transform(x):
    return list(x)

grid = filemap(transform, 'day10.txt')

p1 = 0
p2 = 0

for y, row in enumerate(grid):
    if 'S' in row:
        x = row.index('S')
        break

sy, sx = y, x

pipes = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
    'S': [(-1, 0), (0, -1), (1, 0), (0, 1)]
}

def connects(y, x, dy, dx):
    return 0 <= y+dy < len(grid) and 0 <= x+dx <= len(grid[0]) and \
        (dy, dx) in pipes[grid[y][x]] and (-dy, -dx) in pipes[grid[y+dy][x+dx]]

def other(y, x, dy, dx):
    for ny, nx in pipes[grid[y][x]]:
        if ny != -dy or nx != -dx:
            return ny, nx


for start_dy, start_dx in set(DIRECTIONS.values()):
    y, x = sy, sx
    dy, dx = start_dy, start_dx
    if not connects(y, x, dy, dx):
        continue

    l = 1
    path = set()
    while connects(y, x, dy, dx):
        y += dy
        x += dx
        l += 1
        path.add((y, x))
        if grid[y][x] == 'S':
            p1 = l
            print(p1//2)
            #need to determine what pipe S really is
            # it's the pipe that is (start_dy, start_dx) and (-dy, -dx)
            for pipe, l in pipes.items():
                if pipe != 'S' and (start_dy, start_dx) in l and (-dy, -dx) in l:
                    grid[y][x] = pipe
            break
        dy, dx = other(y, x, dy, dx)
    else:
        continue

    for y, row in enumerate(grid):
        in_above = False
        in_below = False
        for x, i in enumerate(row):
            if (y, x) in path:
                if i == '|':
                    in_above = not in_above
                    in_below = not in_below
                elif i == 'J' or i == 'L':
                    in_above = not in_above
                elif i == '7' or i == 'F':
                    in_below = not in_below
            elif in_above and in_below:
                p2 += 1
    print(p2)

    break


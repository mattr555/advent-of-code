import re
import sys
sys.setrecursionlimit(4000)

EMPTY = ' '
BRICK = '#'
FLOWING = '|'
REST = '~'
XBUFF = 2

line_re = re.compile(r'([xy])=(\d+), [xy]=(\d+)\.\.(\d+)')

data = []
with open("day17.txt") as f:
    for l in f:
        data.append(line_re.match(l).groups())

data = list(map(lambda i: (i[0], int(i[1]), int(i[2]), int(i[3])), data))

min_x = 1000000
max_x = -1
min_y = 1000000
max_y = -1
for i in data:
    if i[0] == 'x':
        min_x = min(min_x, i[1])
        max_x = max(max_x, i[1])
        min_y = min(min_y, i[2])
        max_y = max(max_y, i[3])
    else:
        min_x = min(min_x, i[2])
        max_x = max(max_x, i[3])
        min_y = min(min_y, i[1])
        max_y = max(max_y, i[1])

size_x = max_x - min_x + 1 + (XBUFF * 2)
size_y = max_y - min_y + 1
cx = lambda x: XBUFF + x - min_x
cy = lambda y: y - min_y
grid = []
for _ in range(size_y):
    grid.append([EMPTY] * size_x)

for i in data:
    if i[0] == 'x':
        for y in range(i[2], i[3] + 1):
            grid[cy(y)][cx(i[1])] = BRICK
    else:
        for x in range(i[2], i[3] + 1):
            grid[cy(i[1])][cx(x)] = BRICK


def printGrid(grid):
    for i in grid:
        print(''.join(i))

def outOfBounds(x, y):
    return x < min_x - XBUFF or x > max_x + XBUFF or y < min_y or y > max_y

def projectDownward(x, y):
    if outOfBounds(x, y):
        return
    if grid[cy(y)][cx(x)] in (BRICK, REST):
        return
    
    grid[cy(y)][cx(x)] = FLOWING
    if outOfBounds(x, y+1):
        return
    elif grid[cy(y+1)][cx(x)] in (BRICK, REST):
        projectAcross(x, y)
    else:
        projectDownward(x, y+1)
        if grid[cy(y+1)][cx(x)] == REST:
            projectAcross(x, y)

def projectAcross(x, y):
    #search left for wall
    wmin = x
    while grid[cy(y)][cx(wmin-1)] != BRICK and grid[cy(y+1)][cx(wmin)] in (BRICK, REST):
        wmin -= 1
    wmax = x
    while grid[cy(y)][cx(wmax+1)] != BRICK and grid[cy(y+1)][cx(wmax)] in (BRICK, REST):
        wmax += 1
    
    if grid[cy(y+1)][cx(wmin)] in (BRICK, REST):
        if grid[cy(y+1)][cx(wmax)] in (BRICK, REST):
            #all should be at rest
            for dx in range(wmin, wmax+1):
                grid[cy(y)][cx(dx)] = REST
        
        else:
            #flowing out the right side
            for dx in range(wmin, wmax+1):
                grid[cy(y)][cx(dx)] = FLOWING
            projectDownward(wmax, y)
    else:
        if grid[cy(y+1)][cx(wmax)] in (BRICK, REST):
            #flowing out the left side
            for dx in range(wmin, wmax+1):
                grid[cy(y)][cx(dx)] = FLOWING
            projectDownward(wmin, y)
        
        else:
            #flowing out both sides
            for dx in range(wmin, wmax+1):
                grid[cy(y)][cx(dx)] = FLOWING
            projectDownward(wmin, y)
            projectDownward(wmax, y)


projectDownward(500, min_y)
printGrid(grid)

part1 = 0
part2 = 0
for r in grid:
    for i in r:
        if i == REST:
            part1 += 1
            part2 += 1
        elif i == FLOWING:
            part1 += 1
print(part1)
print(part2)

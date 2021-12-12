from common import *

GRIDSIZE = 10
data = filemap(lambda x: [int(y) for y in x], 'day11.txt')

def neighbors(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            tx = x+dx
            ty = y+dy
            if dx == dy == 0 or tx < 0 or tx >= GRIDSIZE \
                or ty < 0 or ty >= GRIDSIZE:
                continue
            yield (tx, ty)

def do_step(grid):
    for x in range(GRIDSIZE):
        for y in range(GRIDSIZE):
            grid[x][y] += 1

    new_flasher = True
    total_flashers = 0
    while new_flasher:
        new_flasher = False
        for x in range(GRIDSIZE):
            for y in range(GRIDSIZE):
                if grid[x][y] > 9:
                    new_flasher = True
                    total_flashers += 1
                    grid[x][y] = 0
                    for nx, ny in neighbors(x, y):
                        if grid[nx][ny] > 0:
                            grid[nx][ny] += 1
    return total_flashers

p1 = 0
p2 = 0
step = 1
while step <= 100 or p2 == 0:
    f = do_step(data)
    if step <= 100:
        p1 += f
    if f == 100:
        p2 = step
    step += 1
print(p1)
print(p2)


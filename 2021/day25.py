from common import *

def parse(x):
    return x

grid = filemap(parse, 'day25.txt')

def do_step(grid):
    new_grid = denseGrid(len(grid), len(grid[0]), '.')
    move = False
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            nx = (x+1) % len(grid)
            ny = (y+1) % len(grid[0])
            if grid[x][y] == '>':
                if grid[x][ny] == '.':
                    new_grid[x][ny] = '>'
                    move = True
                else:
                    new_grid[x][y] = '>'
            elif grid[x][y] == 'v':
                new_grid[x][y] = 'v'
    newer_grid = denseGrid(len(grid), len(grid[0]), '.')
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            nx = (x+1) % len(grid)
            ny = (y+1) % len(grid[0])
            if new_grid[x][y] == 'v':
                if new_grid[nx][y] == '.':
                    newer_grid[nx][y] = 'v'
                    move = True
                else:
                    newer_grid[x][y] = 'v'
            elif new_grid[x][y] == '>':
                newer_grid[x][y] = '>'
    return newer_grid, move

move = True
n = 0
while move:
    grid, move = do_step(grid)
    n += 1
print(n)

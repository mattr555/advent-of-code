from common import *

data = filemap(list, 'day11.txt')

def find_equilibrium(grid, neighbor_fn, leave_thresh):
    curr = grid
    last = ''
    while repr(curr) != last:
        next = denseGrid(len(curr), len(curr[0]))
        last = repr(curr)
        for y in range(len(curr)):
            for x in range(len(curr[0])):
                neighbors = neighbor_fn(curr, x, y)
                if curr[y][x] == '#':
                    next[y][x] = 'L' if neighbors >= leave_thresh else '#'
                elif curr[y][x] == 'L':
                    next[y][x] = '#' if neighbors == 0 else 'L'
                else:
                    next[y][x] = '.'
        curr = next
    return curr

def p1_neighbors(grid, x, y):
    neighbors = 0
    for dx, dy in DIRECTIONS_DIAGS:
        if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
            neighbors += 1 if grid[y+dy][x+dx] == '#' else 0
    return neighbors

print(repr(find_equilibrium(data, p1_neighbors, 4)).count('#'))

def p2_neighbors(grid, x, y):
    neighbors = 0
    for dx, dy in DIRECTIONS_DIAGS:
        look = 1
        while True:
            tx = x + look * dx
            ty = y + look * dy
            if not (0 <= tx < len(grid[0]) and 0 <= ty < len(grid)):
                break
            if grid[ty][tx] in 'L#':
                neighbors += 1 if grid[ty][tx] == '#' else 0
                break
            look += 1
    return neighbors

print(repr(find_equilibrium(data, p2_neighbors, 5)).count('#'))

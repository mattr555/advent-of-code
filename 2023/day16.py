from common import *

def transform(x):
    return x

grid = filemap(transform, 'day16.txt')

p1 = 0
p2 = 0

def run(sy, sx, sdy, sdx):
    energized = set()
    seen = set()
    to_visit = set([(sy, sx, sdy, sdx)])

    while to_visit:
        y, x, dy, dx = to_visit.pop()
        if (y, x, dy, dx) in seen or y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            continue
        seen.add((y, x, dy, dx))
        energized.add((y, x))

        tile = grid[y][x]
        if tile == '.':
            to_visit.add((y+dy, x+dx, dy, dx))
        elif tile == '-':
            if dy == 0:
                to_visit.add((y+dy, x+dx, dy, dx))
            else:
                to_visit.add((y, x+1, 0, 1))
                to_visit.add((y, x-1, 0, -1))
        elif tile == '|':
            if dx == 0:
                to_visit.add((y+dy, x+dx, dy, dx))
            else:
                to_visit.add((y+1, x, 1, 0))
                to_visit.add((y-1, x, -1, 0))
        elif tile == '/':
            if dx == 0:
                ndx = -dy
                ndy = 0
            else:
                ndx = 0
                ndy = -dx
            to_visit.add((y+ndy, x+ndx, ndy, ndx))
        elif tile == '\\':
            if dx == 0:
                ndx = dy
                ndy = 0
            else:
                ndx = 0
                ndy = dx
            to_visit.add((y+ndy, x+ndx, ndy, ndx))

    return len(energized)

print(run(0, 0, 0, 1))

for row in range(len(grid)):
    p2 = max(p2, run(row, 0, 0, 1))
    p2 = max(p2, run(row, len(grid[0])-1, 0, -1))

for col in range(len(grid[0])):
    p2 = max(p2, run(0, col, 1, 0))
    p2 = max(p2, run(len(grid)-1, col, -1, 0))
print(p2)

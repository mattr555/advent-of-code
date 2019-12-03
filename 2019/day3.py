from common import *

def lineParse(s):
    return [(i[0], int(i[1:])) for i in s.split(",")]

lines = filemap(lineParse, "day3.txt")

grid = defaultdict(lambda: [None] * len(lines))
for lineNum, line in enumerate(lines):
    x = 0
    y = 0
    s = 0
    
    for direction, step in line:
        dx, dy = DIRECTIONS[direction]

        for _ in range(step):
            x += dx
            y += dy
            s += 1
            if grid[(x, y)][lineNum] is None:
                grid[(x, y)][lineNum] = s

manhattan = 1e50
steps = 1e50
for (x, y), v in grid.items():
    if all(i is not None for i in v):
        manhattan = min(manhattan, abs(x) + abs(y))
        steps = min(steps, sum(v))

print(manhattan)
print(steps)

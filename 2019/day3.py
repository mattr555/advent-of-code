from common import *
from collections import defaultdict

lines = []
with open("day3.txt") as f:
    for line in f:
        lines.append([(i[0], int(i[1:])) for i in line.split(",")])

grid = defaultdict(int)
for lineNum, line in enumerate(lines):
    x = 0
    y = 0
    
    for direction, step in line:
        dx = 0
        dy = 0
        if direction == "U":
            dy = 1
        elif direction == "D":
            dy = -1
        elif direction == "L":
            dx = -1
        elif direction == "R":
            dx = 1

        for _ in range(step):
            x += dx
            y += dy
            grid[(x, y)] |= (lineNum + 1)

best = 1e50
for (x, y), v in grid.items():
    if v == 3:
        best = min(best, abs(x) + abs(y))

print(best)

intersections = [{}, {}]

for lineNum, line in enumerate(lines):
    x = 0
    y = 0
    s = 0
    
    for direction, step in line:
        dx = 0
        dy = 0
        if direction == "U":
            dy = 1
        elif direction == "D":
            dy = -1
        elif direction == "L":
            dx = -1
        elif direction == "R":
            dx = 1

        for _ in range(step):
            x += dx
            y += dy
            s += 1

            if grid[(x, y)] == 3 and (x, y) not in intersections[lineNum]:
                intersections[lineNum][(x, y)] = s

best = 1e50
for i in intersections[0]:
    best = min(best, intersections[0][i] + intersections[1][i])
print(best)

from common import *
from intcode import IntcodeVM

import sys
sys.setrecursionlimit(2000)

data = filemap(int, "day15.txt", ',')

grid = defaultdict(lambda: None)
x, y = 0, 0

WALL = 0
OPEN = 1
TARGET = 2

vm = IntcodeVM(data)

BACKWARDS = {1: 2, 2: 1, 3: 4, 4: 3}

def floodfill(x, y, steps):
    for direction in range(1, 5):
        dx, dy = DIRECTIONS[direction]
        nx = x + dx
        ny = y + dy

        if grid[(nx, ny)] is not None:
            continue

        vm.addInput([direction])
        vm.runToBlock()

        grid[(nx, ny)] = vm.output[-1]
        # if vm.output[-1] == TARGET:
        #     print("found in " + str(steps))
        if vm.output[-1] in (OPEN, TARGET):
            floodfill(nx, ny, steps+1)
            vm.addInput([BACKWARDS[direction]])
            vm.runToBlock()
            assert vm.output[-1] != WALL

floodfill(x, y, 0)

q = deque([(0, 0, 0)])
s = set()
m = (inf, 0, 0)
while len(q) > 0:
    x, y, step = q.popleft()
    s.add((x, y))
    for direction in range(1, 5):
        dx, dy = DIRECTIONS[direction]
        nx = x + dx
        ny = y + dy

        if (nx, ny) in s or grid[(nx, ny)] is None or grid[(nx, ny)] == WALL:
            continue
        elif grid[(nx, ny)] == TARGET:
            m = min(m, (step+1, nx, ny))
        else:
            q.append((nx, ny, step+1))

# print(grid)

dg = denseGrid(45, 45, FULL_BLOCK)
for ((x, y), v) in grid.items():
    dg[y + 20][x + 20] = FULL_BLOCK if v == WALL else '.'
    if x == 0 and y == 0:
        dg[y+20][x+20] = '*'
    elif v == TARGET:
        dg[y+20][x+20] = 'T'

for i in dg:
    print(''.join(i))

print(m[0])

q = deque([(m[1], m[2], 0)])
s = set()
m = 0
while len(q) > 0:
    x, y, step = q.popleft()
    m = max(m, step)
    s.add((x, y))
    for direction in range(1, 5):
        dx, dy = DIRECTIONS[direction]
        nx = x + dx
        ny = y + dy

        if (nx, ny) in s or grid[(nx, ny)] is None or grid[(nx, ny)] == WALL:
            continue
        else:
            q.append((nx, ny, step+1))

print(m)
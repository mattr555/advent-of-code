from common import *
from intcode import IntcodeVM

data = filemap(int, "day15.txt", ',')

grid = defaultdict(lambda: None)
x, y = 0, 0

WALL = 0
OPEN = 1
TARGET = 2

vm = IntcodeVM(data)

BACKWARDS = {1: 2, 2: 1, 3: 4, 4: 3}

def explore(x, y):
    for direction in range(1, 5):
        dx, dy = DIRECTIONS[direction]
        nx = x + dx
        ny = y + dy

        if grid[(nx, ny)] is not None:
            continue

        vm.addInput([direction])
        vm.runToBlock()

        grid[(nx, ny)] = vm.output[-1]
        if vm.output[-1] in (OPEN, TARGET):
            explore(nx, ny)
            vm.addInput([BACKWARDS[direction]])
            vm.runToBlock()
            assert vm.output[-1] != WALL

explore(x, y)

PRINT = {
    WALL: FULL_BLOCK,
    OPEN: ' ',
    TARGET: 'T'
}

dg = denseGrid(41, 41, FULL_BLOCK)
for ((x, y), v) in grid.items():
    dg[y + 19][x + 21] = PRINT[v]
    if x == 0 and y == 0:
        dg[y + 19][x + 21] = '*'

for i in dg:
    print(''.join(i))

def bfsFlood(startX, startY):
    q = deque([(startX, startY, 0)])
    s = set()
    minToTarget = (inf, 0, 0)
    maxSteps = 0

    while len(q) > 0:
        x, y, step = q.popleft()

        maxSteps = max(maxSteps, step)
        if grid[(x, y)] == TARGET:
            minToTarget = min(minToTarget, (step, x, y))

        s.add((x, y))
        for direction in range(1, 5):
            dx, dy = DIRECTIONS[direction]
            nx = x + dx
            ny = y + dy

            if (nx, ny) in s or grid[(nx, ny)] is None or grid[(nx, ny)] == WALL:
                continue
            else:
                q.append((nx, ny, step+1))

    return minToTarget, maxSteps

part1, tx, ty = bfsFlood(0, 0)[0]
print(part1)

part2 = bfsFlood(tx, ty)[1]
print(part2)

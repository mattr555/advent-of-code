from common import *
from intcode import IntcodeVM

data = filemap(int, "day11.txt", ",")

BLACK = 0
WHITE = 1


TURNS = {
    'N': 'WE',
    'E': 'NS',
    'S': 'EW',
    'W': 'SN'
}

def run(initialBlock):
    vm = IntcodeVM(data)
    grid = defaultdict(lambda: BLACK)
    grid[(0, 0)] = initialBlock

    direction = 'N'
    x = 0
    y = 0
    halted = False
    while not halted:
        vm.addInput([grid[(x, y)]])
        halted = vm.runToBlock()
        grid[(x, y)] = vm.output[-2]
        direction = TURNS[direction][vm.output[-1]]
        dx, dy = DIRECTIONS[direction]
        x += dx
        y += dy

    return grid

part1 = run(BLACK)
print(len(part1))

part2 = run(WHITE)
dg = denseGrid(7, 48, FULL_BLOCK)
for (x, y), val in part2.items():
    dg[y + 6][x] = FULL_BLOCK if val == BLACK else LIGHT_SHADE

for line in reversed(dg):
    print(''.join(line))

from common import *
from intcode import IntcodeVM

prog = filemap(int, "day17.txt", ',')

vm = IntcodeVM(prog)
vm.runToBlock()

s = ''
for i in vm.output:
    s += chr(i)

print(s)
dg = s.strip().split('\n')
grid = defaultdict(lambda: False)
SCAFFOLD = set('#^><v')
HEIGHT = len(dg)
WIDTH = len(dg[0])

robotPos = None
robotDirection = None

DIRS = {'^': 'N', 'v': 'S', '>': 'W', '<': 'E'}

for y in range(HEIGHT):
    for x in range(WIDTH):
        if dg[y][x] in SCAFFOLD:
            grid[(x, y)] = True
        if dg[y][x] in '^v<>':
            robotPos = (x, y)
            robotDirection = DIRS[dg[y][x]]

ans = 0
for y in range(1, len(dg)-1):
    for x in range(1, len(dg[0])-1):
        if dg[y][x] in SCAFFOLD and \
            dg[y][x+1] in SCAFFOLD and \
            dg[y][x-1] in SCAFFOLD and \
            dg[y-1][x] in SCAFFOLD and \
            dg[y+1][x] in SCAFFOLD:
            ans += x*y

print(ans)

prog[0] = 2
vm = IntcodeVM(prog)



from common import *
from intcode import IntcodeVM

prog = filemap(int, "day19.txt", ',')

s = 0

def readGrid(x, y):
    vm = IntcodeVM(prog)
    vm.addInput([x, y])
    vm.runToBlock()
    return vm.output[-1]


grid = defaultdict(lambda: False)
dg = denseGrid(50, 50, 0)
for x in range(50):
    for y in range(50):
        res = readGrid(x, y)
        s += res
        grid[(x, y)] = res == 1
        dg[y][x] = res
print(s)



# row = 1000
# col = 0

def countRow(r):
    c = 0
    l = 0
    for col in range(r//2, r):
        res = readGrid(col, r)
        c += res
        if l == 0 and res == 1:
            start = col
        elif l == 1 and res == 0:
            end = col-1
            break
        l = res
    return c, start, end

def countCol(ix):
    c = 0
    l = 0
    for row in range(ix, ix*3):
        res = readGrid(ix, row)
        c += res
        if l == 0 and res == 1:
            start = row
        elif l == 1 and res == 0:
            end = row-1
            break
        l = res
    return c, start, end


def binaryThresholdSearch(f, lo, hi):
    if lo >= hi:
        return lo

    mid = (lo + hi) // 2
    res = f(mid)

    if res:
        return binaryThresholdSearch(f, lo, mid)
    else:
        return binaryThresholdSearch(f, mid+1, hi)

SIZE = 100
y = binaryThresholdSearch(lambda x: countRow(x)[0] >= SIZE, 0, SIZE * 20)
_, x, _ = countRow(y)

while not (readGrid(x, y) == 1 and readGrid(x, y+SIZE-1) == 1 and readGrid(x+SIZE-1, y) == 1):
    # shift x so that bottom left is in beam
    _, x, _ = countRow(y+SIZE-1)

    # shift y so that top right is in beam
    _, y, _ = countCol(x+SIZE-1)

print(x*10000 + y)


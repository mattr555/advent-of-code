from common import *
from intcode import IntcodeVM

data = filemap(int, "day13.txt", ",")
data[0] = 2

vm = IntcodeVM(data)

WIDTH = 37
HEIGHT = 20
grid = denseGrid(HEIGHT, WIDTH)

PRINTS = {
    0: " ",
    1: FULL_BLOCK,
    2: LIGHT_SHADE,
    3: FULL_BLOCK,
    4: FULL_BLOCK,
}

def printGrid():
    for row in grid:
        print(''.join(map(PRINTS.__getitem__, row)))

score = 0
paddleX = -1
ballX = -1
def tick(inp=None):
    global score, paddleX, ballX
    if inp is not None:
        vm.addInput([inp])
    halted = vm.runToBlock()
    for i in range(0, len(vm.output), 3):
        x = vm.output[i]
        y = vm.output[i+1]
        t = vm.output[i+2]
        if x == -1 and y == 0:
            score = t
        else:
            grid[y][x] = t
        
        if t == 3:
            paddleX = x
        elif t == 4:
            ballX = x

    vm.clearOutput()
    return halted

tick()
printGrid()

c = Counter()
for i in grid:
    c.update(i)


while True:
    print(score)
    printGrid()
    inp = sign(ballX - paddleX)
    h = tick(inp)
    if h:
        print("game over")
        break

print("part 1", c[2])
print("part 2", score)

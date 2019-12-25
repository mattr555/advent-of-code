from common import *
from intcode import IntcodeVM

prog = filemap(int, "day23.txt", ',')

COMPUTERS = 50
comps = []
qs = []
for i in range(COMPUTERS):
    comps.append(IntcodeVM(prog))
    comps[i].addInput([i])
    comps[i].runToBlock()
    qs.append(deque([]))

# done = False
nat = None
part1 = False
lastY = None
while True:
    idle = True
    for ix, c in enumerate(comps):
        if len(qs[ix]) > 0:
            idle = False
            while qs[ix]:
                x, y = qs[ix].popleft()
                c.addInput([x, y])
        else:
            c.addInput([-1])

        c.runToBlock()

        for i in range(0, len(c.output), 3):
            if c.output[i] == 255:
                if not part1:
                    print(c.output[i+2])
                    part1 = True
                nat = (c.output[i+1], c.output[i+2])
            else:
                qs[c.output[i]].append((c.output[i+1], c.output[i+2]))
        c.clearOutput()
    
    if idle:
        qs[0].append(nat)
        if nat[1] == lastY:
            print(nat[1])
            break
        lastY = nat[1]

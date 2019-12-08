from common import *
from intcode import IntcodeVM
from itertools import permutations

prog = filemap(int, "day7.txt", ',')

m = 0
for perm in permutations(range(5)):
    out = 0
    for i in perm:
        vm = IntcodeVM(prog)
        vm.addInput([i, out])
        vm.runToBlock()
        out = vm.output[0]
    m = max(out, m)

print(m)

m = 0
for perm in permutations(range(5, 10)):
    vms = []
    for i in perm:
        vm = IntcodeVM(prog)
        vm.addInput([i])
        vms.append(vm)

    amp = 0
    out = 0
    while True:
        vm = vms[amp]
        vm.addInput([out])
        halted = vm.runToBlock()
        out = vm.output[-1]
        if halted and amp == 4:
            break
        amp += 1
        amp %= 5
    
    m = max(out, m)
print(m)

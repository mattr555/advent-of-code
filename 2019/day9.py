from common import *

from intcode import IntcodeVM

prog = filemap(int, "day9.txt", ',')

vm = IntcodeVM(prog)
vm.addInput([1])
vm.runToBlock()
print(vm.output)

vm = IntcodeVM(prog)
vm.addInput([2])
vm.runToBlock()
print(vm.output)


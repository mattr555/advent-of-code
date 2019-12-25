from common import *
from intcode import IntcodeVM

prog = filemap(int, "day25.txt", ',')

vm = IntcodeVM(prog)

vm.runToBlock()
while True:
    s = ''
    for i in vm.output:
        s += chr(i)
    print(s)
    vm.clearOutput()

    inp = input('> ')
    for i in inp:
        vm.addInput([ord(i)])
    vm.addInput([10])
    vm.runToBlock()

# ans: 4206594
# astrolabe, ornament, food ration, weather machine
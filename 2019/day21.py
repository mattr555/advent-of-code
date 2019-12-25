from common import *
from intcode import IntcodeVM

prog = filemap(int, "day21.txt", ',')


# if D is true and any of A,B,C is false, jump
script1 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK'''

# D & (!A | !B | !C) & (H | (E & (I | F)))
script2 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT F T
NOT T T
OR I T
AND E T
OR H T
AND T J
RUN'''

def runScript(scr):
    vm = IntcodeVM(prog)
    inp = []
    for line in scr.splitlines():
        inp += list(map(ord, line))
        inp.append(10)

    vm.addInput(inp)
    vm.runToBlock()

    s = ''
    ans = 0
    for i in vm.output:
        try:
            s += chr(i)
        except ValueError:
            ans = i
    return ans, s

ans, s = runScript(script1)
print(ans)

ans, s = runScript(script2)
# print(s)
print(ans)

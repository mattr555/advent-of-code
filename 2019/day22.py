from common import *

data = filemap(lambda x: x, "day22.txt")

SIZE = 10007
stack = list(range(SIZE))

for instruction in data:
    if instruction == 'deal into new stack':
        stack = list(reversed(stack))
    elif instruction.startswith('cut'):
        n = int(instruction[4:])
        stack = stack[n:] + stack[:n]
    elif instruction.startswith('deal with increment'):
        n = int(instruction[20:])
        newStack = [None] * SIZE
        p = 0
        for i in range(SIZE):
            newStack[p] = stack[i]
            p += n
            p %= SIZE
        stack = newStack

print(stack.index(2019))


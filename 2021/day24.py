from common import *

def parse(x):
    return x.split(' ')

prog = filemap(parse, 'day24.txt')

def address(ch):
    return ord(ch)-ord('w')

def compute(instructions, inp):
    ip = 0
    reg = [0, 0, 0, 0]
    for ins in instructions:
        if ins[0] == 'inp':
            reg[address(ins[1])] = inp[ip]
            ip += 1
        else:
            if ins[2].isdigit() or ins[2].startswith('-'):
                val = int(ins[2])
            else:
                val = reg[address(ins[2])]
            
            if ins[0] == 'mul':
                reg[address(ins[1])] *= val
            elif ins[0] == 'add':
                reg[address(ins[1])] += val
            elif ins[0] == 'div':
                assert val != 0
                reg[address(ins[1])] //= val
            elif ins[0] == 'mod':
                assert reg[address(ins[1])] >= 0
                assert val > 0
                reg[address(ins[1])] %= val
            elif ins[0] == 'eql':
                reg[address(ins[1])] = 1 if reg[address(ins[1])] == val else 0
    return reg[3]

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            print(i, j, k, compute(prog[:54], [i,j,k]))
            for l in range(1, 10):
                print(i, j, k, l, compute(prog[:72], [i,j,k,l]))


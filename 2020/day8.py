from common import *

def parse(s):
    a, b = s.split(' ')
    return [a, int(b)]

data = filemap(parse, 'day8.txt')

def terminates(data):
    ip = 0
    acc = 0
    visited = set()
    while ip < len(data):
        if ip in visited:
            return False, acc
        visited.add(ip)
        op, arg = data[ip]
        if op == 'acc':
            acc += arg
            ip += 1
        elif op == 'nop':
            ip += 1
        elif op == 'jmp':
            ip += arg
    return True, acc

print(terminates(data)[1])

swap = {'nop': 'jmp', 'jmp': 'nop'}

for i in range(len(data)):
    if data[i][0] in swap:
        data[i][0] = swap[data[i][0]]
    else:
        continue
    term, acc = terminates(data)
    if term:
        print(acc)
        break
    data[i][0] = swap[data[i][0]]


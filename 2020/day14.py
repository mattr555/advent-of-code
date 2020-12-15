from common import *

def parse(s):
    if s.startswith('mask'):
        return 'mask', 0, s[7:]
    return 'mem', int(s.split('[')[1].split(']')[0]), int(s.split(' = ')[1])

data = filemap(parse, 'day14.txt')

mask = ''
mem = {}
for op, x, y in data:
    if op == 'mask':
        mask = y
    else:
        b = bin(y)[2:]
        b = '0'*(36 - len(b)) + b
        c = ''
        for i, j in zip(mask, b):
            if i == 'X':
                c += j
            else:
                c += i
        c = int(c, 2)
        mem[x] = c
print(sum(mem.values()))


def recurse(mask, b):
    ret = []
    s = ''
    for ix, (i, j) in enumerate(zip(mask, b)):
        if i == '0':
            s += j
        elif i == '1':
            s += '1'
        else:
            r = recurse(mask[ix+1:], b[ix+1:])
            for i in r:
                ret.append(s + '0' + i)
                ret.append(s + '1' + i)
            break
    if len(ret) == 0:
        return [s]
    return ret


mask = ''
mem = {}
for op, addr, v in data:
    if op == 'mask':
        mask = v
    else:
        b = bin(addr)[2:]
        b = '0'*(36 - len(b)) + b
        for a in map(lambda x: int(x, 2), recurse(mask, b)):
            mem[a] = v
print(sum(mem.values()))

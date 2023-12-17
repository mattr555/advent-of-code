from common import *
from functools import cmp_to_key

def transform(x):
    a, b = x.split('\n')
    return eval(a), eval(b)

data = filemap(transform, 'day13.txt', '\n\n')

def cmp(x, y):
    if type(x) is int and type(y) is int:
        if x < y:
            return -1
        elif x == y:
            return 0
        else:
            return 1
    elif type(x) is list and type(y) is list:
        for a, b in zip(x, y):
            c = cmp(a, b)
            if c != 0:
                return c
        if len(x) < len(y):
            return -1
        elif len(x) == len(y):
            return 0
        else:
            return 1
    elif type(x) is list:
        return cmp(x, [y])
    elif type(y) is list:
        return cmp([x], y)
    assert False

p1 = 0
data2 = [[[2]], [[6]]]
for ix, (a, b) in enumerate(data):
    data2.append(a)
    data2.append(b)
    c = cmp(a, b)
    if c == -1:
        p1 += ix + 1
print(p1)

data2.sort(key=cmp_to_key(cmp))
p2 = 1
for ix, a in enumerate(data2):
    if cmp([[2]], a) == 0:
        p2 *= ix + 1
    elif cmp([[6]], a) == 0:
        p2 *= ix + 1
print(p2)


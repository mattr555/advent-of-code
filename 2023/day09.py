from common import *

def transform(x):
    return list(map(int, x.split(' ')))

data = filemap(transform, 'day09.txt')

p1 = 0
p2 = 0

def diffList(x):
    l = []
    for i in range(len(x)-1):
        l.append(x[i+1] - x[i])
    return l

def go(l):
    if all(x == 0 for x in l):
        return 0
    return go(diffList(l)) + l[-1]

for l in data:
    p1 += go(l)
print(p1)

def go_rev(l):
    if all(x == 0 for x in l):
        return 0
    return l[0] - go_rev(diffList(l))

for l in data:
    p2 += go_rev(l)
print(p2)

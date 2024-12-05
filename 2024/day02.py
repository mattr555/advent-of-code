from common import *

def transform(x):
    return list(map(int, x.split(' ')))

data = filemap(transform, 'day02.txt')

def valid(l):
    last_diff = l[1] - l[0]
    for i in range(1, len(l)):
        diff = l[i] - l[i-1]
        if sign(diff) != sign(last_diff):
            break
        elif abs(diff) > 3 or abs(diff) < 1:
            break
        last_diff = diff
    else:
        return True
    return False

p1 = 0

for l in data:
    if valid(l):
        p1 += 1

print(p1)

p2 = 0

for base_l in data:
    good = False
    if valid(base_l):
        good = True
    for to_remove in range(len(base_l)):
        l = base_l[:to_remove] + base_l[(to_remove+1):]
        if valid(l):
            good = True
    if good:
        p2 += 1

print(p2)

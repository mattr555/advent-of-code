from common import *

def transform(x):
    a, b = x.split('   ')
    return int(a), int(b)

data = filemap(transform, 'day1.txt')

p1 = 0
a, b = transpose(data)
for i, j in zip(sorted(a), sorted(b)):
    p1 += abs(i - j)
print(p1)

p2 = 0
for i in a:
    p2 += i * b.count(i)
print(p2)

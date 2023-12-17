from common import *

reg = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

def transform(x):
    return list(map(int, reg.match(x).groups()))

data = filemap(transform, 'day04.txt')

c = 0
c2 = 0
for a, b, x, y in data:
    if (a <= x and y <= b) or (x <= a and b <= y):
        c += 1
    if (a <= x <= b) or (x <= a <= y):
        c2 += 1
print(c)
print(c2)

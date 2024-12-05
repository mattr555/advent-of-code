from common import *

def transform(x):
    return list(x)

data = filemap(transform, 'day04.txt')

p1 = 0
for row in data:
    p1 += ''.join(row).count('XMAS')
    p1 += ''.join(row).count('SAMX')
for row in transpose(data):
    p1 += ''.join(row).count('XMAS')
    p1 += ''.join(row).count('SAMX')
for row in all_diag(data):
    p1 += ''.join(row).count('XMAS')
    p1 += ''.join(row).count('SAMX')
for row in all_diag([list(reversed(x)) for x in data]):
    p1 += ''.join(row).count('XMAS')
    p1 += ''.join(row).count('SAMX')
print(p1)

p2 = 0
for a in range(1, len(data)-1):
    for b in range(1, len(data[a])-1):
        if data[a][b] == 'A':
            c = data[a-1][b-1]
            d = data[a+1][b+1]
            e = data[a-1][b+1]
            f = data[a+1][b-1]
            if ((c == 'M' and d == 'S') or (c == 'S' and d == 'M')) and ((e == 'M' and f == 'S') or (e == 'S' and f == 'M')):
                p2 += 1
print(p2)

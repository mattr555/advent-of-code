from common import *

def transform(x):
    return list(x)

grid = filemap(transform, 'day11.txt')

p1 = 0
p2 = 0

row_prefixes = []
i = 0
for y, row in enumerate(grid):
    if '#' not in row:
        i += 1
    row_prefixes.append(i)

col_prefixes = []
i = 0
for x, row in enumerate(transpose(grid)):
    if '#' not in row:
        i += 1
    col_prefixes.append(i)

points = set()
for y, row in enumerate(grid):
    for x, i in enumerate(row):
        if i == '#':
            points.add((y, x))

for (y1, x1), (y2, x2) in itertools.combinations(points, 2):
    p1 += abs(y2-y1) + abs(row_prefixes[y2] - row_prefixes[y1]) \
        + abs(x2-x1) + abs(col_prefixes[x2] - col_prefixes[x1])
    p2 += abs(y2-y1) + 999999 * abs(row_prefixes[y2] - row_prefixes[y1]) \
        + abs(x2-x1) + 999999 * abs(col_prefixes[x2] - col_prefixes[x1])
print(p1)
print(p2)

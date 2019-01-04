with open('day6.txt') as f:
    data = list(map(lambda x: tuple(map(int, x.replace(' ', '').split(','))), f.read().split('\n')))

max_x = max(data, key=lambda x: x[0])[0]
max_y = max(data, key=lambda x: x[1])[1]

def closestIndex(x, y):
    best = max_x + max_y
    bestIndexes = []
    for ind, (a, b) in enumerate(data):
        this = abs(x - a) + abs(y - b)
        if this == best:
            bestIndexes.append(ind)
        elif this < best:
            best = this
            bestIndexes = [ind]
    if len(bestIndexes) == 1:
        return bestIndexes[0]
    return None

grid = []
for i in range(max_x):
    grid.append([-1] * max_y)

for x in range(max_x):
    for y in range(max_y):
        grid[x][y] = closestIndex(x, y) or -1

from collections import Counter
count = Counter()
for r in grid:
    count += Counter(r)

count[-1] = 0
for i in grid[0]:
    count[i] = 0
for i in grid[-1]:
    count[i] = 0
for i in range(x):
    count[grid[i][0]] = 0
    count[grid[i][-1]] = 0

print(count)

size = 0
for x in range(max_x):
    for y in range(max_y):
        if sum(abs(x - a) + abs(y - b) for (a, b) in data) < 10000:
            size += 1
print(size)
            

        
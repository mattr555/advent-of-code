import re
line_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

max_x = 0
max_y = 0

def string_to_data(l):
    res = line_re.match(l)
    if res is None:
        return None
    return [int(res.group(x)) for x in range(2, 6)] + [int(res.group(1))]

with open("day3.txt") as f:
    data = list(map(string_to_data, f.read().split('\n')))

for i in data:
    max_x = max(max_x, i[0] + i[2])
    max_y = max(max_y, i[1] + i[3])

grid = []
for i in range(max_y):
    row = []
    for j in range(max_x):
        row.append(set())
    grid.append(row)

for i in data:
    for y in range(i[1], i[1] + i[3]):
        for x in range(i[0], i[0] + i[2]):
            grid[y][x].add(i[4])

count = 0
all_possible = set([i[4] for i in data])
for y in range(max_y):
    for x in range(max_x):
        if len(grid[y][x]) > 1:
            count += 1
            all_possible -= grid[y][x]

print(count)
print(len(all_possible))
for i in all_possible:
    print(i)

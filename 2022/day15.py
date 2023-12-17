from common import *
from tqdm import tqdm

reg = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

def transform(x):
    return tuple(map(int, reg.match(x).groups()))

data = filemap(transform, 'day15.txt')
MAX_SIZE = 4000000
ROW = 2000000

# MAX_SIZE = 20
# ROW = 10

s = set()
for sx, sy, bx, by in data:
    dist = abs(bx-sx) + abs(by-sy)
    to_travel_across = dist - abs(ROW - sy)
    if to_travel_across > 0:
        s |= set(range(sx-to_travel_across, sx+to_travel_across))
print(len(s))

def del_interval(l, start, end):
    new_int = []
    for os, oe in l:
        if start <= os:
            if end >= oe:
                continue
            else:
                new_int.append((max(os, end+1), oe))
        else:
            if end < oe:
                new_int.append((os, start-1))
                new_int.append((end+1, oe))
            else:
                new_int.append((os, min(oe, start-1)))
    return new_int

grid = [[(0, MAX_SIZE)] for i in range(MAX_SIZE)]
for sx, sy, bx, by in tqdm(data):
    dist = abs(bx-sx) + abs(by-sy)
    for y in range(sy - dist, sy + dist):
        if y < 0 or y >= MAX_SIZE:
            continue
        to_travel_across = dist - abs(y - sy)
        grid[y] = del_interval(grid[y], sx - to_travel_across, sx + to_travel_across)

for ix, i in enumerate(grid):
    if len(i) > 0:
        print(f"({i[0][0]}, {ix}) = {i[0][0] * MAX_SIZE + ix}")




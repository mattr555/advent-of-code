from common import *

def parse(x):
    return [int(y) for y in x]

data = filemap(parse, 'day09.txt')

def neighbors(x, y):
    n = []
    for tx, ty in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
        if tx >= 0 and tx < len(data) and ty >= 0 and ty < len(data[0]):
            n.append((tx, ty))
    return n

p1 = 0
basins = defaultdict(set)
unassigned = set()
flows = {}
for x in range(len(data)):
    for y in range(len(data[x])):
        d = data[x][y]
        if all(d < data[tx][ty] for (tx, ty) in neighbors(x, y)):
            p1 += 1 + d
            basins[(x, y)].add((x, y))
        elif d == 9:
            continue
        else:
            unassigned.add((x, y))
            flows[(x, y)] = min((data[tx][ty], (tx, ty)) for tx, ty in neighbors(x, y))[1]
print(p1)

while unassigned:
    cx, cy = unassigned.pop()
    gathered = set([(cx, cy)])
    while (cx, cy) in flows:
        cx, cy = flows[(cx, cy)]
        gathered.add((cx, cy))
        unassigned.discard((cx, cy))
    basins[(cx, cy)].update(gathered)

p2 = 1
for i in list(sorted(basins.values(), key=lambda x: len(x), reverse=True))[:3]:
    p2 *= len(i)
print(p2)



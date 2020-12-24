from common import *

def parse(s):
    dirs = []
    d = ''
    for i in s:
        if i in 'ns':
            d = i
        elif i in 'ew':
            dirs.append(d + i)
            d = ''
    return dirs

data = filemap(parse, 'day24.txt')

MOVEMENTS = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (0, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (0, -1)
}

flipped = set()
for move in data:
    x, y = 0, 0
    for m in move:
        dx, dy = MOVEMENTS[m]
        x += dx
        y += dy
    if (x, y) in flipped:
        flipped.remove((x, y))
    else:
        flipped.add((x, y))
print(len(flipped))

black = flipped
for turn in range(100):
    neighbor_ct = defaultdict(int)
    for (x, y) in black:
        for (dx, dy) in MOVEMENTS.values():
            neighbor_ct[(x+dx, y+dy)] += 1
    new_black = set()
    for (x, y) in black:
        if 1 <= neighbor_ct[(x, y)] <= 2:
            new_black.add((x, y))
    for (x, y) in neighbor_ct.keys() - black:
        if neighbor_ct[(x, y)] == 2:
            new_black.add((x, y))
    black = new_black
print(len(black))

from common import *

reg = re.compile(r'target area: x=(\d+)..(\d+), y=(-\d+)..(-\d+)')

def parse(x):
    groups = reg.match(x).groups()
    return int(groups[0]), int(groups[1]), int(groups[2]), int(groups[3])

minx, maxx, miny, maxy = filemap(parse, 'day17.txt')[0]

def attempt(dx, dy):
    x, y = 0, 0
    highest = 0
    while x <= maxx and y >= miny:
        x += dx
        y += dy
        dx -= 1
        if dx < 0:
            dx = 0
        dy -= 1
        highest = max(highest, y)
        if minx <= x <= maxx and miny <= y <= maxy:
            return highest
    return None

p1 = 0
p2 = 0
for dy in range(1000, miny-1, -1):
    for dx in range(maxx, 1, -1):
        a = attempt(dx, dy)
        if a is not None:
            p1 = max(p1, a)
            p2 += 1
print(p1)
print(p2)

from common import *

def transform(x):
    return x

data = filemap(transform, 'day12.txt')

def go_from(sx, sy):
    q = deque([(sx, sy, 0)])
    seen = set()
    dirs = set(DIRECTIONS.values())

    while q:
        x, y, d = q.popleft()
        cur_alt = data[x][y]
        if cur_alt == 'E':
            return d
        if cur_alt == 'S':
            cur_alt = 'a'

        for dx, dy in dirs:
            if (x+dx, y+dy) in seen:
                continue
            if x+dx < 0 or x+dx >= len(data) or y+dy < 0 or y+dy >= len(data[0]):
                continue
            this_alt = data[x+dx][y+dy]
            if this_alt == 'E':
                this_alt = 'z'
            if ord(this_alt) - 1 > ord(cur_alt):
                continue
            q.append((x+dx, y+dy, d+1))
            seen.add((x+dx, y+dy))

for x, i in enumerate(data):
    if 'S' in i:
        print(go_from(x, i.index('S')))

m = inf
for x, i in enumerate(data):
    for y, j in enumerate(i):
        if j == 'a':
            res = go_from(x, y)
            if res:
                m = min(m, go_from(x, y))
print(m)


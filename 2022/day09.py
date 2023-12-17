from common import *

def transform(x):
    i, j = x.split(' ')
    return i, int(j) 

data = filemap(transform, 'day09.txt')

def move_rel(h, t):
    hx, hy = h
    tx, ty = t
    if hx == tx:
        if ty < hy-1:
            ty = hy-1
        elif ty > hy+1:
            ty = hy+1
    elif hy == ty:
        if tx < hx-1:
            tx = hx-1
        elif tx > hx+1:
            tx = hx+1
    elif abs(hx-tx) > 1 or abs(hy-ty) > 1:
        # I need a diagonal step
        if hx > tx:
            dx = 1
        else:
            dx = -1
        if hy > ty:
            dy = 1
        else:
            dy = -1
        tx += dx
        ty += dy
    return tx, ty

visited_1 = set([(0, 0)])
visited_9 = set([(0, 0)])
rope = [(0, 0) for _ in range(10)]

for dir, n in data:
    dx, dy = DIRECTIONS[dir]
    for _ in range(n):
        new_rope = [(rope[0][0] + dx, rope[0][1] + dy)]
        for t in rope[1:]:
            new_rope.append(move_rel(new_rope[-1], t))
        rope = new_rope
        print(rope)
        visited_1.add(new_rope[1])
        visited_9.add(new_rope[9])

print(len(visited_1))
print(len(visited_9))

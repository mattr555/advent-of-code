from common import *
from math import gcd, atan2, pi
from functools import cmp_to_key

data = filemap(lambda x: x, "day10.txt")

# data = '''.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##'''.split('\n')

# print(data.count('#'))

def totalDiv(a, b):
    if b == 0:
        return inf
    return a / b

def detects(x, y):
    detected = 0
    angles = {}
    for ty in range(len(data)):
        for tx in range(len(data[0])):
            if tx == x and ty == y:
                continue
            if data[ty][tx] == '#':
                g = gcd(ty - y, tx - x)
                dy = (ty - y) // g
                dx = (tx - x) // g
                for steps in range(1, g):
                    if data[y + steps * dy][x + steps * dx] == '#':
                        break
                else:
                    detected += 1
                    angles[(dx, dy)] = (tx, ty)
    return detected, x, y, angles


b = (0, -1, -1, {})
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            b = max(b, detects(x, y))
print(b[0])

def key(a):
    return -atan2(a[0], a[1])

l = list(sorted(b[3], key=key))
# poor man's phase shift

for ix, (i, j) in enumerate(l):
    if i >= 0 and j < 0:
        startIx = ix
        break

l = l[startIx:] + l[:startIx]
# print(l)

for ix, k in enumerate(l):
    if ix == 199:
        # print(b)
        print(b[3][k][0] * 100 + b[3][k][1])

# print(list(map(lambda i: b[3][i], l)))

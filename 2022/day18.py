from common import *

def transform(x):
    return tuple(map(int, x.split(',')))

data = set(filemap(transform, 'day18.txt'))

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def naive_sf(pts):
    ct = 0
    for x, y, z in pts:
        for dx, dy, dz in DIRS:
            if (x+dx, y+dy, z+dz) not in pts:
                ct += 1
    return ct

print(naive_sf(data))

minx = min(x[0] for x in data) - 1
miny = min(x[1] for x in data) - 1
minz = min(x[2] for x in data) - 1
maxx = max(x[0] for x in data) + 1
maxy = max(x[1] for x in data) + 1
maxz = max(x[2] for x in data) + 1

s = set()
q = set([(minx, miny, minz)])
while q:
    x, y, z = q.pop()
    s.add((x, y, z))
    for dx, dy, dz in DIRS:
        nx, ny, nz = x+dx, y+dy, z+dz
        if minx <= nx <= maxx and miny <= ny <= maxy and minz <= nz <= maxz and (nx, ny, nz) not in data and (nx, ny, nz) not in s:
            q.add((nx, ny, nz))

lx = maxx - minx + 1
ly = maxy - miny + 1
lz = maxy - minz + 1
outside_sf = 2 * lx * ly + 2 * ly * lz + 2 * lx * lz

print(naive_sf(s) - outside_sf)

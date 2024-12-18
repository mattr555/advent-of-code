from collections import defaultdict, deque, Counter, namedtuple
import math
from math import inf, gcd
from copy import deepcopy
import itertools
import re
from dataclasses import dataclass
from tqdm import tqdm

def filemap(func, filename, sep='\n', chunksize=None):
    with open(filename) as f:
        raw = f.read().strip().split(sep)
        if chunksize:
            raw = chunk(raw, chunksize)
        return list(map(func, raw))


DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),

    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),

    1: (0, 1),
    4: (1, 0),
    2: (0, -1),
    3: (-1, 0), 
}

DIRECTIONS_DIAGS = {
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
}

def chunk(l, n):
    return [l[i*n:(i+1)*n] for i in range(len(l) // n)]

def denseGrid(r, c, val=None):
    return [[val] * c for _ in range(r)]

FULL_BLOCK = "█"
LIGHT_SHADE = "░"
MEDIUM_SHADE = "▒"
DARK_SHADE = "▓"

def lcm(a, b):
    return (a * b) // gcd(a, b)

def sign(x):
    if x == 0:
        return 0
    return x // abs(x)

# transpose along major axis
def transpose(l):
    return list(map(list, zip(*l)))

def major_diag(b, opposite=False):
    d = []
    for ix in range(len(b)):
        if opposite:
            d.append(b[ix][-(ix+1)])
        else:
            d.append(b[ix][ix])
    return d

def all_diag(grid):
    ret = []
    for dist in range(len(grid) + len(grid[0])):
        d = []
        for i in range(dist+1):
            a = i
            b = dist - i
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                d.append(grid[a][b])
        ret.append(d)
    return ret

def getitem(ix):
    return lambda i: i[ix]

def product(l):
    n = 1
    for i in l:
        n *= i
    return n

def neighbors(grid, y, x, diags=False):
    if diags:
        directions = DIRECTIONS_DIAGS
    else:
        directions = DIRECTIONS.values()

    for (dx, dy) in directions:
        if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid[y]):
            yield (y+dy, x+dx), grid[y+dy][x+dx]

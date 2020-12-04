from collections import defaultdict, deque, Counter
import math
from math import inf, gcd
import itertools
import re

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

def transpose(l):
    return list(map(list, zip(*l)))

def getitem(ix):
    return lambda i: i[ix]

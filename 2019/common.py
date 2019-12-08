from collections import defaultdict, deque, Counter
import itertools

def filemap(func, filename, sep='\n'):
    with open(filename) as f:
        return list(map(func, f.read().strip().split(sep)))


DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),

    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0)
}


def chunk(l, n):
    for i in range(len(l) // n):
        yield l[i*n:(i+1)*n]

def denseGrid(r, c):
    return [[None] * c for _ in range(r)]


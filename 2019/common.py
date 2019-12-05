from collections import defaultdict, deque

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

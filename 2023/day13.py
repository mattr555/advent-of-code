from common import *

def transform(x):
    return x.split('\n')

data = filemap(transform, 'day13.txt', sep='\n\n')

p1 = 0
p2 = 0

def same(a, b):
    return all(x == y for x, y in zip(a, b))

for grid in data:
    for row in range(0, len(grid)-1):
        if same(grid[row::-1], grid[row+1:]):
            p1 += 100 * (row+1)

    grid = transpose(grid)
    for row in range(0, len(grid)-1):
        if same(grid[row::-1], grid[row+1:]):
            p1 += row + 1
print(p1)

def off_by_one(a, b):
    l = [x != y for x, y in zip(a, b)]
    if sum(l) == 1:
        return l.index(True)
    return None

for grid in data:
    for row in range(0, len(grid)-1):
        obo = off_by_one(grid[row::-1], grid[row+1:])
        if obo is not None:
            # compare the mismatched row to see if we can replace one cell
            obo2 = off_by_one(grid[row+1+obo], grid[row-obo])
            if obo2 is not None:
                p2 += 100 * (row+1)

    grid = transpose(grid)
    for row in range(0, len(grid)-1):
        obo = off_by_one(grid[row::-1], grid[row+1:])
        if obo is not None:
            # compare the mismatched row to see if we can replace one cell
            obo2 = off_by_one(grid[row+1+obo], grid[row-obo])
            if obo2 is not None:
                p2 += (row+1)
print(p2)

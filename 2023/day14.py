from common import *

def transform(x):
    return list(x)

data = filemap(transform, 'day14.txt')

p1 = 0
p2 = 0

def tilt(grid, dy, dx):
    new_grid = deepcopy(grid)
    if dy == 0:
        new_grid = transpose(new_grid)
    
    if dy > 0 or dx > 0:
        new_grid.reverse()

    for y in range(len(new_grid)):
        for x in range(len(new_grid[0])):
            if new_grid[y][x] == 'O':
                ny = y - 1
                while ny >= 0 and new_grid[ny][x] not in 'O#':
                    ny -= 1
                new_grid[ny+1][x] = 'O'
                if ny+1 != y:
                    new_grid[y][x] = '.'

    if dy > 0 or dx > 0:
        new_grid.reverse()
    if dy == 0:
        new_grid = transpose(new_grid)
    return new_grid

def loading_factor(grid):
    n = 0
    for ix, row in enumerate(grid):
        n += row.count('O') * (len(grid) - ix)
    return n

grid = tilt(data, -1, 0)
print(loading_factor(grid))

results = defaultdict(list)

grid = data
cycle = 0
first_match = inf
for cycle in range(10000):
    grid = tilt(grid, -1, 0)
    grid = tilt(grid, 0, -1)
    grid = tilt(grid, 1, 0)
    grid = tilt(grid, 0, 1)
    result = '\n'.join(''.join(x) for x in grid)
    if result in results:
        first_match = min(first_match, cycle)
        if len(results[result]) == 2:
            cycle_length = results[result][1][1] - results[result][0][1]
            break
    results[result].append((loading_factor(grid), cycle))

offset_i_want = (1000000000 - first_match - 1) % cycle_length
for l in results.values():
    for ans, offset in l:
        if offset - first_match == offset_i_want:
            print(ans)


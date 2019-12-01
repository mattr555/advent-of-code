with open("day18.txt") as f:
    grid = list(map(list, f.read().strip('\n').split('\n')))

OPEN = '.'
TREE = '|'
YARD = '#'

def iterate(grid):
    new_grid = []
    for y in range(len(grid)):
        new_row = []
        for x in range(len(grid[0])):
            o = 0
            t = 0
            l = 0
            for dy in range(max(0, y-1), min(len(grid), y+2)):
                for dx in range(max(0, x-1), min(len(grid[0]), x+2)):
                    if grid[dy][dx] == OPEN:
                        o += 1
                    elif grid[dy][dx] == TREE:
                        t += 1
                    elif grid[dy][dx] == YARD:
                        l += 1
            
            if grid[y][x] == OPEN:
                if t >= 3:
                    new_row.append(TREE)
                else:
                    new_row.append(OPEN)
            elif grid[y][x] == TREE:
                if l >= 3:
                    new_row.append(YARD)
                else:
                    new_row.append(TREE)
            elif grid[y][x] == YARD:
                if l >= 2 and t >= 1:
                    new_row.append(YARD)
                else:
                    new_row.append(OPEN)
                
        new_grid.append(new_row)
    
    return new_grid

def printGrid(grid):
    for i in grid:
        print(''.join(i))

def value(grid):
    wooded = 0
    yards = 0
    for r in grid:
        for i in r:
            if i == YARD:
                yards += 1
            elif i == TREE:
                wooded += 1
    return wooded * yards

for i in range(10):
    grid = iterate(grid)

print("part1:", value(grid))

for i in range(10, 3500):
    if i % 100 == 0:
        print(i, ":", value(grid))

    grid = iterate(grid)


        
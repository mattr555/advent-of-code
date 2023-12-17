from common import *

def transform(x):
    return x

data = filemap(transform, 'day17.txt')[0]
data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

TURNS = 2022
TURNS = 1000000

def move_side(rock, x, y, dir, grid):
    dx = {'>': 1, '<': -1}[dir]
    can_move = True
    for rx, ry in rock:
        newx = rx + x + dx
        if newx < 0 or newx > 6:
            can_move = False
        elif (newx, y+ry) in grid:
            can_move = False
    if can_move:
        return x + dx, y
    else:
        return x, y

def move_down(rock, x, y, grid):
    can_move = True
    for rx, ry in rock:
        newy = ry + y - 1
        if newy < 0:
            can_move = False
        elif (x+rx, newy) in grid:
            can_move = False
    if can_move:
        return False, (x, y - 1)
    else:
        return True, (x, y)

def insert_rock(rock, x, y, grid, maxy):
    for rx, ry in rock:
        grid.add((rx + x, ry + y))
        maxy = max(maxy, ry+y)
    return maxy

grid = set()
move = 0
maxy = -1
for turn in tqdm(range(TURNS)):
    rock = ROCKS[turn % len(ROCKS)]
    x = 2
    y = maxy + 4

    if turn % len(ROCKS) == 0 and move % len(data) == 0:
        print(move, turn)
    
    while True:
        x, y = move_side(rock, x, y, data[move % len(data)], grid)
        move += 1
        stopped, (x, y) = move_down(rock, x, y, grid)

        if stopped:
            maxy = insert_rock(rock, x, y, grid, maxy)
            break

print(maxy + 1)

# def print_grid(grid):
#     for y in range(max(i[1] for i in grid), -1, -1):
#         for x in range(7):
#             if (x, y) in grid:
#                 print('#', end='')
#             else:
#                 print('.', end='')
#         print()

# print_grid(grid)
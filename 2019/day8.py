from common import *

WIDTH = 25
HEIGHT = 6

with open("day8.txt") as f:
    data = list(map(int, f.read().strip()))

fewest = Counter([0] * HEIGHT * WIDTH)
layers = chunk(data, HEIGHT * WIDTH)
for layer in layers:
    c = Counter(layer)
    if c[0] < fewest[0]:
        fewest = c

print(fewest[1] * fewest[2])

grid = [2] * (HEIGHT * WIDTH)

for layer in layers:
    for ix, i in enumerate(layer):
        if grid[ix] == 2 and i != 2:
            grid[ix] = i

for r in chunk(grid, WIDTH):
    for i in r:
        if i == 0:
            print("█", end="")
        else:
            print(" ", end="")
    print()

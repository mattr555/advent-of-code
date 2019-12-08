from common import *

WIDTH = 25
HEIGHT = 6

with open("day8.txt") as f:
    data = list(map(int, f.read().strip()))

from collections import Counter

fewest = Counter([0] * HEIGHT * WIDTH)
layers = []
for i in range(len(data) // (HEIGHT * WIDTH)):
    layer = data[i*HEIGHT*WIDTH:(i+1)*HEIGHT*WIDTH]
    c = Counter(layer)
    layers.append(layer)
    # print(c)
    if c[0] < fewest[0]:
        fewest = c

print(fewest[1] * fewest[2])

grid = [2] * (HEIGHT * WIDTH)

for layer in layers:
    for ix, i in enumerate(layer):
        if grid[ix] == 2 and i != 2:
            grid[ix] = i
    print(grid.count(2))

for i in range(HEIGHT):
    for j in range(WIDTH):
        if grid[i * WIDTH + j] == 0:
            print("█", end="")
        else:
            print(" ", end="")
    print()

print(grid)
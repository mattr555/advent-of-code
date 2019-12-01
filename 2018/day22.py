MOD = 20183
DEPTH = 7740

target = (12, 763)

grid = []
for i in range(target[1] + 1):
    grid.append([0] * (target[0] + 1))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if y == 0:
            grid[y][x] = (x * 16807) % MOD
        elif x == 0:
            grid[y][x] = (y * 48271) % MOD
        elif (x, y) == target:
            grid[y][x] = 0
        else:
            grid[y][x] = (grid[y][x-1] * grid[y-1][x]) % MOD
        grid[y][x] += DEPTH
        grid[y][x] %= MOD

part1 = 0

for r in grid:
    for i in r:
        part1 += i % 3

print(part1)
        
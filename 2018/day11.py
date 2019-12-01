serial_number = 5468

def power_level(x, y, num=serial_number):
    rack_id = x + 10
    level = rack_id * y
    level += num
    level *= rack_id
    level //= 100
    level %= 10
    return level - 5

assert power_level(122, 79, 57) == -5
assert power_level(217, 196, 39) == 0

ans = 0
coord = (0, 0)
for x in range(1, 298):
    for y in range(298):
        this_sum = 0
        for dx in range(3):
            for dy in range(3):
                this_sum += power_level(x + dx, y + dy)
        if this_sum > ans:
            ans = this_sum
            coord = (x, y)

print(ans)
print(coord)

grid = []
for x in range(300):
    grid.append([power_level(x, y) for y in range(300)])

prefix_table = []
for row in grid:
    res = [0]
    s = 0
    for i in row:
        s += i
        res.append(s)
    prefix_table.append(res)

ans = 0
coord = (0, 0)
for square_size in range(1, 301):
    for x in range(1, 301 - square_size):
        for y in range(1, 301 - square_size):
            this_sum = 0
            for r in range(square_size):
                this_sum += prefix_table[x+r][y+square_size] - prefix_table[x+r][y]
                # for dy in range(square_size):
                #     this_sum += grid[x+dx][y+dy]
            if this_sum > ans:
                ans = this_sum
                coord = (x, y, square_size)
    print(square_size, coord, "done")
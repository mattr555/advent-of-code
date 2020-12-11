from common import *

def parse(s):
    return list(s)

data = filemap(parse, 'day11.txt')
curr = data

last = ''
while repr(curr) != last:
    next = denseGrid(len(curr), len(curr[0]))
    last = repr(curr)
    for y in range(len(curr)):
        for x in range(len(curr[0])):
            neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1,0,1]:
                    if 0 <= x+dx < len(curr[0]) and 0 <= y+dy < len(curr) and not (dx == 0 and dy == 0):
                        neighbors += 1 if curr[y+dy][x+dx] == '#' else 0
            if curr[y][x] == '#':
                next[y][x] = 'L' if neighbors >= 4 else '#'
            elif curr[y][x] == 'L':
                next[y][x] = '#' if neighbors == 0 else 'L'
            else:
                next[y][x] = '.'
    curr = next
print(sum(i.count('#') for i in curr))

curr = data
last = ''
while repr(curr) != last:
    next = denseGrid(len(curr), len(curr[0]))
    last = repr(curr)
    for y in range(len(curr)):
        for x in range(len(curr[0])):
            neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1,0,1]:
                    if (dx == dy == 0):
                        continue
                    look = 1
                    while True:
                        tx = x + look * dx
                        ty = y + look * dy
                        if not (0 <= tx < len(curr[0]) and 0 <= ty < len(curr)):
                            break
                        if curr[ty][tx] in 'L#':
                            neighbors += 1 if curr[ty][tx] == '#' else 0
                            break
                        look += 1
            if curr[y][x] == '#':
                next[y][x] = 'L' if neighbors >= 5 else '#'
            elif curr[y][x] == 'L':
                next[y][x] = '#' if neighbors == 0 else 'L'
            else:
                next[y][x] = '.'
    curr = next

print(sum(i.count('#') for i in curr))

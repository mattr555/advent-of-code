from common import *

def parse(s):
    return s[0], int(s[1:])

data = filemap(parse, 'day12.txt')

DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
COMPASS = 'NESW'

dir = 'E'
x = 0
y = 0
for command, n in data:
    if command in DIRECTIONS:
        x += DIRECTIONS[command][0] * n
        y += DIRECTIONS[command][1] * n
    elif command == 'F':
        x += DIRECTIONS[dir][0] * n
        y += DIRECTIONS[dir][1] * n
    elif command == 'L':
        dir = COMPASS[(COMPASS.index(dir) - (n // 90)) % 4]
    elif command == 'R':
        dir = COMPASS[(COMPASS.index(dir) + (n // 90)) % 4]
print(abs(x) + abs(y))

wpx = 10
wpy = 1
sx = 0
sy = 0
for command, n in data:
    if command in DIRECTIONS:
        wpx += DIRECTIONS[command][0] * n
        wpy += DIRECTIONS[command][1] * n
    elif command == 'F':
        sx += wpx * n
        sy += wpy * n
    elif (command, n) in [('L', 90), ('R', 270)]:
        wpx, wpy = -wpy, wpx
    elif (command, n) in [('L', 180), ('R', 180)]:
        wpx, wpy = -wpx, -wpy
    elif (command, n) in [('L', 270), ('R', 90)]:
        wpx, wpy = wpy, -wpx

print(abs(sx) + abs(sy))

from common import *

data = filemap(list, "day24.txt")

def gridToStr(g):
    return ''.join(''.join(i) for i in g)

def part1():
    def neighbors(l, x, y):
        n = 0
        if x > 0:
            n += 1 if l[y][x-1] == '#' else 0
        if y > 0:
            n += 1 if l[y-1][x] == '#' else 0
        if x < len(l[0])-1:
            n += 1 if l[y][x+1] == '#' else 0
        if y < len(l)-1:
            n += 1 if l[y+1][x] == '#' else 0
        return n

    def step(l):
        ret = []
        for y in range(len(l)):
            ret.append([])
            for x in range(len(l[0])):
                new = ''
                if l[y][x] == '#':
                    new = '#' if neighbors(l, x, y) == 1 else '.'
                else:
                    new = '#' if 1 <= neighbors(l, x, y) <= 2 else '.'
                ret[-1].append(new)
        return ret


    s = set()
    grid = list(data)
    while True:
        gs = gridToStr(grid)
        if gs in s:
            break
        else:
            s.add(gs)
        grid = step(grid)

    def biodiversity(s):
        p = 1
        ans = 0
        for i in s:
            if i == '#':
                ans += p
            p <<= 1
        return ans

    return biodiversity(gs)

print(part1())

DIRS = set(DIRECTIONS.values())

def part2():
    grid = defaultdict(lambda: [['.'] * 5 for _ in range(5)])
    grid[0] = list(data)

    def neighbors(g, level, x, y):
        ans = []
        for dx, dy in DIRS:
            tx, ty = x+dx, y+dy
            if tx == -1:
                ans.append(g[level-1][2][1])
            elif tx == 5:
                ans.append(g[level-1][2][3])
            elif ty == -1:
                ans.append(g[level-1][1][2])
            elif ty == 5:
                ans.append(g[level-1][3][2])
            elif tx == 2 and ty == 2:
                # inner
                if x == 1:
                    for i in range(5):
                        ans.append(g[level+1][i][0])
                elif x == 3:
                    for i in range(5):
                        ans.append(g[level+1][i][4])
                elif y == 1:
                    for i in range(5):
                        ans.append(g[level+1][0][i])
                elif y == 3:
                    for i in range(5):
                        ans.append(g[level+1][4][i])
            else:
                ans.append(g[level][ty][tx])
        return ans.count('#')

    def step(g):
        ret = defaultdict(lambda: [['.'] * 5 for _ in range(5)])
        for level in range(min(g.keys()) - 1, max(g.keys()) + 2):
            l = g[level]
            newL = []
            for y in range(len(l)):
                newL.append([])
                for x in range(len(l[0])):
                    new = ''
                    if x == 2 and y == 2:
                        new = '.'
                    elif l[y][x] == '#':
                        new = '#' if neighbors(g, level, x, y) == 1 else '.'
                    else:
                        new = '#' if 1 <= neighbors(g, level, x, y) <= 2 else '.'
                    newL[-1].append(new)
            ret[level] = newL
        return ret
    
    for _ in range(200):
        grid = step(grid)
    
    total = 0
    for i in grid.values():
        total += gridToStr(i).count('#')
    return total

print(part2())
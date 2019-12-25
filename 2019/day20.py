from common import *
from string import ascii_uppercase

DIRS = set(DIRECTIONS.values())

data = []
for line in open("day20.txt").readlines():
    data.append(line.strip('\n'))

grid = set()
portals = defaultdict(lambda: None)
portalLocs = defaultdict(list)
for y in range(2, len(data)-2):
    for x in range(2, len(data[0])-2):
        if data[y][x] == '.':
            grid.add((x, y))
            for (dx, dy) in DIRS:
                if data[y+dy][x+dx] in ascii_uppercase:
                    thisLetter = data[y+dy][x+dx]
                    otherLetter = data[y+(dy*2)][x+(dx*2)]
                    if dy < 0 or dx < 0:
                        pID = otherLetter+thisLetter
                    else:
                        pID = thisLetter+otherLetter
                    
                    isOuter = False
                    if x == 2 or x == len(data[0])-3 or y == 2 or y == len(data)-3:
                        isOuter = True

                    portals[(x, y)] = (pID, isOuter)
                    portalLocs[pID].append((x, y))

# print(portals)
# print(portalLocs)

def search(withLevels=False):
    startPos = portalLocs['AA'][0]
    q = deque([(startPos[0], startPos[1], 0, 0)])
    s = set()
    while len(q) > 0:
        x, y, level, steps = q.popleft()
        # if steps % 100 == 0:
        #     print(steps)

        for dx, dy in DIRS:
            t = (x+dx, y+dy)
            if (t[0], t[1], level) not in s and t in grid:
                s.add((t[0], t[1], level))
                q.append((t[0], t[1], level, steps+1))

        if (x, y) in portals:
            pID, isOuter = portals[(x, y)]
            if pID == 'AA':
                continue
            if pID == 'ZZ':
                if level == 0:
                    return steps
                else:
                    continue

            possible = portalLocs[pID][0]
            if possible == (x, y):
                possible = portalLocs[pID][1]

            nextLevel = 0
            if withLevels:
                nextLevel = level-1 if isOuter else level+1

            if nextLevel >= 0 and (possible[0], possible[1], nextLevel) not in s:
                s.add((possible[0], possible[1], nextLevel))
                q.append((possible[0], possible[1], nextLevel, steps+1))
        
print(search())
print(search(True))


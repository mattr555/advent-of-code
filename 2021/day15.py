from common import *
from heapq import heappush, heappop

def parse(x):
    return [int(y) for y in x]

data = filemap(parse, 'day15.txt')

def risk(data, x, y):
    xct, xm = divmod(x, len(data))
    yct, ym = divmod(y, len(data[0]))
    return ((data[xm][ym] + xct + yct - 1) % 9) + 1

# dp = denseGrid(len(data)*5, len(data[0])*5, 0)
# for x in range(len(dp)-1, -1, -1):
#     for y in range(len(dp[0])-1, -1, -1):
#         m = inf
#         if x < len(dp) - 1:
#             m = min(m, dp[x+1][y])
#         if y < len(dp[0]) - 1:
#             m = min(m, dp[x][y+1])
#         if m == inf:
#             m = 0
#         dp[x][y] = m + risk(data, x, y)
# print(dp[0][0] - data[0][0])

for mult in (1, 5):
    boundx = len(data) * mult
    boundy = len(data[0]) * mult

    def neighbors(x, y):
        n = []
        for tx, ty in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
            if tx >= 0 and tx < boundx and ty >= 0 and ty < boundy:
                n.append((tx, ty))
        return n

    seen = set()
    to_visit = [(0, 0, 0)]
    while to_visit:
        distance, x, y = heappop(to_visit)
        if x == boundx-1 and y == boundy - 1:
            print(distance)
            break
        for xi, yi in neighbors(x, y):
            if (xi, yi) not in seen:
                seen.add((xi, yi))
                heappush(to_visit, (distance+risk(data, xi, yi), xi, yi))



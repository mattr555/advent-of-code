from common import *

def transform(x):
    return [int(i) for i in x]

data = filemap(transform, 'day08.txt')
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

p1 = 0
p2 = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        scenic_score = 1
        edge_viz = False
        for dx, dy in directions:
            n = 1
            while True:
                nx = x+dx*n
                ny = y+dy*n
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                    edge_viz = True
                    break
                n += 1
                if data[nx][ny] >= data[x][y]:
                    break
            scenic_score *= n-1
        if edge_viz:
            p1 += 1
        p2 = max(p2, scenic_score)

print(p1)
print(p2)

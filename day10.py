class Point(object):
    def __init__(self, s):
        self.x = int(s[10:16])
        self.y = int(s[17:24])
        self.dx = int(s[36:38])
        self.dy = int(s[40:42])
    
    def step(self, n=1):
        self.x += self.dx * n
        self.y += self.dy * n

with open("day10.txt") as f:
    data = list(map(Point, f.read().strip().split('\n')))

# while data[0].y > 10:
# for _ in range(10000):
for i in data:
    i.step(9950)

def printGrid(points):
    grid = []
    min_x = min(points, key=lambda i: i.x).x
    min_y = min(points, key=lambda i: i.y).y
    max_x = max(points, key=lambda i: i.x).x
    max_y = max(points, key=lambda i: i.y).y

    for i in range(max_y - min_y + 1):
        grid.append(['.'] * (max_x - min_x + 1))
    
    for point in points:
        grid[point.y - min_y][point.x - min_x] = '#'
    
    out = ''
    for row in grid:
        out += ''.join(row)
        out += '\n'
    return out

for stepCount in range(9950, 10050):
    with open("day10/step-{}.txt".format(stepCount), 'w') as f:
        f.write(printGrid(data))
    
    if stepCount == 10027:
        print(printGrid(data).replace('.', ' '))
        print(stepCount)
    
    for i in data:
        i.step()
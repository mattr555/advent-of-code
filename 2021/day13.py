from common import *

points, folds = filemap(lambda x: x, 'day13.txt', '\n\n')
points = set(map(lambda x: tuple(map(int, x.split(','))), points.split('\n')))
folds = list(map(lambda x: (x[11], int(x[13:])), folds.split('\n')))

for f_ix, (fdir, fn) in enumerate(folds):
    new_points = set()
    for x, y in points:
        if fdir == 'x' and x > fn:
            new_points.add((2*fn - x, y))
        elif fdir == 'y' and y > fn:
            new_points.add((x, 2*fn - y))
        else:
            new_points.add((x, y))
    points = new_points

    if f_ix == 0:
        print(len(points))

maxX = max([i[0] for i in points])
maxY = max([i[1] for i in points])
grid = denseGrid(maxY+1, maxX+1, ' ')
for x, y in points:
    grid[y][x] = FULL_BLOCK
for l in grid:
    print(''.join(l))

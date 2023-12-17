from common import *
import heapq

def transform(x):
    return list(map(int, x))

grid = filemap(transform, 'day17.txt')

p1 = 0
p2 = 0

def build_graph(min_dist, max_dist):
    to_visit = set([(0, 0, '-'), (0, 0, '|')])
    edges = defaultdict(set)

    while to_visit:
        y, x, dir = to_visit.pop()
        if (y, x, dir) in edges:
            continue

        if dir == '|':
            # can go E or W from here
            for d in (1, -1):
                s = 0
                for dx in range(1, max_dist+1):
                    nx = x+(d*dx)
                    if 0 <= nx < len(grid[0]):
                        s += grid[y][nx]
                        if dx >= min_dist:
                            edges[(y, x, dir)].add((y, nx, '-', s))
                            to_visit.add((y, nx, '-'))

        else:
            # can go N or S from here
            for d in (1, -1):
                s = 0
                for dy in range(1, max_dist+1):
                    ny = y+(d*dy)
                    if 0 <= ny < len(grid):
                        s += grid[ny][x]
                        if dy >= min_dist:
                            edges[(y, x, dir)].add((ny, x, '|', s))
                            to_visit.add((ny, x, '|'))

    return edges


def dijkstra(edges):
    # distance, y, x, dir
    q = [(0, 0, 0, '-'), (0, 0, 0, '|')]
    distance = defaultdict(lambda: inf)
    distance[(0, 0, '-')] = 0
    distance[(0, 0, '|')] = 0
    heapq.heapify(q)

    while q:
        last_dist, y, x, dir = heapq.heappop(q)
        if last_dist == distance[(y, x, dir)]:
            for oy, ox, od, w in edges[(y, x, dir)]:
                alt = last_dist + w
                if alt < distance[(oy, ox, od)]:
                    distance[(oy, ox, od)] = alt
                    heapq.heappush(q, (alt, oy, ox, od))
    
    return min(distance[(len(grid)-1, len(grid[0])-1, '-')], distance[(len(grid)-1, len(grid[0])-1, '|')])

print(dijkstra(build_graph(1, 3)))
print(dijkstra(build_graph(4, 10)))


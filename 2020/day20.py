from common import *

class Tile(object):
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid
    
    def possible_edges(self):
        l = ['', '', '', '']
        for i in range(len(self.grid)):
            l[0] += self.grid[0][i]
            l[1] += self.grid[i][-1]
            l[2] += self.grid[-1][-(i+1)]
            l[3] += self.grid[-(i+1)][0]
        return l
    
    def edge(self, n):
        all_edges = self.possible_edges()
        if n < 4:
            return all_edges[n]
        return ''.join(reversed(all_edges[n % 4]))
    
    def grid_for_orient(self, orient):
        l = ['', '', '', '']
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                l[0] += self.grid[i][j]
                l[1] += self.grid[j][-(i+1)]
                l[2] += self.grid[-(i+1)][-(j+1)]
                l[3] += self.grid[-(j+1)][i]
        if orient > 3:
            non_cropped = [''.join(reversed(x)) for x in chunk(l[orient-4], len(self.grid))]
        else:
            non_cropped = chunk(l[orient], len(self.grid))
        return [s[1:-1] for s in non_cropped][1:-1]

tile_size = 0
def parse(s):
    global tile_size
    id = int(s[5:9])
    l = s.split('\n')[1:]
    tile_size = len(l)
    return id, Tile(id, l)

data = dict(filemap(parse, 'day20.txt', sep='\n\n'))

edges = defaultdict(set)
for i in data.values():
    for ix, e in enumerate(i.possible_edges()):
        edges[e].add((i.id, ix))
        edges[''.join(reversed(e))].add((i.id, ix+4))

edge_lookup = {}
non_matching_edges = defaultdict(set)
for i in edges.values():
    if len(i) == 1:
        tile_id, orient = next(iter(i))
        non_matching_edges[tile_id].add(orient)
    else:
        it = iter(i)
        a = next(it)
        b = next(it)
        edge_lookup[a] = b
        edge_lookup[b] = a

p1 = 1
for k, v in non_matching_edges.items():
    if len(v) == 4:
        p1 *= k
        corner_to_start = k

dim = int(math.sqrt(len(data)))
grid_layout = denseGrid(dim, dim)

for candidate_top in range(4):
    if candidate_top in non_matching_edges[corner_to_start] and (candidate_top + 3) % 4 in non_matching_edges[corner_to_start]:
        grid_layout[0][0] = (corner_to_start, candidate_top)
        break

def rightmost(tile):
    m = {0:1, 1:2, 2:3, 3:0, 4:7, 7:6, 6:5, 5:4}
    return tile[0], m[tile[1]]

def bottommost(tile):
    m = {0:2, 1:3, 2:0, 3:1, 4:6, 7:5, 6:4, 5:7}
    return tile[0], m[tile[1]]

def top_for_left(edge):
    #note: it's the same as the rightmost function!
    m = {0:1, 1:2, 2:3, 3:0, 4:7, 7:6, 6:5, 5:4}
    return edge[0], m[edge[1]]

def flip(tile):
    return tile[0], (tile[1] + 4) % 8

for row in range(dim):
    if row != 0:
        edge_to_match = bottommost(grid_layout[row-1][0])
        grid_layout[row][0] = flip(edge_lookup[edge_to_match])
    
    for col in range(1, dim):
        edge_to_match = rightmost(grid_layout[row][col-1])
        grid_layout[row][col] = top_for_left(flip(edge_lookup[edge_to_match]))

grid = ['' for _ in range(dim*(tile_size-2))]
for rn, row in enumerate(grid_layout):
    for tile_id, orient in row:
        subgrid = data[tile_id].grid_for_orient(orient)
        for ix, i in enumerate(subgrid):
            grid[rn*(tile_size-2)+ix] += i

def hash_locations(g):
    return set((i, j) for i in range(len(g)) for j in range(len(g[0])) if g[i][j] == '#')

print('\n'.join(grid))
water_locations = hash_locations(grid)

sea_monster = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

monster_locations = hash_locations(sea_monster)

def find_monsters(g):
    water_locations = hash_locations(g)
    for i in range(len(g) - len(sea_monster)):
        for j in range(len(g) - len(sea_monster[0])):
            to_check = set((i+di, j+dj) for (di, dj) in monster_locations)
            if all(g[ti][tj] == '#' for (ti, tj) in to_check):
                water_locations -= to_check
    return len(water_locations)

def flip_grid(g):
    return [''.join(reversed(x)) for x in g]

def rotate_grid(g):
    l = []
    for i in range(len(g)):
        l.append('')
        for j in range(len(g)):
            l[-1] += g[j][-(i+1)]
    return l

print('part 1', p1)

r = grid
for rotation in range(4):
    r = rotate_grid(r)
    a = find_monsters(r)
    if a != len(water_locations):
        print('part 2', a)
    a = find_monsters(flip_grid(r))
    if a != len(water_locations):
        print('part 2', a)

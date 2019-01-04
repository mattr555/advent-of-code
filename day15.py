MAX_INT = 1000000

def printGrid(grid):
    for i in grid:
        print(''.join(map(str, i)))

def in_range(units, grid, kind):
    ans = []
    for i in units:
        if kind == i.kind:
            for x, y in [(i.x + 1, i.y), (i.x - 1, i.y), (i.x, i.y+1), (i.x, i.y-1)]:
                if grid[y][x] == '.':
                    ans.append((y, x))
    return ans

def pts_in_range(pt, grid, kind):
    ans = []
    y, x = pt
    for oy, ox in [(y+1, x), (y, x+1), (y, x-1), (y-1, x)]:
        if grid[oy][ox] == kind:
            ans.append((oy, ox))
    return ans

def unit_at(point, units):
    for i in units:
        if point[0] == i.y and point[1] == i.x:
            return i

def movement_grid(start, grid):
    ans = []
    for _ in range(len(grid)):
        ans.append([(MAX_INT, None)] * len(grid[0]))
    
    def floodFill(pt, depth, last):
        y, x = pt
        if depth < ans[y][x][0] or (depth == ans[y][x][0] and last < ans[y][x][1]):
            ans[y][x] = (depth, last)
            for oy, ox in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
                if grid[oy][ox] == '.':
                    floodFill((oy, ox), depth + 1, pt)
    
    floodFill(start, 0, None)
    return ans

def step_toward(target, move_grid):
    ty, tx = target
    depth, pt = move_grid[ty][tx]
    if pt is None:
        return None
    if depth == 1:
        return target
    ny, nx = pt
    while depth > 2:
        depth, (ny, nx) = move_grid[ny][nx]
    return ny, nx

def closest(pts, move_grid):
    best = (MAX_INT, None)
    for y, x in sorted(pts):
        dist = move_grid[y][x][0]
        if dist <= best[0]:
            next_step = step_toward((y, x), move_grid)
            if next_step is not None and (dist < best[0] or best[1] is None or next_step < best[1]):
                best = (dist, next_step)
    return best[1]

def done(units):
    return len(set(map(lambda i: i.kind, units))) < 2

MYENEMY = {'G': 'E', 'E': 'G'}

class Unit(object):
    def __init__(self, x, y, kind, ap):
        self.x = x
        self.y = y
        self.kind = kind
        self.hp = 200
        self.ap = ap
    
    def move(self, units, grid):
        my_coord = (self.y, self.x)
        my_enemy = MYENEMY[self.kind]

        if not any(i.kind == my_enemy for i in units):
            return False

        if pts_in_range(my_coord, grid, my_enemy):
            return True
        
        possibles = in_range(units, grid, my_enemy)
        move_grid = movement_grid(my_coord, grid)
        next_step = closest(possibles, move_grid)

        print('me', my_coord)
        if next_step:
            # print('my target', my_target)
            grid[self.y][self.x] = '.'
            # next_step = step_toward(my_target, move_grid)
            print('next step', next_step)
            (self.y, self.x) = next_step
            grid[self.y][self.x] = self.kind
        
        return True
    
    def attack(self, units, grid):
        my_coord = (self.y, self.x)
        my_enemy = MYENEMY[self.kind]

        my_possibles = map(lambda pt: unit_at(pt, units), pts_in_range(my_coord, grid, my_enemy))
        my_possibles = list(sorted(my_possibles, key=lambda i: (i.hp, i.y, i.x)))

        if len(my_possibles) > 0:
            my_attack = my_possibles[0]
            my_attack.hp -= self.ap
            return my_attack


import sys
if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = 'day15.txt'

import copy
with open(fn) as f:
    orig_grid = list(map(list, f.read().strip('\n').split('\n')))

def outcome(units, rounds):
    return rounds * sum(map(lambda i: i.hp, units))

def play(grid, elf_attack=3, bail_on_elf_death=False):
    units = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in 'GE':
                units.append(Unit(x, y, grid[y][x], elf_attack if grid[y][x] == 'E' else 3))


    playing = True
    rounds = 0
    while playing:
        units.sort(key=lambda i: (i.y, i.x))
        next_units = units.copy()
        for i in units:
            if i.hp <= 0:
                continue
            should_continue = i.move(next_units, grid)
            if not should_continue:
                playing = False
                break
            my_attacked = i.attack(next_units, grid)
            if my_attacked and my_attacked.hp <= 0:
                grid[my_attacked.y][my_attacked.x] = '.'
                if my_attacked in next_units:
                    next_units.remove(my_attacked)
                if bail_on_elf_death and my_attacked.kind == 'E':
                    return None, 'G'
                    
        else:
            rounds += 1

            print("round", rounds)
            printGrid(grid)
        units = next_units

    return outcome(units, rounds), units[0].kind

part_1 = play(copy.deepcopy(orig_grid))[0]

elf_attack = 3
winner = 'G'
while winner == 'G':
    elf_attack += 1
    part_2, winner = play(copy.deepcopy(orig_grid), elf_attack, True)

print("part 1:", part_1)
print("part 2:", part_2)


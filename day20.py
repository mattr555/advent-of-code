with open("day20.txt") as f:
    data = f.read().strip()[1:-1]

# data = "WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))"

import sys
sys.setrecursionlimit(5000)

DIRECTIONS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

class Room(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def build(self, dir_, all_rooms):
        dx, dy = DIRECTIONS[dir_]
        connect_coords = (self.x + dx, self.y + dy)
        if connect_coords in all_rooms:
            room_to_connect = all_rooms[connect_coords]
        else:
            room_to_connect = Room(connect_coords[0], connect_coords[1])
            all_rooms[connect_coords] = room_to_connect
        
        if dir_ == 'N':
            self.north = room_to_connect
            room_to_connect.south = self
        elif dir_ == 'S':
            self.south = room_to_connect
            room_to_connect.north = self
        elif dir_ == 'E':
            self.east = room_to_connect
            room_to_connect.west = self
        else:
            self.west = room_to_connect
            room_to_connect.east = self
        
        return room_to_connect

class Expression(list):
    def __repr__(self):
        return "Expression" + super(Expression, self).__repr__()

class Branch(list):
    def __repr__(self):
        return "Branch" + super(Branch, self).__repr__()


all_rooms = {}
start_point = Room(0, 0)
all_rooms[(0, 0)] = start_point

def findBranchSplits(i):
    assert data[i] == '('
    depth = 1
    start = i+1
    splits = []
    while depth > 0:
        i += 1
        if data[i] == '(':
            depth += 1
        elif data[i] == ')':
            depth -= 1
        elif depth == 1 and data[i] == '|':
            splits.append((start, i))
            start = i+1
    splits.append((start, i))
    return i, splits

def parseExpression(i, end_point=len(data)):
    ret = Expression()
    while i < end_point:
        if data[i] in 'NESW':
            ret.append(data[i])
        elif data[i] == '(':
            branch, i = parseBranch(i)
            ret.append(branch)
        elif data[i] in '|)':
            raise Exception("ahh this shouldn't happen")
        i += 1
    return ret

def parseBranch(i):
    ret = Branch()
    end, splits = findBranchSplits(i)
    for s, e in splits:
        ret.append(parseExpression(s, e))
    return ret, end

r = parseExpression(0)
print(r)

#so the problem definition is more general than the actual input
#smh


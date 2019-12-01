TURNTABLE = {
    '^': '<^>',
    '>': '^>v',
    'v': '>v<',
    '<': 'v<^'
}

GRIDREPLACE = {
    '^': '|',
    'v': '|',
    '>': '-',
    '<': '-'
}

BACKSLASHTABLE = {
    '^': '<',
    '>': 'v',
    'v': '>',
    '<': '^'
}

FORWARDSLASHTABLE = {
    '^': '>',
    '>': '^',
    'v': '<',
    '<': 'v'
}

DX = {
    '<': -1,
    '>': 1
}

DY = {
    '^': -1,
    'v': 1
}

class Cart(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.nextTurn = 0
        self.collided = False
    
    def move(self, grid):
        self.x += DX.get(self.direction, 0)
        self.y += DY.get(self.direction, 0)
        
        new_space = grid[self.y][self.x]
        if new_space == '+':
            self.direction = TURNTABLE[self.direction][self.nextTurn]
            self.nextTurn += 1
            self.nextTurn %= 3
        elif new_space == '\\':
            self.direction = BACKSLASHTABLE[self.direction]
        elif new_space == '/':
            self.direction = FORWARDSLASHTABLE[self.direction]

def checkCollision(carts):
    l = map(lambda c: (c.x, c.y), carts)
    s = set()
    for i in l:
        if i in s:
            return i
        s.add(i)
    return None


with open("day13.txt") as f:
    grid = list(map(list, f.read().strip('\n').split('\n')))

carts = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] in 'v><^':
            carts.append(Cart(x, y, grid[y][x]))
            grid[y][x] = GRIDREPLACE[grid[y][x]]

ticks = 0
coll = None
while len(carts) > 1:
    carts.sort(key=lambda c: (c.y, c.x))
    new_carts = []
    for cart in carts:
        cart.move(grid)
        coll = checkCollision(carts)
        if coll is not None:
            print(coll)
            for c in carts:
                if (c.x, c.y) == coll:
                    c.collided = True
    
    for cart in carts:
        if not cart.collided:
            new_carts.append(cart)
    carts = new_carts
    ticks += 1

print(carts[0].x, carts[0].y)
print("ticks", ticks)
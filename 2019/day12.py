from common import *
import re

class Planet(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
    
    def potential(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    def kinetic(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

def m(l):
    r = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
    m = r.match(l)
    return Planet(int(m.group(1)), int(m.group(2)), int(m.group(3)))

data = filemap(m, "day12.txt")

def sign(x):
    if x == 0:
        return 0
    return x // abs(x)

from itertools import combinations
def step():
    for a, b in combinations(data, 2):
        a.vx += sign(b.x - a.x)
        b.vx -= sign(b.x - a.x)
        a.vy += sign(b.y - a.y)
        b.vy -= sign(b.y - a.y)
        a.vz += sign(b.z - a.z)
        b.vz -= sign(b.z - a.z)
    
    for i in data:
        i.step()

xs = {}
ys = {}
zs = {}
xf = False
yf = False
zf = False
s = 0
xn, yn, zn = 0, 0, 0

while not all((xf, yf, zf)):
    xk = tuple([i.x for i in data] + [i.vx for i in data])
    yk = tuple([i.y for i in data] + [i.vy for i in data])
    zk = tuple([i.z for i in data] + [i.vz for i in data])

    if not xf and xk in xs:
        # print(f"x cycle found at {xs[xk]} to {s}")
        xf = True
        xn = s
    elif not xf:
        xs[xk] = s
    if not yf and yk in ys:
        # print(f"y cycle found at {ys[yk]} to {s}")
        yf = True
        yn = s
    elif not yf:
        ys[yk] = s
    if not zf and zk in zs:
        # print(f"z cycle found at {zs[zk]} to {s}")
        zf = True
        zn = s
    elif not zf:
        zs[zk] = s
    
    step()
    s += 1

    if s == 1000:
        print(sum([i.potential() * i.kinetic() for i in data]))


from math import gcd
g2 = gcd(yn, zn)
g3 = gcd(xn, g2)
# print(g3)

lcm2 = (yn * zn) // g2
lcm3 = (xn * lcm2) // g3
# print(lcm3)

# ok i have no idea why it's divided by 2.
print(lcm3 // 2)

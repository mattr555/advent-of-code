from common import *
from itertools import combinations
import re

class Planet(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def gravitate(self, other):
        self.vx += sign(other.x - self.x)
        other.vx -= sign(other.x - self.x)
        self.vy += sign(other.y - self.y)
        other.vy -= sign(other.y - self.y)
        self.vz += sign(other.z - self.z)
        other.vz -= sign(other.z - self.z)
    
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

def step():
    for a, b in combinations(data, 2):
        a.gravitate(b)
    
    for i in data:
        i.step()

xs = {}
ys = {}
zs = {}
s = 0
xn, yn, zn = 0, 0, 0

while not all(i > 0 for i in (xn, yn, zn)):
    if xn == 0:
        xk = tuple([i.x for i in data] + [i.vx for i in data])
        if xk in xs:
            print(f"x cycle found at {xs[xk]} to {s}")
            xn = s
        else:
            xs[xk] = s

    if yn == 0:
        yk = tuple([i.y for i in data] + [i.vy for i in data])
        if yk in ys:
            print(f"y cycle found at {ys[yk]} to {s}")
            yn = s
        else:
            ys[yk] = s

    if zn == 0:
        zk = tuple([i.z for i in data] + [i.vz for i in data])
        if zk in zs:
            print(f"z cycle found at {zs[zk]} to {s}")
            zn = s
        else:
            zs[zk] = s

    step()
    s += 1

    if s == 1000:
        print(sum([i.potential() * i.kinetic() for i in data]))


print(lcm(lcm(xn, yn), zn))

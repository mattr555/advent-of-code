from common import *
from enum import Enum

class Node(object):
    def __init__(self, l=None, r=None):
        self.l = l
        self.r = r

    def __str__(self):
        return f'[{self.l},{self.r}]'

    def __repr__(self):
        return str(self)
    
    def __int__(self):
        return 3*int(self.l) + 2*int(self.r)

def parse(x):
    def go(n):
        if x[n] == '[':
            node = Node()
            node.l, n = go(n+1)
            assert x[n] == ','
            node.r, n = go(n+1)
            assert x[n] == ']'
            return node, n+1
        else:
            assert x[n].isdigit()
            return int(x[n]), n+1
    node, n = go(0)
    assert n == len(x)
    return node

trees = filemap(parse, 'day18.txt')

def add_to_leftmost(node, num):
    if type(node.l) is int:
        node.l += num
    else:
        add_to_leftmost(node.l, num)

def add_to_rightmost(node, num):
    if type(node.r) is int:
        node.r += num
    else:
        add_to_rightmost(node.r, num)

def do_explode(root):
    def go(n, depth):
        # returns direct_explode, child_explode, (propl, propr)
        if depth == 4:
            assert type(n.l) is int
            assert type(n.r) is int
            return True, True, (n.l, n.r)
        child_explode = False
        propl = None
        propr = None
        if type(n.l) is Node:
            direct_explode, child_explode, (propl, propr) = go(n.l, depth+1)
            if direct_explode:
                n.l = 0
            if propr:
                if type(n.r) is int:
                    n.r += propr
                else:
                    add_to_leftmost(n.r, propr)
                propr = None
        if not child_explode and type(n.r) is Node:
            direct_explode, child_explode, (propl, propr) = go(n.r, depth+1)
            if direct_explode:
                n.r = 0
            if propl:
                if type(n.l) is int:
                    n.l += propl
                else:
                    add_to_rightmost(n.l, propl)
                propl = None
        return False, child_explode, (propl, propr)
    _, child_explode, _ = go(root, 0)
    return child_explode

def do_split(n):
    done = False
    if type(n.l) is int and n.l >= 10:
        d, m = divmod(n.l, 2)
        n.l = Node(d, d+m)
        return True
    elif type(n.l) is Node:
        done = do_split(n.l)
    if not done and type(n.r) is int and n.r >= 10:
        d, m = divmod(n.r, 2)
        n.r = Node(d, d+m)
        return True
    elif not done and type(n.r) is Node:
        done = do_split(n.r)
    return done

def do_reduce(n):
    while True:
        if do_explode(n):
            continue
        if do_split(n):
            continue
        break


n = deepcopy(trees[0])
for i in trees[1:]:
    n = Node(n, deepcopy(i))
    do_reduce(n)
print(int(n))

best = 0
for a, b in itertools.combinations(trees, 2):
    n = Node(deepcopy(a), deepcopy(b))
    do_reduce(n)
    best = max(best, int(n))
    n = Node(deepcopy(b), deepcopy(a))
    do_reduce(n)
    best = max(best, int(n))
print(best)

from common import *

class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

inp = '394618527'

def solve(max_range, turns, p1=True):
    nodes = [None]
    for i in range(1, len(inp) + 1):
        nodes.append(Node(i, None))

    cup_head = nodes[int(inp[0])]
    p = cup_head
    for i in inp[1:]:
        p.next = nodes[int(i)]
        p = p.next

    for i in range(len(inp)+1, max_range + 1):
        n = Node(i, None)
        nodes.append(n)
        p.next = n
        p = p.next

    p.next = cup_head
    current = p.next

    for turn in range(turns):
        picked_up = current.next
        current.next = current.next.next.next.next

        vals = set([picked_up.val, picked_up.next.val, picked_up.next.next.val])

        next_cup = current.val - 1
        while next_cup in vals or next_cup == 0:
            next_cup -= 1
            next_cup %= max_range + 1

        dest = nodes[next_cup]
        picked_up.next.next.next = dest.next
        dest.next = picked_up

        current = current.next
    
    if p1:
        p = nodes[1]
        p = p.next
        while p.val != 1:
            print(p.val, end='')
            p = p.next
        print()
    else:
        print(nodes[1].next.val * nodes[1].next.next.val)

solve(9, 100, True)
solve(1_000_000, 10_000_000, False)

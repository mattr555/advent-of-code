from math import prod
from common import *

def pad(s):
    return '0' * (4 - len(s)) + s

def parse(x):
    return ''.join([pad(bin(int(y, 16))[2:]) for y in x])

data = filemap(parse, 'day16.txt')[0]

def packet(ix):
    version = int(data[ix:ix+3], 2)
    ptype = int(data[ix+3:ix+6], 2)
    if ptype == 4:
        next_ix = ix+6
        v = 0
        done = False
        while not done:
            v <<= 4
            v += int(data[next_ix+1:next_ix+5], 2)
            if data[next_ix] == '0':
                done = True
            next_ix += 5
        return (version, ptype, v), next_ix
    else:
        subpackets = []
        lentype = data[ix+6]
        if lentype == '0':
            bitslen = int(data[ix+7:ix+7+15], 2)
            next_ix = ix+7+15
            stop_ix = next_ix + bitslen
            while next_ix < stop_ix:
                subpkt, next_ix = packet(next_ix)
                subpackets.append(subpkt)
        elif lentype == '1':
            numpkts = int(data[ix+7:ix+7+11], 2)
            next_ix = ix+7+11
            for i in range(numpkts):
                subpkt, next_ix = packet(next_ix)
                subpackets.append(subpkt)
        return (version, ptype, subpackets), next_ix

pkt = packet(0)[0]

def part1(pkt):
    if type(pkt[2]) is int:
        return pkt[0]
    else:
        return pkt[0] + sum(part1(p) for p in pkt[2])
print(part1(pkt))

def eval(pkt):
    _, ptype, val = pkt
    if ptype == 0:
        return sum(eval(p) for p in val)
    elif ptype == 1:
        return prod(eval(p) for p in val)
    elif ptype == 2:
        return min(eval(p) for p in val)
    elif ptype == 3:
        return max(eval(p) for p in val)
    elif ptype == 4:
        return val
    elif ptype == 5:
        v1 = eval(val[0])
        v2 = eval(val[1])
        return 1 if v1 > v2 else 0
    elif ptype == 6:
        v1 = eval(val[0])
        v2 = eval(val[1])
        return 1 if v1 < v2 else 0
    elif ptype == 7:
        v1 = eval(val[0])
        v2 = eval(val[1])
        return 1 if v1 == v2 else 0
print(eval(pkt))

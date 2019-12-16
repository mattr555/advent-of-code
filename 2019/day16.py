from common import *

print("WARNING: Run this with pypy or be sad :(")

BASEPATTERN = [0, 1, 0, -1]
data = list(map(int, filemap(lambda x: x, "day16.txt")[0]))

def flatmap(f, items):
    return itertools.chain.from_iterable(map(f, items))

def runPhase(l):
    ret = []
    for position in range(len(l)):
        thisPattern = itertools.cycle(flatmap(lambda i: itertools.repeat(i, position+1), BASEPATTERN))
        next(thisPattern)
        ans = 0
        for i in l:
            ans += i * next(thisPattern)
        ret.append(abs(ans) % 10)
    return ret

p1data = list(data)
for i in range(100):
    p1data = runPhase(p1data)
print(''.join(map(str, p1data[:8])))

def runPhase2(l):
    prefixes = []
    acc = 0
    for i in l:
        prefixes.append(acc)
        acc += i
    prefixes.append(acc)
    
    ret = []
    for position in range(len(l)):
        ans = 0
        sign = 1
        for offset in range(position, len(l), (position+1) * 2):
            ans += sign * (prefixes[min(position+offset+1, len(prefixes)-1)] - prefixes[offset])
            sign *= -1
        ret.append(abs(ans) % 10)
    return ret

offset = 0
for i in range(7):
    offset *= 10
    offset += data[i]

data *= 10000
for i in range(100):
    data = runPhase2(data)
    print('p2 loop', i)
print(''.join(map(str, data[offset:offset+8])))

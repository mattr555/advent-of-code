from common import *

def transform(x):
    return x.split('\n')

graphs, tests = filemap(transform, 'day05.txt', sep='\n\n')
graph = set()

for i in graphs:
    graph.add(tuple(map(int, i.split('|'))))

p1 = 0
p2 = 0
for i in tests:
    t = list(map(int, i.split(',')))
    good = True
    for a in range(len(t)):
        for b in range(a+1, len(t)):
            if (t[b],t[a]) in graph:
                good = False
                t[a],t[b] = t[b],t[a]
    if good:
        p1 += t[len(t)//2]
    else:
        p2 += t[len(t)//2]

print(p1)
print(p2)

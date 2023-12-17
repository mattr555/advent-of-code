from common import *

def transform(x):
    if '=' not in x:
        return x
    return x[0:3], x[7:10], x[12:15]

data = filemap(transform, 'day08.txt')

directions = data[0]
graph = {x[0]: (x[1], x[2]) for x in data[2:]}

def run(i, ends_with, loop=False, ii=0):
    ct = 0
    # print(i)
    while not i.endswith(ends_with):
        if directions[ii] == 'L':
            i = graph[i][0]
        else:
            i = graph[i][1]
        ii += 1
        ii %= len(directions)
        ct += 1
    # print(ct, i, graph[i], directions[ii])
    if loop:
        run(graph[i][0], ends_with, False, ii+1)
    return ct

print(run('AAA', 'ZZZ'))

p2s = []
for i in graph:
    if i.endswith('A'):
        p2s.append(run(i, 'Z', True))

p2 = 1
for i in p2s:
    p2 = lcm(p2, i)
print(p2)

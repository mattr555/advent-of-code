from common import *

data = filemap(lambda x: x.split(')'), "day6.txt")

graph = defaultdict(set)

for i in data:
    graph[i[0]].add(i[1])

q = deque([("COM", 0)])
s = 0
while len(q) > 0:
    this, depth = q.popleft()
    s += depth
    for i in graph[this]:
        q.append((i, depth+1))

print(s)

parents = {}
for i in data:
    parents[i[1]] = i[0]

def parent_chain(i):
    l = []
    while i != "COM":
        l.append(i)
        i = parents[i]
    return l

you = parent_chain("YOU")
you.reverse()
san = parent_chain("SAN")
san.reverse()

for ix, (i, j) in enumerate(zip(you, san)):
    if i != j:
        # print(ix)
        # -2 to discount myself and santa
        print(len(you) - ix + len(san) - ix - 2)
        break
from common import *

def parse(x):
    return tuple(x.split('-'))

data = filemap(parse, 'day12.txt')

graph = defaultdict(set)
for i, j in data:
    graph[i].add(j)
    graph[j].add(i)

def can_still_visit_twice(v):
    c = Counter(v)
    for i, ct in c.items():
        if i == i.lower() and ct > 1:
            return False
    return True

def traverse(graph, can_visit_one_twice=False):
    def go(current, visited):
        new_visit = visited + [current]
        ans = set()
        if current == 'end':
            return set([','.join(new_visit)])
        for i in graph[current]:
            if i == i.lower() and i in visited:
                if can_visit_one_twice and can_still_visit_twice(new_visit) and i != 'start':
                    pass
                else:
                    continue
            ans.update(go(i, new_visit))
        return ans
    return go('start', [])

print(len(traverse(graph)))
p2 = traverse(graph, True)
print(len(p2))
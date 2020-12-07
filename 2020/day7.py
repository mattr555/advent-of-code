from common import *

reg = re.compile(r'(\w+ \w+) bags contain ((?:\d+ \w+ \w+ bags?[,.] ?|no other bags)+)')
def parse(s):
    bag, contains = reg.match(s).groups()
    if 'no other bags' in contains:
        return bag, []
    return bag, [(int(x.split(' ')[0]), ' '.join(x.split(' ')[1:3])) for x in contains.split(', ')]

data = dict(filemap(parse, 'day7.txt'))

def crawl(x, visited, target):
    for i, j in data[x]:
        if j == target:
            return True
        if j not in visited:
            if crawl(j, visited, target):
                return True
            visited.add(j)
    return False

def dfsSum(x):
    s = 0
    for i, j in data[x]:
        s += i
        s += i * dfsSum(j)
    return s

p1 = 0
for key in data:
    if crawl(key, set(), 'shiny gold'):
        p1 += 1
print(p1)
print(dfsSum('shiny gold'))

from common import *

# note: had to modify the input to convert to Chomsky normal form
# in part 1, cases to change were 8 and 44

unit_productions = defaultdict(set)
def parseRule(s):
    n = int(s.split(':')[0])
    if s.endswith('"'):
        # unit production
        unit_productions[s[-2]].add(n)
        return ('dummy', 'asdf')
    l = [tuple(int(x) for x in y.split(' ')) for y in s.split(':')[1].strip().split(' | ')]
    return (n, l)

rules, tests = filemap(lambda x: x, 'day19-p2.txt', sep='\n\n')
rules = dict(map(parseRule, rules.split('\n')))
del rules['dummy']
tests = tests.split('\n')
total_rules = max(rules.keys()) + 1
print(rules)
print(tests)

def denseGrid(x, y, z, val=None):
    return [[[val] * z for _ in range(y)] for _ in range(x)]

# pseudocode yoinked from https://en.wikipedia.org/wiki/CYK_algorithm
def parse(st):
    cyk_grid = denseGrid(len(st)+1, len(st)+1, total_rules, val=False)
    for ix, ch in enumerate(st):
        for r_a in unit_productions[ch]:
            cyk_grid[1][ix+1][r_a] = True
    for l in range(2, len(st)+1):
        for s in range(1, len(st)-l+2):
            for p in range(1, l):
                for r_a, rule_set in rules.items():
                    for rule in rule_set:
                        if cyk_grid[p][s][rule[0]] and cyk_grid[l-p][s+p][rule[1]]:
                            cyk_grid[l][s][r_a] = True
    
    if cyk_grid[len(st)][1][0]:
        print(st, "good")
        return True
    print(st, "no good")
    return False

print(len(list(filter(parse, tests))))

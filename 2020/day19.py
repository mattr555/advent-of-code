from common import *

# note: had to manually modify the input to convert to Chomsky normal form
# in part 1, rules to change were 8 and 44
# in part 2, I had to further modify 8, as well as add a new rule for the ternary node in 11

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

# pseudocode yoinked from https://en.wikipedia.org/wiki/CYK_algorithm
# kept the 1-indexing from the pseudocode. that's why some of it is funky below
# using a set instead of a boolean array for the inner-most dimension
def parse(st):
    cyk_grid = [[set() for _ in range(len(st)+1)] for _ in range(len(st)+1)]
    for ix, ch in enumerate(st):
        for r_a in unit_productions[ch]:
            cyk_grid[1][ix+1].add(r_a)

    for l in range(2, len(st)+1):
        for s in range(1, len(st)-l+2):
            for p in range(1, l):
                for r_a, rule_set in rules.items():
                    for r_b, r_c in rule_set:
                        if r_b in cyk_grid[p][s] and r_c in cyk_grid[l-p][s+p]:
                            cyk_grid[l][s].add(r_a)

    if 0 in cyk_grid[len(st)][1]:
        print(st, "good")
        return True
    print(st, "no good")
    return False

print(len(list(filter(parse, tests))))

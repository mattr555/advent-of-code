from common import *

reg = re.compile(r'([\w ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
def parse_note(x):
    a, b, c, d, e = reg.match(x).groups()
    return (a, (int(b), int(c), int(d), int(e)))

with open('day16.txt') as f:
    notes, mine, nearby = f.read().strip().split('\n\n')
    notes = dict(map(parse_note, notes.split('\n')))
    mine = [int(x) for x in mine.split('\n')[1].split(',')]
    nearby = list(map(lambda x: [int(y) for y in x.split(',')], nearby.split('\n')[1:]))

valids = []
p1 = 0
for ticket in nearby:
    tick_valid = True
    for val in ticket:
        for a, b, c, d in notes.values():
            if (a <= val <= b or c <= val <= d):
                break
        else:
            p1 += val
            tick_valid = False
    if tick_valid:
        valids.append(ticket) 
print(p1)

possibles = {rule_name: set(range(len(valids[0]))) for rule_name in notes.keys()}
for ticket in valids:
    for field_ix, val in enumerate(ticket):
        for rule_name, (a, b, c, d) in notes.items():
            if not (a <= val <= b or c <= val <= d):
                possibles[rule_name].discard(field_ix)

assignment = {}
while len(assignment) != len(notes):
    for rule_name, rule_set in possibles.items():
        if len(rule_set) == 1:
            asst = rule_set.pop()
            assignment[rule_name] = asst
            for other_set in possibles.values():
                other_set.discard(asst)

p2 = 1
for k, v in assignment.items():
    if k.startswith('departure'):
        p2 *= mine[v]
print(p2)

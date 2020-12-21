from common import *

reg = re.compile(r'([\w ]+) \(contains ([\w, ]+)\)')
def parse(s):
    ingredients, allergies = reg.match(s).groups()
    return set(ingredients.split(' ')), set(allergies.split(', '))

data = filemap(parse, 'day21.txt')

all_ingredients = set().union(*map(getitem(0), data))
all_allergens = set().union(*map(getitem(1), data))

m = {x: all_ingredients.copy() for x in all_allergens}
for i, j in data:
    for allergy in j:
        m[allergy] &= i

non_potential_allergens = all_ingredients - set().union(*m.values())

p1 = 0
for i, _ in data:
    p1 += len(i & non_potential_allergens)
print(p1)

real_map = {}
while len(real_map) < len(m):
    for i, j in m.items():
        if len(j) == 1:
            identified = j.pop()
            real_map[i] = identified
            for k in m.values():
                k.discard(identified)
print(','.join(real_map[x] for x in sorted(real_map.keys())))

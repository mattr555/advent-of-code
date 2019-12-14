from common import *

def m(l):
    ret = []
    inp = l.replace(',', '').replace('=> ', '').strip().split(' ')
    for i in range(0, len(inp), 2):
        ret.append((int(inp[i]), inp[i+1]))
    return ret

data = filemap(m, "day14.txt")

# print(data)
# print(len(set(i[-1] for i in data)))
# only one way to make each thing

table = {}
for i in data:
    table[i[-1][1]] = (i[-1][0], i[:-1])

def make(chem, required):
    recipe_amt, ingredients = table[chem]
    to_make = int(math.ceil(required[chem]/recipe_amt))
    ret = []
    for ing_amt, ing in ingredients:
        ret.append((to_make * ing_amt, ing))
    return to_make * recipe_amt, ret

def test(n):
    required = defaultdict(int)
    required['FUEL'] = n
    q = set(['FUEL'])
    while len(q) > 0:
        chem = q.pop()
        if chem == 'ORE' or required[chem] <= 0:
            continue

        i_need = required[chem]
        total_made, new_requires = make(chem, required)
        for a, i in new_requires:
            q.add(i)
            required[i] += a
        required[chem] = i_need - total_made
    return required['ORE']


print(test(1))

lo = 1
hi = 10000000
while lo < hi:
    t = (lo + hi) // 2
    res = test(t)
    if res <= 1000000000000:
        lo = t+1
    else:
        hi = t-1

print(hi)

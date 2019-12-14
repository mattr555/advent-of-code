from common import *
import math

def m(l):
    ret = []
    for ix, i in enumerate(l.replace(',', '').replace('=> ', '').strip().split(' ')):
        if ix % 2 == 0:
            ret.append(int(i))
        else:
            ret.append(i)
    return ret

data = filemap(m, "day14.txt")

# print(data)
# print(len(set(i[-1] for i in data)))
# only one way to make each thing

table = {}

for i in data:
    table[i[-1]] = (i[-2], i[:-2])

def make(chem, required):
    recipe_amt, ingredients = table[chem]
    to_make = int(math.ceil(required[chem]/recipe_amt))
    ret = []
    for i in range(0, len(ingredients), 2):
        ret.append((to_make * ingredients[i], ingredients[i+1]))
    return to_make * recipe_amt, ret

def test(n):
    required = defaultdict(int)
    required['FUEL'] = n
    q = deque(['FUEL'])
    while any(i != 'ORE' for i in q):
        chem = q.popleft()
        if chem == 'ORE':
            pass
        elif required[chem] <= 0:
            pass
        else:
            i_need = required[chem]
            total_made, new_requires = make(chem, required)
            for a, i in new_requires:
                q.append(i)
                required[i] += a
            required[chem] = i_need - total_made
    return required['ORE']


print(test(1))

min_ = 1
max_ = 1000000000
while min_ < max_:
    t = (min_ + max_) // 2
    res = test(t)
    if res <= 1000000000000:
        min_ = t+1
    else:
        max_ = t-1

print(max_)


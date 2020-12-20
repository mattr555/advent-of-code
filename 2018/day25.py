data = []
with open('day25.txt') as f:
    for l in f:
        data.append(list(map(int, l.split(','))))
print(data)

sets = {i: set([i]) for i in range(len(data))}
leaders = list(range(len(data)))

def distance(x, y):
    return sum(map(lambda i: abs(i[0] - i[1]), zip(x, y)))

import itertools
for i, j in itertools.combinations(range(len(data)), 2):
    if distance(data[i], data[j]) <= 3:
        # union
        if leaders[i] != leaders[j]:
            new_leader = min(leaders[i], leaders[j])
            old_leader = max(leaders[i], leaders[j])
            for x in sets[old_leader]:
                leaders[x] = new_leader
            sets[new_leader] |= sets[old_leader]
            del sets[old_leader]
print(len(sets))


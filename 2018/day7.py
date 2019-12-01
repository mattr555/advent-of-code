all_steps = set()
data = []
with open("day7.txt") as f:
    for ss in f:
        s = ss.strip()
        data.append((s[5], s[-12]))
        all_steps.add(s[5])
        all_steps.add(s[-12])

from collections import defaultdict
from copy import deepcopy
mapping = defaultdict(set)

for (s, e) in data:
    mapping[e].add(s)
mapping2 = deepcopy(mapping)

to_search = list(sorted(all_steps - set(mapping.keys())))
to_search2 = deepcopy(to_search)

ans = []
while to_search:
    about_to_happen = to_search.pop(0)
    for i in list(mapping.keys()):
        mapping[i].discard(about_to_happen)
        if len(mapping[i]) == 0:
            to_search.append(i)
            del mapping[i]
    ans.append(about_to_happen)
    to_search.sort()

print(''.join(ans))


workers = [None] * 5
offset = 60
mapping = mapping2
to_search = to_search2
t = 0

while len(mapping) > 0 or not all(x is None for x in workers):
    for ind in range(len(workers)):
        i = workers[ind]
        if i is not None:
            i[1] -= 1
            if i[1] == 0:
                for j in list(mapping.keys()):
                    mapping[j].discard(i[0])
                    if len(mapping[j]) == 0:
                        to_search.append(j)
                        del mapping[j]
                to_search.sort()
                workers[ind] = None
    
    t += 1

    while to_search and None in workers:
        to_work = to_search.pop(0)
        ind = workers.index(None)
        workers[ind] = [to_work, offset + ord(to_work) - ord('A') + 1]

print(t-1)

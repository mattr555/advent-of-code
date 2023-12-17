from common import *

data = filemap(str, 'day07.txt')

curpath = []
tree = {'/': {}}
ix = 0
used_space = 0
while ix < len(data):
    i = data[ix]
    if i.startswith('$ cd'):
        if i == '$ cd ..':
            curpath.pop()
            ix += 1
        else:
            curpath.append(i.split(' ')[2])
            ix += 1
    elif i == '$ ls':
        ix += 1
        while ix < len(data) and not data[ix].startswith('$'):
            t, n = data[ix].split(' ')
            if t == 'dir':
                t = {}
            else:
                t = int(t)
                used_space += t
            dxtree = tree
            for dx in curpath:
                dxtree = dxtree[dx]
            dxtree[n] = t
            ix += 1
    else:
        assert False

total = 0
to_delete = inf
def dir_size(d):
    global total, to_delete
    s = 0
    for _, t in d.items():
        if type(t) is int:
            s += t
        else:
            s += dir_size(t)
    if s <= 100000:
        total += s
    if 70000000 - (used_space - s) >= 30000000:
        to_delete = min(to_delete, s)
    return s

dir_size(tree['/'])
print(total)
print(to_delete)

from common import *
from tqdm import tqdm

mod = 1

class Monkey(object):
    def __init__(self, items, inspect, throw):
        self.items = items
        self.inspect = inspect
        self.throw = throw
        self.inspection_count = 0

def transform(x):
    global mod
    lines = x.split('\n')
    starting_items = list(map(int, lines[1].strip('  Starting items: ').split(', ')))
    ops = lines[2].strip().split(' ')
    def op(old):
        if ops[5].isdigit():
            n = int(ops[5])
        else:
            assert ops[5] == "old"
            n = old
        if ops[4] == '+':
            return old + n
        else:
            assert ops[4] == "*"
            return old * n

    div = int(lines[3].strip().split(' ')[3])
    mod *= div
    t = int(lines[4].strip().split(' ')[5])
    f = int(lines[5].strip().split(' ')[5])
    def throw(n):
        return t if n % div == 0 else f

    return Monkey(starting_items, op, throw)


data = filemap(transform, 'day11.txt', '\n\n')
data2 = deepcopy(data)

for turn in range(20):
    for monkey in data:
        while monkey.items:
            monkey.inspection_count += 1
            n = monkey.items.pop(0)
            n = monkey.inspect(n) // 3
            new = monkey.throw(n)
            data[new].items.append(n)

data.sort(key=lambda m: m.inspection_count, reverse=True)
print(data[0].inspection_count * data[1].inspection_count)

for turn in range(10000):
    for monkey in data2:
        while monkey.items:
            monkey.inspection_count += 1
            n = monkey.items.pop(0)
            n = monkey.inspect(n)
            n = n % mod
            new = monkey.throw(n)
            data2[new].items.append(n)

data2.sort(key=lambda m: m.inspection_count, reverse=True)
print(data2[0].inspection_count * data2[1].inspection_count)
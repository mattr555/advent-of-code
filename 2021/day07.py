from common import *

def parse(x):
    return int(x)

data = filemap(parse, 'day07.txt', ',')

def test_alignment_p1(a):
    return sum(abs(x-a) for x in data)

def test_alignment_p2(a):
    return sum((abs(x-a)*(abs(x-a)+1))/2 for x in data)

for func in (test_alignment_p1, test_alignment_p2):
    ans = inf
    for i in range(min(data), max(data)):
        ans = min(ans, func(i))
    print(int(ans))

from common import *

def transform(x):
    return x

data = filemap(transform, 'day03.txt')

p1 = 0
p2 = 0
enabled = True
for l in data:
    for do, dont, a, b in re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)', l):
        if a:
            p1 += int(a) * int(b)
            if enabled:
                p2 += int(a) * int(b)
        elif do:
            enabled = True
        elif dont:
            enabled = False
        else:
            assert False
print(p1)
print(p2)

from common import *

data = filemap(lambda x: x, 'day6.txt', sep='\n\n')

p1 = 0
p2 = 0
for group in data:
    s = set(group)
    s = s - set('\n')
    p1 += len(s)
    all = set(s)
    for line in group.split('\n'):
        s -= all - set(line)
    p2 += len(s)

print(p1)
print(p2)

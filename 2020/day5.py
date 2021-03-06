from common import *

def parse(s):
    i = s.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    return int(i, 2)

data = filemap(parse, 'day5.txt')

print(max(data))

for i, j in zip(sorted(data), range(min(data), max(data))):
    if i != j:
        print(j)
        break

from common import *

def parse(s):
    i = s.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    return int(i, 2)

data = filemap(parse, 'day5.txt')

print(max(data))

lasti = list(sorted(data))[0] - 1
for i in sorted(data):
    if lasti == i - 1:
        pass
    else:
        print(i - 1)
    lasti = i

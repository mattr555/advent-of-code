from common import *

def group(x):
    return [int(i) for i in x.split('\n')]
data = filemap(group, 'day01.txt', '\n\n')

print(max(map(sum, data)))

sums = list(map(sum, data))
sums.sort(reverse=True)
print(sum(sums[:3]))


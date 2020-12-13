from common import *

data = filemap(lambda x: x, 'day13.txt')
time = int(data[0])
buses = data[1].split(',')

best = (inf, 0)
for i in buses:
    if i == 'x':
        continue
    x = int(i) - (time % int(i))
    best = min(best, (x, int(i)))
print(best[0] * best[1])

# find the first i st
#  i % 7 == 0
#  i % 13 == 12
#  i % 59 == 55
#  i % 31 == 25
#  i % 19 == 12
# chinese remainder theorem FTW

values = []
for a, n in enumerate(buses):
    if n == 'x':
        continue
    values.append(((int(n) - a) % int(n), int(n)))

v = values[0][0] # actual value
n = values[0][1] # increase amt
i = 1 # correct so far
while i < len(values):
    if v % values[i][1] == values[i][0]:
        n *= values[i][1]
        i += 1
    else:
        v += n
print(v)

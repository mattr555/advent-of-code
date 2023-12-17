from common import *

def transform(x):
    return list(map(int, re.findall('\d+', x)))

data = transpose(filemap(transform, 'day06.txt'))

p1 = 1
p2 = 0

for time, distance in data:
    n = 0
    for speed in range(time+1):
        if speed * (time - speed) > distance:
            n += 1
    p1 *= n
print(p1)


def transform(x):
    return list(map(int, re.findall('\d+', x.replace(' ', ''))))

data = transpose(filemap(transform, 'day06.txt'))

time, distance = data[0]
for speed in range(time+1):
    if speed * (time - speed) > distance:
        p2 += 1
print(p2)

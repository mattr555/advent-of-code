from common import *

data = filemap(int, 'day1.txt')
TARGET = 2020

#part 1
s = set()
for i in data:
    if i in s:
        print(i * (TARGET - i))
    else:
        s.add(TARGET - i)

#part 2
s = set(data)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        k = (TARGET - data[i] - data[j])
        if k in s:
            print(data[i] * data[j] * k)
            break
    else:
        continue
    break

from common import *

data = filemap(int, 'day9.txt')

for i in range(25, len(data)):
    target = data[i]
    arr = data[i-25:i]
    s = set(arr)
    for i in arr:
        if target - i in s:
            break
    else:
        print(target)
        p1 = target
        break

for i in range(len(data)):
    s = data[i]
    for j in range(i+1, len(data)):
        s += data[j]
        if s == p1:
            print(min(data[i:j+1]) + max(data[i:j+1]))
        elif s > p1:
            break

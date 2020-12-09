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

start = 0
end = 2
s = data[start] + data[end-1]
while s != p1:
    if s < p1:
        s += data[end]
        end += 1
    else:
        s -= data[start]
        start += 1
print(min(data[start:end]) + max(data[start:end]))

from common import *

data = filemap(int, 'day01.txt')

ct = 0
for i, j in zip(data, data[1:]):
    if i < j:
        ct += 1
print(ct)

windows = []
for i, j, k in zip(data, data[1:], data[2:]):
    windows.append(i+j+k)
p2 = 0
for i, j in zip(windows, windows[1:]):
    if i < j:
        p2 += 1
print(p2)

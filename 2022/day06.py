from common import *

def transform(x):
    return x

data = filemap(transform, 'day06.txt')[0]

for l in (4, 14):
    for i in range(len(data)):
        if len(set(data[i:i+l])) == l:
            print(i+l)
            break

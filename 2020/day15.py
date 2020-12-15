from common import *

data = [1,17,0,10,18,11,6]
TARGET1 = 2020
TARGET2 = 30_000_000

def build_hash(data):
    ret = {}
    for ix, i in enumerate(data[:-1]):
        ret[i] = ix+1
    return ret

hash = build_hash(data)
last_spoken = data[-1]

for i in range(len(data), TARGET2):
    if i == TARGET1:
        print(last_spoken)
    if last_spoken in hash:
        next_to_speak = i - hash[last_spoken]
    else:
        next_to_speak = 0
    hash[last_spoken] = i
    last_spoken = next_to_speak
print(last_spoken)

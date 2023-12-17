from common import *

def hash(x):
    n = 0
    for i in x:
        n += ord(i)
        n *= 17
        n %= 256
    return n

def transform(x):
    return x.split(',')

data = filemap(transform, 'day15.txt')[0]

print(sum(map(hash, data)))

boxes = [[] for x in range(256)]

for step in data:
    if '=' in step:
        label = step[:-2]
    else:
        label = step[:-1]

    box_to_op = hash(label)
    to_modify = None
    for ix, i in enumerate(boxes[box_to_op]):
        if i[0] == label:
            to_modify = ix
    if '=' in step:
        if to_modify is not None:
            boxes[box_to_op][to_modify] = (label, int(step[-1]))
        else:
            boxes[box_to_op].append((label, int(step[-1])))
    else:
        if to_modify is not None:
            boxes[box_to_op] = boxes[box_to_op][:to_modify] + boxes[box_to_op][to_modify+1:]

p2 = 0
for box_ix, box in enumerate(boxes):
    for lens_ix, lens in enumerate(box):
        p2 += (box_ix+1) * (lens_ix+1) * lens[1]
print(p2)



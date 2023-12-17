from common import *

with open('day05.txt') as f:
    lines = f.readlines()
    box_d = lines[:8]
    move_d = lines[10:]

box_d.reverse()
boxes = [[] for x in range(9)]
for row in box_d:
    for ix, column in enumerate(range(1, 34, 4)):
        if row[column] != ' ':
            boxes[ix].append(row[column])

boxes2 = deepcopy(boxes)

for move in move_d:
    to_move, f, t = map(int, re.match(r'move (\d+) from (\d+) to (\d+)', move).groups())
    for _ in range(to_move):
        c = boxes[f-1].pop()
        boxes[t-1].append(c)
    
    boxes2[t-1] += boxes2[f-1][-to_move:]
    for _ in range(to_move):
        boxes2[f-1].pop()

for i in boxes:
    print(i[-1], end='')
print()

for i in boxes2:
    print(i[-1], end='')
print()

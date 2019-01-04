import re
line_re = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')

def processLine(l):
    match = line_re.match(l)
    return tuple(map(int, match.group(1, 2, 3, 4)))

with open("day23.txt") as f:
    data = list(map(processLine, f.read().strip().split("\n")))

strongest = max(data, key=lambda x: x[3])

def isInRange(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) <= a[3]

print(len(list(filter(lambda i: isInRange(strongest, i), data))))

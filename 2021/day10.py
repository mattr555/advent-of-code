from common import *

def parse(x):
    return x

data = filemap(parse, 'day10.txt')
print(data)

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

p1 = 0
p2 = []
for line in data:
    s = deque()
    for i in line:
        if i in '([<{':
            s.append(')]>}'['([<{'.index(i)])
        elif i == s[-1]:
            s.pop()
        else:
            p1 += scores[i]
            break
    else:
        end_score = 0
        while s:
            end_score *= 5
            end_score += {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
            }[s.pop()]
        p2.append(end_score)
print(p1)
p2.sort()
print(p2[math.floor(len(p2)/2)])

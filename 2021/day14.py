from common import *

def parse(x):
    return x

data = filemap(parse, 'day14.txt')
s = list(data[0])
digraphs = defaultdict(int)
for ix in range(len(s) - 1):
    digraphs[s[ix] + s[ix+1]] += 1
rules = dict(map(lambda x: tuple(x.split(' -> ')), data[2:]))

def calculate_score(digraphs):
    letters = defaultdict(int)
    for di, ct in digraphs.items():
        letters[di[0]] += ct
        letters[di[1]] += ct
    letters[s[0]] += 1
    letters[s[-1]] += 1

    ct = list(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    return ct[0][1]//2 - ct[-1][1]//2

for step in range(40):
    new_digraphs = defaultdict(int)
    for di, ct in digraphs.items():
        insert = rules[di]
        new_digraphs[di[0] + insert] += ct
        new_digraphs[insert + di[1]] += ct
    digraphs = new_digraphs
    if step == 9:
        print(calculate_score(digraphs))
print(calculate_score(digraphs))

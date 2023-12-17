from common import *

def transform(x):
    y, i_have = x.split(' | ')
    _, winning = y.split(': ')
    return set(map(int, re.findall(r'\d+', winning))), set(map(int, re.findall(r'\d+', i_have)))

data = filemap(transform, 'day04.txt')

p1 = 0

cards = [1] * len(data)

for ix, (winning, i_have) in enumerate(data):
    n = len(winning & i_have)
    if n > 0:
        p1 += 2 ** (n-1)
        for i in range(ix+1, ix+n+1):
            cards[i] += cards[ix]

print(p1)
print(sum(cards))

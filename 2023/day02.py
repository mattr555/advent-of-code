from common import *

reg = re.compile(r"Game (\d+): (.*)")
def transform(x):
    id, game = reg.match(x).groups()
    y = {'id': int(id), 'hands': []}
    for hand in game.split('; '):
        z = []
        for bag in hand.split(', '):
            a, b = bag.split(' ')
            z.append((int(a), b))
        y['hands'].append(z)
    return y

data = filemap(transform, 'day02.txt')

p1 = 0
p2 = 0
for game in data:
    mred, mblue, mgreen = 0, 0, 0
    for hand in game['hands']:
        for n, color in hand:
            if color == 'red':
                mred = max(mred, n)
            if color == 'green':
                mgreen = max(mgreen, n)
            if color == 'blue':
                mblue = max(mblue, n)
    if mred <= 12 and mgreen <= 13 and mblue <= 14:
        p1 += game['id']
    p2 += mred * mgreen * mblue
print(p1)
print(p2)
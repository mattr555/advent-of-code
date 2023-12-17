from common import *

def parse(x):
    return int(x.split(' ')[-1])

data = filemap(parse, 'day21.txt')

d = 1
rolls = 0
p1 = data[0]
p2 = data[1]
scores = [0, 0]
done = False
while not done:
    for player in range(2):
        for i in range(3):
            data[player] += d
            data[player] = ((data[player] - 1) % 10) + 1
            d += 1
            d = ((d - 1) % 100) + 1
            rolls += 1
        scores[player] += data[player]
        if max(scores) >= 1000:
            print(rolls * min(scores))
            done = True
            break

sums = defaultdict(int)
for a, b, c in itertools.product(range(1, 4), range(1, 4), range(1, 4)):
    sums[a+b+c] += 1

# p1score, p2score, p1pos, p2pos
states = {(0, 0, p1, p2): 1}
wins = [0, 0]
turn = 0
while states:
    new_states = defaultdict(int)
    for state, count in states.items():
        for dice_sum, mult in sums.items():
            new_st = list(state)
            new_st[turn+2] += dice_sum
            new_st[turn+2] = ((new_st[turn+2] - 1) % 10) + 1
            new_st[turn] += new_st[turn+2]
            if new_st[turn] >= 21:
                wins[turn] += count * mult
            else:
                new_states[tuple(new_st)] += count * mult
    states = new_states
    turn = (turn + 1) % 2
print(max(wins))

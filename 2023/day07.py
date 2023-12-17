from common import *

def transform(x):
    hand, bid = x.split(' ')
    return hand, int(bid)

data = filemap(transform, 'day07.txt')

p1 = 0
p2 = 0

ranks = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

def hand_value_p1(i):
    hand, bid = i

    c = Counter(hand)
    if c.most_common()[0][1] == 5:
        card_type = 0
    elif c.most_common()[0][1] == 4:
        card_type = 1
    elif c.most_common()[0][1] == 3:
        # full house?
        if c.most_common()[1][1] == 2:
            card_type = 2
        else:
            card_type = 3
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        card_type = 4
    elif c.most_common()[0][1] == 2:
        card_type = 5
    else:
        card_type = 6

    return (card_type, *[ranks.index(x) for x in hand])

for ix, (hand, bid) in enumerate(sorted(data, key=hand_value_p1, reverse=True)):
    p1 += (ix+1) * bid
print(p1)


ranks_p2 = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
def hand_value_p2(i):
    hand, bid = i

    c = Counter(hand)
    jokers = c.get("J", 0)
    c["J"] = 0
    if c.most_common()[0][1] + jokers == 5:
        card_type = 0
    elif c.most_common()[0][1] + jokers == 4:
        card_type = 1
    elif c.most_common()[0][1] + jokers == 3:
        # full house?
        if c.most_common()[1][1] == 2:
            card_type = 2
        else:
            card_type = 3
    elif c.most_common()[0][1] + jokers == 2 and c.most_common()[1][1] == 2:
        card_type = 4
    elif c.most_common()[0][1] + jokers == 2:
        card_type = 5
    else:
        card_type = 6

    return (card_type, *[ranks_p2.index(x) for x in hand])

for ix, (hand, bid) in enumerate(sorted(data, key=hand_value_p2, reverse=True)):
    p2 += (ix+1) * bid
print(p2)
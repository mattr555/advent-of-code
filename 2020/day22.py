from common import *

def parse(s):
    l = s.split('\n')[1:]
    return deque(map(int, l))

p1, p2 = filemap(parse, 'day22.txt', sep='\n\n')
p1_start = deque(p1)
p2_start = deque(p2)

while len(p1) > 0 and len(p2) > 0:
    a = p1.popleft()
    b = p2.popleft()
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

if len(p1) > 0:
    p = p1
else:
    p = p2

def score(p):
    ans = 0
    for ix, i in enumerate(p):
        ans += (len(p) - ix) * i
    print(ans)
score(p)


def playGame(p1, p2):
    seen_states = set()
    while len(p1) > 0 and len(p2) > 0:
        st = (str(list(p1)), str(list(p2)))
        if st in seen_states:
            return 1 # for player 1
        seen_states.add(st)
        a = p1.popleft()
        b = p2.popleft()
        if a <= len(p1) and b <= len(p2):
            new_p1 = deque(list(p1)[:a])
            new_p2 = deque(list(p2)[:b])
            winner = playGame(new_p1, new_p2)
        elif a > b:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    if len(p1) > 0:
        return 1
    else:
        return 2


winner = playGame(p1_start, p2_start)
if winner == 1:
    score(p1_start)
else:
    score(p2_start)

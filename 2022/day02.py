from common import *

def d(x):
    a, b = x.split(' ')
    return ord(a) - ord('A'), ord(b) - ord('X')

data = filemap(d, 'day02.txt')

score = 0
for a, b in data:
    if a == b:
        score += 3
    elif a == (b-1) % 3:
        score += 6
    
    score += b + 1
print(score)

score = 0
for a, b in data:
    my_choice = 0
    if b == 0:
        my_choice = (a - 1) % 3
    elif b == 1:
        my_choice = a
        score += 3
    elif b == 2:
        my_choice = (a + 1) % 3
        score += 6
    score += my_choice + 1
print(score)


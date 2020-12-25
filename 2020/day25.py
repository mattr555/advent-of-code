from common import *

card_public = 9033205
door_public = 9281649

l = 0
subject = 7
v = 1
card_loop = 0
door_loop = 0
while card_loop == 0 or door_loop == 0:
    v = v * subject
    v %= 20201227
    l += 1
    if v == card_public:
        card_loop = l
    if v == door_public:
        door_loop = l

v = 1
for i in range(card_loop):
    v = v * door_public
    v %= 20201227 
print(v)


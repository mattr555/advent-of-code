from common import *

data = filemap(lambda x: tuple(x.split(' ')), 'day02.txt')

x = 0
depth_p1 = 0
depth_p2 = 0
aim = 0
for dir, n in data:
    n = int(n)
    if dir == 'forward':
        x += n
        depth_p2 += aim * n
    elif dir == 'up':
        depth_p1 -= n
        aim -= n
    elif dir == 'down':
        depth_p1 += n
        aim += n
print(x * depth_p1)
print(x * depth_p2)

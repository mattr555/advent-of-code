from common import *

def transform(x):
    return x

data = filemap(transform, 'day01.txt')

p1=0
for i in data:
    ans = ''
    for j in i:
        if j.isdigit():
            ans += j
    p1 += 10*int(ans[0]) + int(ans[-1])
print(p1)

m = ['one','two','three','four','five','six','seven','eight','nine']

def num(x):
    if x.isdigit():
        return int(x)
    return m.index(x) + 1

p2 = 0
reg = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|\d)')
for i in data:
    matches = reg.findall(i)
    p2 += 10*num(matches[0]) + num(matches[-1])
print(p2)

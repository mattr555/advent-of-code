from common import *

def parse(s):
    reg = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
    a, b, c, d = reg.match(s).groups()
    a = int(a)
    b = int(b)
    return a, b, c, d

data = filemap(parse, 'day2.txt')

ct = 0
for lo, hi, ch, pw in data:
    c = pw.count(ch)
    if lo <= c <= hi:
        ct += 1
print(ct)

ct = 0
for pos1, pos2, ch, pw in data:
    if (pw[pos1-1] == ch) ^ (pw[pos2-1] == ch):
        ct += 1
print(ct)

from common import *
from operator import neg

def parse(x):
    l = x.split('\n')
    scanner = int(re.match(r'--- scanner (\d+) ---', l[0]).group(1))
    points = [tuple(map(int, y.split(','))) for y in l[1:]]
    return scanner, points

data = filemap(parse, 'day19.txt', sep='\n\n')

def fixed_axis_for_point(p):
    target = tuple(sorted(map(abs, p)))
    assert 0 < target[0] < target[1] < target[2] # no equality
    ret = []
    x, y, z = p
    for i in target:
        if i == abs(x):
            ret.append((0, sign(x)))
        elif i == abs(y):
            ret.append((1, sign(y)))
        elif i == abs(z):
            ret.append((2, sign(z)))
    return ret

def remap_axis(ax):
    def go(p):
        ret = []
        for a, sgn in ax:
            ret.append(sgn * p[a])
        return tuple(ret)
    return go

def translate(t):
    def go(p):
        return tuple(map(sum, zip(p, t)))
    return go

def canonicalize_on_point(points, pt):
    zeroes = tuple(map(neg, points[pt]))
    sort_key = lambda x: sum(abs(y) for y in x)
    anchored = list(sorted(
        map(translate(zeroes), points),
        key=sort_key))
    assert sort_key(anchored[1]) < sort_key(anchored[2])
    axis = fixed_axis_for_point(anchored[1])
    return set(map(remap_axis(axis), anchored)), axis

matches = defaultdict(dict)

for scanner_a, beacon_a in data:
    for scanner_b, beacon_b in data[scanner_a+1:]:
        if scanner_b in matches[scanner_a]:
            continue
        for pt_a in range(len(beacon_a)):
            for pt_b in range(len(beacon_b)):
                try:
                    s_a, ax_a = canonicalize_on_point(beacon_a, pt_a)
                    s_b, ax_b = canonicalize_on_point(beacon_b, pt_b)
                    l = len(s_a & s_b)
                    if l >= 12:
                        matches[scanner_a][scanner_b] = (pt_a, ax_a, pt_b, ax_b)
                        # print(f'got one! {scanner_a}[{pt_a}] -> {scanner_b}[{pt_b}] ({l} points)')
                except AssertionError:
                    pass
print(matches)

from common import *

data = filemap(lambda x: x, 'day03.txt')

def count_bits(data):
    counts = [0] * len(data[0])
    for n in data:
        for ix, i in enumerate(n):
            if i == '1':
                counts[ix] += 1
    return counts

gamma = ''
epsilon = ''
for i in count_bits(data):
    if i > len(data) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))

def narrow_down(l, most):
    def go(l, ix):
        if len(l) == 1:
            return l[0]
        bits = count_bits(l)
        one_is_most_common = bits[ix] >= len(l) / 2
        correct_bit = '0' if one_is_most_common ^ most else '1'
        return go(list(filter(lambda x: x[ix] == correct_bit, l)), ix + 1)
    return int(go(l, 0), 2)

print(narrow_down(data, True) * narrow_down(data, False))

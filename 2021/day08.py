from common import *

def parse(x):
    signals, output = x.split(' | ')
    return (signals.split(' '), output.split(' '))

data = filemap(parse, 'day08.txt')

real_values = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
helpful = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

def remap(fake, mapping):
    new = ''
    for i in fake:
        new += 'abcdefg'[mapping.index(i)]
    new = ''.join(sorted(new))
    if new in real_values:
        return real_values.index(new)
    return None

p1 = 0
p2 = 0
for signals, output in data:
    possible_mappings = {
        x: set('abcdefg') for x in 'abcdefg'
    }
    for i in output:
        if len(i) in helpful:
            p1 += 1
    for i in signals + output:
        if len(i) in helpful:
            for fake in i:
                possible_mappings[fake] &= set(real_values[helpful[len(i)]])

    # by this analysis, "f" and "c" are linked
    real_mapping = {}
    exclude = set('fc')
    for i in possible_mappings:
        if possible_mappings[i] - exclude:
            possible_mappings[i] -= exclude
    
    # next we figure out "a", "b" and "d"
    exclude = exclude.union(set('abd'))
    for i in possible_mappings:
        if possible_mappings[i] - exclude:
            possible_mappings[i] -= exclude
    
    # finally for each pair of real db, ge, fc we try the possible combinations.
    # 2^3 == 8
    pairs_to_retrieve = ['db', 'ge', 'fc']
    pairs = ['', '', '']
    single_a = ''
    for fake, s in possible_mappings.items():
        if len(s) == 2:
            for ix, i in enumerate(pairs_to_retrieve):
                if set(i) == s:
                    pairs[ix] += fake
        else:
            single_a = fake

    for db_ix, ge_ix, fc_ix in itertools.product(range(2), range(2), range(2)):
        mapping = single_a + pairs[0][db_ix] + pairs[2][fc_ix] + pairs[0][db_ix-1] + \
            pairs[1][ge_ix] + pairs[2][fc_ix-1] + pairs[1][ge_ix-1]
        if all(remap(x, mapping) is not None for x in signals + output):
            # we found one!
            out_digits = [remap(x, mapping) for x in output]
            acc = 0
            for i in out_digits:
                acc *= 10
                acc += i
            p2 += acc

print(p1)
print(p2)

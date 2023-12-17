from common import *

def transform(x):
    if x.startswith('seeds: '):
        return list(map(int, x.split(' ')[1:]))
    return [list(map(int, y.split(' '))) for y in x.split('\n')[1:]]

data = filemap(transform, 'day05.txt', sep='\n\n')

p1 = inf
p2 = inf
seeds = data[0]
transformers = data[1:]

def do_it(seed):
    n = seed
    for ranges in transformers:
        for dst_start, src_start, range_len in ranges:
            if src_start <= n < src_start + range_len:
                n = dst_start + (n - src_start)
                break
    return n

for seed in seeds:
    p1 = min(p1, do_it(seed))
print(p1)

def transform_interval(interval, range):
    #return: mapped, not_mapped

    my_start, my_end = interval
    dst_start, src_start, range_len = range
    src_end = src_start + range_len
    
    def transform(x):
        return dst_start + x - src_start

    if src_start <= my_start < src_end:
        # at least the front part of this will be transformed
        if my_end <= src_end:
            # all of it will be transformed
            return [(transform(my_start), transform(my_end))], []
        else:
            # left mapped, right unmapped
            return [(transform(my_start), transform(src_end))], [(src_end, my_end)]
    if my_start < src_start and src_start < my_end:
        # at least some part after the start will be transformed
        if my_end <= src_end:
            # left unmapped, right mapped
            return [(transform(src_start), transform(my_end))], [(my_start, src_start)]
        else:
            # left unmapped, middle mapped, right unmapped
            return [(transform(src_start), transform(src_end))], [(my_start, src_start), (src_end, my_end)]
    # no intersection, no transformation
    return [], [(my_start, my_end)]


for start, l in chunk(seeds, 2):
    intervals = [(start, start+l)]
    for ranges in transformers:
        unmapped = intervals
        mapped = []
        for range in ranges:
            new_unmapped = []
            for i in unmapped:
                m, um = transform_interval(i, range)
                mapped += m
                new_unmapped += um
            unmapped = new_unmapped
        intervals = unmapped + mapped
    p2 = min(p2, min(intervals)[0])
print(p2)
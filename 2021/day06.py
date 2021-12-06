from common import *

def parse(x):
    return int(x)

data = filemap(parse, 'day06.txt', ',')
counts = Counter(data)
for i in range(256):
    new_counts = defaultdict(int)
    for days, fish in sorted(counts.items()):
        if days == 0:
            new_counts[6] += fish
            new_counts[8] += fish
        else:
            new_counts[days-1] += fish
    counts = new_counts
    if i == 79:
        print(sum(counts.values()))

print(sum(counts.values()))

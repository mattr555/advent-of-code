with open("day1.txt") as f:
    data = list(map(int, f.read().strip().split('\n')))

print(sum(data))

current = 0
all_freqs = set([0])
done = False
while not done:
    for i in data:
        current += i
        if current in all_freqs:
            print(current)
            done = True
            break
        all_freqs.add(current)
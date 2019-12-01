from collections import Counter

with open("day2.txt") as f:
    data = f.read().strip().split('\n')

threes = 0
twos = 0
for i in data:
    c = Counter(i)
    if 3 in c.values():
        threes += 1
    if 2 in c.values():
        twos += 1
print(threes * twos)

def isMatch(a, b):
    ans = None
    for i in range(len(a)):
        if a[i] != b[i]:
            if ans is None:
                ans = i
            else:
                return None
    return ans

for i in range(len(data)):
    for j in range(i+1, len(data)):
        ans = isMatch(data[i], data[j])
        if ans is not None:
            print(data[i][:ans] + data[i][ans+1:])


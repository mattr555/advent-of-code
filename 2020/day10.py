from common import *

data = filemap(int, 'day10.txt')
one_jolt = 0
three_jolt = 0
now = 0
for i in sorted(data):
    if i - now == 1:
        one_jolt += 1
    elif i - now == 3:
        three_jolt += 1
    now = i
three_jolt += 1
print(one_jolt * three_jolt)

data = set(data).union({0})
dp = [0] * (max(data) + 4)
dp[0] = 1
for i in range(len(dp)):
    dp[i] += dp[i-1] if i-1 in data else 0
    dp[i] += dp[i-2] if i-2 in data else 0
    dp[i] += dp[i-3] if i-3 in data else 0
print(dp[-1])

import re
from collections import defaultdict

time = r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\]'
time_re = re.compile(time)
guard_re = re.compile(time + r' Guard #(\d+) begins shift')

with open("day4.txt") as f:
    data = f.read().split('\n')

data.sort()
guards = defaultdict(list)

current_guard = None
sleep_time = None
for i in data:
    guard_match = guard_re.match(i)
    if guard_match:
        current_guard = guard_match.group(2)
    else:
        time_match = time_re.match(i)
        if time_match:
            if i.find("falls asleep") > -1:
                sleep_time = int(time_match.group(1))
            else:
                wake_time = int(time_match.group(1))
                guards[current_guard].append((sleep_time, wake_time))

guard_totals = dict(map(lambda i: (i[0], sum(y - x for (x, y) in i[1])), guards.items()))
sleepiest_guard, _ = max(guard_totals.items(), key=lambda x: x[1])

def timeHist(intervals):
    times = [0]*60
    for (start, end) in intervals:
        for i in range(start, end):
            times[i] += 1
    return times

times = timeHist(guards[sleepiest_guard])
best_time = times.index(max(times))
sleepiest_guard = int(sleepiest_guard)
print("the sleepiest guard is", sleepiest_guard)
print("the best time is", best_time)
print("the answer #1 is", best_time * sleepiest_guard)

def fn(i):
    times = timeHist(guards[i])
    return (max(times), times.index(max(times)), i)
best_config = max(map(fn, guards.keys()))
print("the best guard for #2 is", best_config[2])
print("the best minute is", best_config[1])
print("the answer is", best_config[1] * int(best_config[2]))

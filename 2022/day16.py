from common import *
from typing import Set

reg = re.compile("Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)")

def transform(x):
    m = reg.match(x)
    if not m:
        print(x)
    m = m.groups()
    return (m[0], (int(m[1]), set(m[2].split(', '))))

@dataclass(unsafe_hash=True)
class State(object):
    my_current_location: int
    elephant_current_location: int
    open: int
    score: int

data = dict(filemap(transform, 'day16.txt'))

translation = list(data.keys())

fast_data = {}
for k, v in data.items():
    fast_data[translation.index(k)] = (v[0], set(translation.index(x) for x in v[1]))

states = set([State(translation.index('AA'), translation.index('AA'), 0, 0)])

def is_set(v, n):
    return (v >> n) % 2 == 1

def set_bit(v, n):
    return v + (1 << n)

# for step in tqdm(range(30)):
#     new_states = set()
#     for state in states:
#         valve, others = fast_data[state.current_location]
#         if valve > 0 and not is_set(state.open, state.current_location):
#             new_states.add(State(state.current_location, set_bit(state.open, state.current_location), state.score + (30-(step+1)) * valve))
#         for o in others:
#             new_states.add(State(o, state.open, state.score))
#     states = new_states

for step in tqdm(range(26)):
    new_states = set()
    for state in states:
        valve, others = fast_data[state.my_current_location]
        if valve > 0 and not is_set(state.open, state.my_current_location):
            new_states.add(State(state.my_current_location, state.elephant_current_location, set_bit(state.open, state.my_current_location), state.score + (26-(step+1)) * valve))
        for o in others:
            new_states.add(State(o, state.elephant_current_location, state.open, state.score))
    states = new_states

    new_states = set()
    for state in states:
        valve, others = fast_data[state.elephant_current_location]
        if valve > 0 and not is_set(state.open, state.elephant_current_location):
            new_states.add(State(state.my_current_location, state.elephant_current_location, set_bit(state.open, state.elephant_current_location), state.score + (26-(step+1)) * valve))
        for o in others:
            new_states.add(State(state.my_current_location, o, state.open, state.score))
    states = new_states

print(max(x.score for x in states))

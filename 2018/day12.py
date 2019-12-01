with open("day12.txt") as f:
    table = {i[0:5]: i[9] for i in f.read().strip().split('\n')}

initial_state = "##.......#.######.##..#...#.#.#..#...#..####..#.##...#....#...##..#..#.##.##.###.##.#.......###....#"

# from collections import defaultdict
# with open("day12-example.txt") as f:
#     table = defaultdict(lambda: '.')
#     for i in f.read().strip().split('\n'):
#         table[i[0:5]] = i[9]
# initial_state = "#..#.#..##......###...###"

def value(s, n):
    ans = 0
    for ind, i in enumerate(s):
        if i == '#':
            ans += ind - 2*n
    return ans

def doTrans(state):
    old_state = "...." + state + "...."
    new_state = ""
    for i in range(2, len(old_state) - 2):
        new_state += table[old_state[i-2:i+3]]
    return new_state

s = initial_state
first_state = doTrans(s)
for i in range(10000):
    if i % 100 == 0:
        print(s.count('#'))
        print(i, ':', value(s, i))
    s = doTrans(s)
    
    # print(value(s, i))
    # if initial_state in s:
    #     print('!!!')



def do(registers, op):
    new_r = registers.copy()

    if op[0] == 'addr':
        new_r[op[3]] = registers[op[1]] + registers[op[2]]
    elif op[0] == 'addi':
        new_r[op[3]] = registers[op[1]] + op[2]
    elif op[0] == 'mulr':
        new_r[op[3]] = registers[op[1]] * registers[op[2]]
    elif op[0] == 'muli':
        new_r[op[3]] = registers[op[1]] * op[2]
    elif op[0] == 'banr':
        new_r[op[3]] = registers[op[1]] & registers[op[2]]
    elif op[0] == 'bani':
        new_r[op[3]] = registers[op[1]] & op[2]
    elif op[0] == 'borr':
        new_r[op[3]] = registers[op[1]] | registers[op[2]]
    elif op[0] == 'bori':
        new_r[op[3]] = registers[op[1]] | op[2]
    elif op[0] == 'setr':
        new_r[op[3]] = registers[op[1]]
    elif op[0] == 'seti':
        new_r[op[3]] = op[1]
    elif op[0] == 'gtir':
        new_r[op[3]] = 1 if op[1] > registers[op[2]] else 0
    elif op[0] == 'gtri':
        new_r[op[3]] = 1 if registers[op[1]] > op[2] else 0
    elif op[0] == 'gtrr':
        new_r[op[3]] = 1 if registers[op[1]] > registers[op[2]] else 0
    elif op[0] == 'eqir':
        new_r[op[3]] = 1 if op[1] == registers[op[2]] else 0
    elif op[0] == 'eqri':
        new_r[op[3]] = 1 if registers[op[1]] == op[2] else 0
    elif op[0] == 'eqrr':
        new_r[op[3]] = 1 if registers[op[1]] == registers[op[2]] else 0
    return new_r

ALL_OPS = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

with open("day16part1.txt") as f:
    data = f.read().strip('\n').split('\n')

i = 0
part1 = 0
op_map = {i: set(ALL_OPS) for i in range(16)}
while i < len(data):
    before = list(map(int, data[i][9:19].split(',')))
    after = list(map(int, data[i+2][9:19].split(',')))
    op = list(map(int, data[i+1].split()))
    op_code = op[0]

    correct = 0
    correct_op = None
    for o in ALL_OPS:
        op[0] = o
        if do(before, op) == after:
            correct += 1
            correct_op = o
        else:
            op_map[op_code].discard(o)
    if correct >= 3:
        part1 += 1
    # elif correct == 1:
    #     op_map[op_code] = correct_op

    i += 4

while any(len(v) > 1 for v in op_map.values()):
    locked_in = set()
    for k, v in op_map.items():
        if len(v) == 1:
            locked_in |= v

    for k in op_map:
        if len(op_map[k]) != 1:
            op_map[k] -= locked_in

print(part1)
print(op_map)

full_ops = {k: v.pop() for k, v in op_map.items()}
print(full_ops)

registers = [0,0,0,0]
with open("day16part2.txt") as f:
    for l in f.read().strip('\n').split('\n'):
        op = list(map(int, l.split(' ')))
        op[0] = full_ops[op[0]]
        registers = do(registers, op)

print(registers[0])
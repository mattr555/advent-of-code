from common import *

prog = filemap(int, "day5.txt", ',')

def interpret_op(op):
    modes = []
    o = op % 100
    op //= 100
    while op > 0:
        modes.append(op % 10)
        op //= 10
    return o, modes

INST_PARAMS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3
}

def run(data, input_):
    data = list(data)
    input_ = deque(input_)

    ip = 0
    output = []
    while data[ip] != 99:
        op, modes = interpret_op(data[ip])
        modes += [0] * (INST_PARAMS[op] - len(modes))
        
        values = []
        for ix, mode in enumerate(modes):
            if mode == 0:
                values.append(data[data[ip+ix+1]])
            else:
                values.append(data[ip+ix+1])

        v = 0
        skip_inc = False
        if op == 1:
            data[data[ip+3]] = values[0] + values[1]
        elif op == 2:
            data[data[ip+3]] = values[0] * values[1]
        elif op == 3:
            data[data[ip+1]] = input_.popleft()
        elif op == 4:
            output.append(values[0])
        elif op == 5:
            if values[0] != 0:
                ip = values[1]
                skip_inc = True
        elif op == 6:
            if values[0] == 0:
                ip = values[1]
                skip_inc = True
        elif op == 7:
            if values[0] < values[1]:
                data[data[ip+3]] = 1
            else:
                data[data[ip+3]] = 0
        elif op == 8:
            if values[0] == values[1]:
                data[data[ip+3]] = 1
            else:
                data[data[ip+3]] = 0
        
        if not skip_inc:
            ip += INST_PARAMS[op] + 1
    return output

print(run(prog, [1]))
print(run(prog, [5]))

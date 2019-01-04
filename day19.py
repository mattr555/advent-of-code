
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

with open("day19.txt") as f:
    ip = int(f.readline()[4])
    data = f.read().strip('\n').split('\n')

instructions = []
for i in data:
    s = i.split(' ')
    instructions.append((s[0], int(s[1]), int(s[2]), int(s[3])))


registers = [0,0,0,0,0,0]
while registers[ip] < len(instructions):
    if registers[ip] > 16:
        print("ip", registers[ip], "inst", instructions[registers[ip]], "registers", registers)
    registers = do(registers, instructions[registers[ip]])
    registers[ip] += 1

print(registers[0])

registers = [1,0,0,0,0,0]
while registers[ip] < len(instructions):
    to_execute = registers[ip]
    if to_execute > 16 or to_execute == 7:
        print("ip", to_execute, "inst", instructions[to_execute], "registers", registers)
    if to_execute == 35:
        break
    registers = do(registers, instructions[to_execute])
    registers[ip] += 1

# print(registers[0])

print("so..the program calculates the sum of the factors of whatever registers[2] is when the loop starts")
print("registers[2] =", registers[2])
print("i went to wolfram|alpha and got 11151360")
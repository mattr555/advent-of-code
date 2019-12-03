from common import *

initial_data = filemap(int, "day2.txt", ',')

def run(a, b):
    data = list(initial_data)
    data[1] = a
    data[2] = b

    i = 0
    while data[i] != 99:
        v = 0
        if data[i] == 1:
            v = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            v = data[data[i+1]] * data[data[i+2]]
        data[data[i+3]] = v
        i += 4
    return data[0]

print(run(12, 2))

for a in range(100):
    for b in range(100):
        if run(a, b) == 19690720:
            print(100 * a + b)

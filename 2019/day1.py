from common import filemap

data = filemap(int, "day1.txt")

def fuel(n):
    return (n // 3) - 2

print(sum(map(fuel, data)))

def fuelfuel(n):
    total = 0
    while True:
        n = fuel(n)
        if n <= 0:
            break
        total += n
    return total

assert fuelfuel(100756) == 50346
print(sum(map(fuelfuel, data)))

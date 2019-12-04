from common import *

def digits(n):
    n = abs(n)
    ret = []
    while n != 0:
        ret.append(n % 10)
        n //= 10
    ret.reverse()
    return ret

def check(n):
    s = digits(n)
    if len(s) != 6:
        return False, False

    last = -1
    good1 = False
    good2 = False
    repeats = 1
    for i in s:
        if i < last:
            return False, False
        elif i == last:
            repeats += 1
            good1 = True
        else:
            if repeats == 2:
                good2 = True
            repeats = 1
        last = i
    if repeats == 2:
        good2 = True
    return good1, good2


count1 = 0
count2 = 0
for i in range(123257, 647016):
    good1, good2 = check(i)
    if good1:
        count1 += 1
    if good2:
        count2 += 1
print(count1)
print(count2)

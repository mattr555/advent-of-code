from common import *

def meets_criteria(n):
    s = list(map(int, str(n)))
    if len(s) != 6:
        return False
    last = -1
    good = False
    for i in range(len(s)):
        if s[i] < last:
            return False
        elif s[i] == last:
            good = True
        last = s[i]
    return good

def meets_extra_criteria(n):
    s = list(map(int, str(n)))
    if len(s) != 6:
        return False
    last = -1
    good = False
    repeats = 0
    for i in range(len(s)):
        if s[i] < last:
            return False
        elif s[i] == last:
            repeats += 1
        else:
            if repeats == 1:
                good = True
            repeats = 0
        last = s[i]
    if repeats == 1:
        good = True
    return good


c = 0
cc = 0
for i in range(123257, 647016):
    if meets_criteria(i):
        c += 1
    if meets_extra_criteria(i):
        cc += 1
print(c)
print(cc)

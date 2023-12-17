from common import *

def transform(x):
    a, b = x.split(' ')
    return a, list(map(int, b.split(',')))

data = filemap(transform, 'day12.txt')

answers = {}

def memoize(fn):
    def wrapped(s, l):
        hash = 0
        for i in l:
            hash *= 20
            hash += i
        if (s, hash) in answers:
            return answers[(s, hash)]
        answers[(s, hash)] = fn(s, l)
        return answers[(s, hash)]
    return wrapped

@memoize
def go(s, l):
    # call assuming a . is always to the left of s
    if len(s) == 0:
        if len(l) == 0:
            return 1
        return 0

    if s[0] == '.':
        ix = 1
        while ix < len(s) and s[ix] == '.':
            ix += 1
        return go(s[ix:], l)

    if len(l) == 0:
        return 0 if '#' in s else 1

    # can i fit l[0] # starting at s[0]?
    to_place = l[0]
    ix = 0
    ans = 0
    while to_place > 0 and ix < len(s):
        if s[ix] == '?' or s[ix] == '#':
            ix += 1
            to_place -= 1
        else:
            break
    else:
        if to_place == 0:
            # I succeeded in fitting #s
            # is it the end of the string?
            if ix == len(s):
                return 1 if len(l) == 1 else 0
            # otherwise I need to put a dot down next
            if s[ix] == '?' or s[ix] == '.':
                # cool. recur with the hashes + dot done
                ix += 1
                ans += go(s[ix:], l[1:])

    # can I put a . down and go from there?
    if s[0] == '?':
        ans += go(s[1:], l)
    return ans

print(sum(go(a, b) for a, b in data))
print(sum(go('?'.join([a]*5), b*5) for a, b in data))

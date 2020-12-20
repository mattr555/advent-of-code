from common import *



def parse(s):
    def go(s, ix):
        l = []
        i = ix
        while i < len(s):
            if s[i].isdigit():
                l.append(int(s[i]))
            elif s[i] in '+*':
                l.append(s[i])
            elif s[i] == '(':
                inner, i = go(s, i+1)
                # i -= 1
                l.append(inner)
            elif s[i] == ')':
                break
            i += 1
        return l, i

    s = s.replace(' ', '')
    return go(s, 0)[0]
    

def evaluate(s):
    n = 0
    next_op = lambda x, y: y
    for i in s:
        if type(i) is int:
            n = next_op(n, i)
        elif i == '+':
            next_op = lambda x, y: x+y
        elif i == '*':
            next_op = lambda x, y: x*y
        else:
            n = next_op(n, evaluate(i))
    return n


data = filemap(parse, 'day18.txt')
print(sum(map(evaluate, data)))

def evaluate(s):
    n = 0
    # three passes: parentheses, addition, multiplication
    for i in range(len(s)):
        if type(s[i]) is list:
            s[i] = evaluate(s[i])
    
    l = deque()
    i = 0
    while i < len(s):
        if s[i] == '+':
            a = l.pop()
            l.append(a + s[i+1])
            i += 1
        else:
            l.append(s[i])
        i += 1

    n = 1
    while len(l) > 0:
        a = l.popleft()
        if a == '*':
            continue
        n *= a
    return n
print(sum(map(evaluate, data)))

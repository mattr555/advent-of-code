with open("day5.txt") as f:
    data = f.read()

# data = 'dabAcCaCBAcCcaDA'


def react(data):
    newdata = ''
    while True:
        i = 0
        while i < len(data):
            if i < len(data) - 1 and data[i].lower() == data[i+1].lower() and data[i] != data[i+1]:
                i += 2
            else:
                newdata += data[i]
                i += 1
        if len(newdata) == len(data):
            break
        else:
            data = newdata
            newdata = ''
    return newdata

# print(data)
reacted = react(data)
print(len(reacted))

best = len(reacted)

for i in range(26):
    char_to_remove = chr(ord('a') + i)
    this_try = reacted.replace(char_to_remove, '').replace(char_to_remove.upper(), '')
    best = min(best, len(react(this_try)))
    print(char_to_remove)
print(best)


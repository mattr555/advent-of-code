from common import *

def parse(s):
    return s

data = filemap(parse, 'day4.txt', sep='\n\n')

p1 = 0
p2 = 0
for i in data:
    keys = {}
    for line in i.split('\n'):
        for item in line.split(' '):
            key = item[:3]
            keys[key] = item[4:]
    
    if 'cid' in keys:
        del keys['cid']
    if len(keys) == 7:
        p1 += 1

        valid = True
        valid = valid and (keys['byr'].isdigit()) and len(keys['byr']) == 4 and (1920 <= int(keys['byr']) <= 2002)
        valid = valid and (keys['iyr'].isdigit()) and len(keys['iyr']) == 4 and (2010 <= int(keys['iyr']) <= 2020)
        valid = valid and (keys['eyr'].isdigit()) and len(keys['eyr']) == 4 and (2020 <= int(keys['eyr']) <= 2030)
        if keys['hgt'][-2:] == 'in':
            valid = valid and (keys['hgt'][:-2].isdigit()) and (59 <= int(keys['hgt'][:-2]) <= 76)
        elif keys['hgt'][-2:] == 'cm':
            valid = valid and (keys['hgt'][:-2].isdigit()) and (150 <= int(keys['hgt'][:-2]) <= 193)
        else:
            valid = False
        valid = valid and re.match(r'\#[0-9a-f]{6}', keys['hcl'])
        valid = valid and keys['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = valid and keys['pid'].isdigit() and len(keys['pid']) == 9
        if valid:
            p2 += 1

print(p1)
print(p2)


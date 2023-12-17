import os
import sys
import requests

day_file = '''from common import *

def transform(x):
    return x

data = filemap(transform, 'day{:02d}.txt')
'''

if __name__ == "__main__":
    day = int(sys.argv[1])

    with open('secret.txt') as f:
        session = f.read()

    resp = requests.get(
        'https://adventofcode.com/2022/day/{}/input'.format(day),
        headers={'User-Agent': 'mattramina@gmail.com'},
        cookies={'session': session}
    )
    assert resp.status_code == 200

    assert not os.path.exists('day{:02d}.py'.format(day))

    with open('day{:02d}.py'.format(day), 'w') as f:
        f.write(day_file.format(day))

    with open('day{:02d}.txt'.format(day), 'w') as f:
        f.write(resp.content.decode('utf-8'))

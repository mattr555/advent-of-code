from common import *

data = filemap(lambda x: x, 'day04.txt', '\n\n')
numbers = list(map(int, data[0].split(',')))
boards = [[list(map(int, y.split())) for y in x.split('\n')] for x in data[1:]]

def has_bingo(b):
    return any(all(x) for x in b) or \
        any(all(x) for x in transpose(b))

def sum_unmarked(board, marked):
    s = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if not marked[i][j]:
                s += board[i][j]
    return s

def first_bingo(board):
    state = denseGrid(5, 5, False)
    for n, called in enumerate(numbers):
        for x, row in enumerate(board):
            if called in row:
                y = row.index(called)
                state[x][y] = True
        if has_bingo(state):
            return n+1, sum_unmarked(board, state) * called

res = list(sorted(map(first_bingo, boards)))
print(res[0][1])
print(res[-1][1])

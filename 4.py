# create and return a 5x5 array with all elements False
def all_false():
    return [[False for _ in range(5)] for _ in range(5)]

# parse out all possible boards
def parse_boards(lines):
    boards = []
    idx = 0
    while True:
        if idx >= len(lines):
            return boards
        board = [parse_row(lines[idx + i]) for i in range(5)]
        marked = all_false()
        idx += 6
        boards.append([board, marked])

# parse out a row for a board
def parse_row(line):
    return list(map(int, line.strip().split()))

# check if a board has horizontal or vertical bingo
def bingo(marked):
    return any(all(marked[row]) for row in range(5)) or\
        any(all(marked[row][col] for row in range(5)) for col in range(5))

# mark the first occurrence of num in board
def mark(num, board, marked):
    for row in range(5):
        for col in range(5):
            if board[row][col] == num:
                marked[row][col] = True
                return

# sum the unmarked numbers in a board
def sum_unmarked(board, marked):
    return \
    sum(
        sum(0 if marked[row][col] else board[row][col] for col in range(5)) \
        for row in range(5)
    )

# useful for debugging: print the elements of a board
def print_board(board):
    for r in range(5):
        for c in range(5):
            print(board[r][c], end=' ')
        print()

# call a number and mark all boards that have it
def call_num(num, boards):
    for board, marked in boards:
        mark(num, board, marked)

# read data
with open('4.txt') as f:
    lines = f.readlines()

# fetch list of numbers called, and boards
nums = list(map(int, lines[0].strip().split(',')))
boards = parse_boards(lines[2:])

# part 1
solved = False
for num in nums:
    if solved:
        break
    call_num(num, boards)

    for board, marked in boards:
        if bingo(marked):
            solved = True
            print(num * sum_unmarked(board, marked))
            break

# part 2
import sys

# reset all boards
for _, marked in boards:
    marked = all_false()

won_boards = set() # indices of boards that have won
for num in nums:
    call_num(num, boards)

    for idx, (board, marked) in enumerate(boards):
        if idx in won_boards:
            continue

        if bingo(marked):
            if len(won_boards) == len(boards)-1:
                print(num * sum_unmarked(board, marked))
                sys.exit(0)
            won_boards.add(idx)

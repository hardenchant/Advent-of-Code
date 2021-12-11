from utils import get_input


def get_test_input():
    a = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
    return [i.strip() for i in a.split('\n')]


def get_boards(input_board_lines):
    boards = []
    board = []
    for line in input_board_lines:
        if line == '':
            boards.append(board)
            board = []
        else:
            board.append([int(j) for i in line.split('  ') for j in i.split(' ')])
    if board:
        boards.append(board)
    return boards


def check_win(board):
    for line in board:
        if line == [None] * len(line):
            return True
    transposed_board = [*zip(*board)]
    for line in transposed_board:
        # TUPLE HERE!
        if line == (None,) * len(line):
            return True
    return False


def main0(input_lines: list):
    numbers = map(int, input_lines[0].split(','))
    boards = get_boards(input_lines[2:])
    for number in numbers:
        boards = [[[None if num == number else num for num in line] for line in board] for board in boards]
        for board in boards:
            if check_win(board):
                return number * sum([num for line in board for num in line if num is not None])
    return None


def main1(input_lines: list):
    numbers = map(int, input_lines[0].split(','))
    boards = get_boards(input_lines[2:])
    for number in numbers:
        boards = [[[None if num == number else num for num in line] for line in board] for board in boards]
        if len(boards) == 1 and check_win(boards[0]):
            return number * sum([num for line in boards[0] for num in line if num is not None])
        boards = [board for board in boards if not check_win(board)]
    return None


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

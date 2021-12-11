from utils import get_input


def get_test_input():
    a = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    max_size_x = 1000
    max_size_y = 1000
    board = []
    for _ in range(max_size_y):
        board.append(['.'] * max_size_x)

    for line in input_lines:
        first, sec = line.split(' -> ')
        x1, y1 = map(int, first.split(','))
        x2, y2 = map(int, sec.split(','))
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    board[i][x1] = 1 if board[i][x1] == '.' else (board[i][x1] + 1)
            else:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    board[y1][i] = 1 if board[y1][i] == '.' else (board[y1][i] + 1)
    points_count = 0
    for line in board:
        for num in line:
            if num != '.' and int(num) > 1:
                points_count += 1
    return points_count


def main1(input_lines: list):
    max_size_x = 1000
    max_size_y = 1000
    board = []
    for _ in range(max_size_y):
        board.append(['.'] * max_size_x)

    for line in input_lines:
        first, sec = line.split(' -> ')
        x1, y1 = map(int, first.split(','))
        x2, y2 = map(int, sec.split(','))

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                board[i][x1] = 1 if board[i][x1] == '.' else (board[i][x1] + 1)
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                board[y1][i] = 1 if board[y1][i] == '.' else (board[y1][i] + 1)
        elif y2 > y1:
            if x2 - x1 != y2 - y1:
                raise Exception('wtf1')
            for i in range(0, x2 - x1 + 1):
                board[y1 + i][x1 + i] = 1 if board[y1 + i][x1 + i] == '.' else (board[y1 + i][x1 + i] + 1)
        elif y2 < y1:
            if x2 - x1 != y1 - y2:
                raise Exception('wtf2')
            for i in range(0, x2 - x1 + 1):
                board[y1 - i][x1 + i] = 1 if board[y1 - i][x1 + i] == '.' else (board[y1 - i][x1 + i] + 1)
        else:
            raise Exception('wtf3')

    points_count = 0
    for line in board:
        for num in line:
            if num != '.' and int(num) > 1:
                points_count += 1
    return points_count


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

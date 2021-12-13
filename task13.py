from utils import get_input


def get_test_input():
    a = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''
    return [i.strip() for i in a.split('\n')]


def main0(input_lines: list, one_step=True):
    max_x = 0
    max_y = 0
    coords = {}
    folds = []
    fold_mode = False
    for line in input_lines:
        if line == '':
            fold_mode = True
        elif not fold_mode:
            x, y = map(int, line.split(','))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            coords[x, y] = True
        else:
            line, coord = line.split(' ')[-1].split('=')
            folds.append((line, int(coord),))

    for line, coord in folds:
        if line == 'x':
            new_max_x = coord - 1
            for y in range(max_y + 1):
                coords.pop((coord, y), None)
                for x in range(coord + 1, max_x + 1):
                    if (x, y) in coords:
                        coords.pop((x, y))
                        coords[new_max_x - x + coord + 1, y] = True
            max_x = new_max_x
        elif line == 'y':
            new_max_y = coord - 1
            for x in range(max_x + 1):
                coords.pop((x, coord), None)
                for y in range(coord + 1, max_y + 1):
                    if (x, y) in coords:
                        coords.pop((x, y))
                        coords[x, new_max_y - y + coord + 1] = True
            max_y = new_max_y
        if one_step:
            return len(coords.keys())
    return coords, max_x, max_y


def main1(input_lines: list):
    coords, max_x, max_y = main0(input_lines, one_step=False)
    board = [[' ' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for x, y in coords.keys():
        board[y][x] = '\33[7m \33[m'
    for l in board:
        print(''.join(l))
    return None


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0, test:', main0(test_input_lines))
    print('Answer 1, test:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, real:', main0(real_input))
    print('Answer 1, real:', main1(real_input))

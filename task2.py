from utils import get_input


def get_test_input():
    a = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    pos = 0
    depth = 0
    for i in input_lines:
        command, num = i.split(' ')
        num = int(num)
        match command:
            case 'forward':
                pos += num
            case 'down':
                depth += num
            case 'up':
                depth -= num
            case _:
                raise Exception('wtf')
    return pos * depth


def main1(input_lines: list):
    pos = 0
    depth = 0
    aim = 0
    for i in input_lines:
        command, num = i.split(' ')
        num = int(num)
        match command:
            case 'forward':
                pos += num
                depth += aim * num
            case 'down':
                aim += num
            case 'up':
                aim -= num
            case _:
                raise Exception('wtf')
    return pos * depth


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

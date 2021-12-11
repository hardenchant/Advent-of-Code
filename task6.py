from utils import get_input


def get_test_input():
    a = '''3,4,3,1,2'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    fishs = list(map(int, input_lines[0].split(',')))
    for i in range(80):
        to_append = fishs.count(0)
        fishs = [6 if i == 0 else i - 1 for i in fishs]
        for _ in range(to_append):
            fishs.append(8)
    return len(fishs)


def main1(input_lines: list):
    fishs = list(map(int, input_lines[0].split(',')))
    fishs_d = {}
    fishs = [6 - i for i in fishs]
    for i in fishs:
        fishs_d[i] = fishs_d[i] + 1 if i in fishs_d else 1
    next_day = 0
    next_2day = 0
    for _ in range(256):
        fishs_d = {((k + 1) % 7): v for k, v in fishs_d.items()}
        to_append = fishs_d.get(0, 0)
        fishs_d[0] = fishs_d[0] + next_day if 0 in fishs_d else next_day
        next_day = next_2day
        next_2day = to_append
    return sum(fishs_d.values()) + next_day + next_2day


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

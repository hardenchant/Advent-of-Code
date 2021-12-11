from utils import get_input


def get_test_input():
    a = '''16,1,2,0,4,2,7,1,2,14'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    crabs = [int(i) for i in input_lines[0].split(',')]
    crabs = sorted(crabs)
    lowest_fuel = 99999999999
    for i in range(crabs[-1]):
        candidate = sum([abs(crab - i) for crab in crabs])
        if candidate < lowest_fuel:
            lowest_fuel = candidate
    return lowest_fuel


def main1(input_lines: list):
    crabs = [int(i) for i in input_lines[0].split(',')]
    crabs = sorted(crabs)
    lowest_fuel = 99999999999
    for i in range(crabs[-1]):
        candidate = int(sum([(abs(crab - i) + 1) * abs(crab - i) / 2 for crab in crabs]))
        if candidate < lowest_fuel:
            lowest_fuel = candidate
    return lowest_fuel


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

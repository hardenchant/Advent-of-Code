from utils import get_input


def get_test_input():
    a = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def _main0(input_lines: list):
    records_count = len(input_lines)
    ones_stat = {i: 0 for i in range(len(input_lines[0]))}
    for record in input_lines:
        for num, i in enumerate(record):
            if int(i):
                ones_stat[num] += 1
    gamma_bin = ''.join(['1' if ones_stat[i] > records_count / 2 else '0' for i in range(len(input_lines[0]))])
    epsilon_bin = ''.join(['0' if int(i) else '1' for i in gamma_bin])
    strange_bits = [bit_num for bit_num, stat in ones_stat.items() if stat == records_count / 2]
    return gamma_bin, epsilon_bin, strange_bits


def main0(input_lines: list):
    gamma_bin, epsilon_bin, _ = _main0(input_lines)
    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)
    return gamma * epsilon


def get_oxygen_gen_rating_bin(input_lines):
    cur_list = list(input_lines)
    for i in range(len(input_lines[0])):
        gamma_bin, _, strange_bits = _main0(cur_list)
        if i in strange_bits:
            oxygen_gen_rating_next_bit = '1'
        else:
            oxygen_gen_rating_next_bit = gamma_bin[i]
        cur_list = [line for line in cur_list if line[i] == oxygen_gen_rating_next_bit]
        if len(cur_list) == 1:
            return cur_list[0]
    raise Exception('wtf')


def get_co2_scrub_rating_bin(input_lines):
    cur_list = list(input_lines)
    for i in range(len(input_lines[0])):
        _, epsilon_bin, strange_bits = _main0(cur_list)
        if i in strange_bits:
            oxygen_gen_rating_next_bit = '0'
        else:
            oxygen_gen_rating_next_bit = epsilon_bin[i]
        cur_list = [line for line in cur_list if line[i] == oxygen_gen_rating_next_bit]
        if len(cur_list) == 1:
            return cur_list[0]
    raise Exception('wtf')


def main1(input_lines: list):
    oxygen_gen_rating_bin = get_oxygen_gen_rating_bin(input_lines)
    co2_scrub_rating_bin = get_co2_scrub_rating_bin(input_lines)

    return int(oxygen_gen_rating_bin, 2) * int(co2_scrub_rating_bin, 2)


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

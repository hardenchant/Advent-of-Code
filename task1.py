from utils import get_input


def get_test_input():
    a = '''199
200
208
210
200
207
240
269
260
263'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


def main0(input_lines: list):
    nums = [int(i) for i in input_lines]
    prev = nums[0]
    res = 0
    for i in nums[1:]:
        if i > prev:
            res += 1
        prev = i
    return res


def main1(input_lines: list):
    nums = [int(i) for i in input_lines]
    new_nums = []
    for i in range(len(nums) - 2):
        new_nums.append(sum(nums[i: i + 3]))
    return main0(new_nums)


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

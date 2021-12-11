import itertools
import math

from utils import get_input


def get_test_input():
    a = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


coords_getters = (
    lambda y, x: (y - 1, x),
    lambda y, x: (y, x - 1),
    lambda y, x: (y, x + 1),
    lambda y, x: (y + 1, x),
)


def get_lower_points_coord_to_value(handle_map):
    lower_points_coord_to_value = {}
    for y, x in itertools.product(range(len(handle_map)), range(len(handle_map[0]))):
        if handle_map[y][x][0] == 9:
            continue
        lower_points_coord_to_value[y, x] = handle_map[y][x][0]
        for coords_getter in coords_getters:
            y2, x2 = coords_getter(y, x)
            if y2 < 0 or x2 < 0:
                continue
            try:
                if (y2, x2) in lower_points_coord_to_value or not handle_map[y][x][0] < handle_map[y2][x2][0]:
                    lower_points_coord_to_value.pop((y, x))
                    break
            except IndexError:
                pass
    return lower_points_coord_to_value


def main0(input_lines: list):
    handle_map = [[(int(i), False) for i in list(line)] for line in input_lines]
    lower_points_coord_to_value = get_lower_points_coord_to_value(handle_map)
    return sum(lower_points_coord_to_value.values()) + len(lower_points_coord_to_value)


def recursive_get_basins(y, x, handle_map):
    to_sum = [1]
    handle_map[y][x] = handle_map[y][x][0], True
    for coords_getter in coords_getters:
        y2, x2 = coords_getter(y, x)
        if y2 < 0 or x2 < 0:
            continue
        try:
            handle_map[y2][x2]
        except IndexError:
            continue
        if handle_map[y2][x2][0] == 9 or handle_map[y2][x2][1]:
            continue
        if handle_map[y][x][0] < handle_map[y2][x2][0]:
            handle_map, value = recursive_get_basins(y2, x2, handle_map)
            to_sum.append(value)
    return handle_map, sum(to_sum)


def main1(input_lines: list):
    handle_map = [[(int(i), False) for i in list(line)] for line in input_lines]
    lower_points_coord_to_value = get_lower_points_coord_to_value(handle_map)
    basin_lengths = []
    for (y, x) in lower_points_coord_to_value.keys():
        handle_map, value = recursive_get_basins(y, x, handle_map)
        basin_lengths.append(value)
    return math.prod(list(reversed(sorted(basin_lengths)))[:3])


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

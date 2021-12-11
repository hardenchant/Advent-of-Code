import itertools

from utils import get_input


def get_test_input():
    a = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''
    return [i.strip() for i in a.split('\n') if i.strip() != '']


coords_getters = (
    lambda y, x: (y - 1, x),
    lambda y, x: (y + 1, x),
    lambda y, x: (y, x - 1),
    lambda y, x: (y, x + 1),
    lambda y, x: (y - 1, x - 1),
    lambda y, x: (y - 1, x + 1),
    lambda y, x: (y + 1, x + 1),
    lambda y, x: (y + 1, x - 1),
)


def handle_flashed_octopuse(y, x, octopuses) -> list[list]:
    for coords_getter in coords_getters:
        y2, x2 = coords_getter(y, x)
        if y2 < 0 or x2 < 0:
            continue
        try:
            octopuses[y2][x2] += 1
        except IndexError:
            continue
    return octopuses


def get_flashed_coords(octopuses) -> set:
    return set(
        (y, x) for y, x in itertools.product(range(len(octopuses)), range(len(octopuses[0]))) if octopuses[y][x] > 9
    )


def main0(input_lines: list):
    octopuses = [[int(i) for i in line] for line in input_lines]
    flashed = 0
    for _ in range(100):
        octopuses = [[i + 1 for i in line] for line in octopuses]
        flashed_coords = get_flashed_coords(octopuses)
        new_flashed_coords = set(flashed_coords)
        while new_flashed_coords:
            for coords in new_flashed_coords:
                octopuses = handle_flashed_octopuse(*coords, octopuses)
            new_flashed_coords = get_flashed_coords(octopuses) - flashed_coords
            flashed_coords.update(new_flashed_coords)
        flashed += len(flashed_coords)
        for y, x in flashed_coords:
            octopuses[y][x] = 0
    return flashed


def main1(input_lines: list):
    octopuses = [[int(i) for i in line] for line in input_lines]
    octopuses_count = sum([len(i) for i in octopuses])
    for i in range(1000):
        octopuses = [[i + 1 for i in line] for line in octopuses]
        flashed_coords = get_flashed_coords(octopuses)
        new_flashed_coords = set(flashed_coords)
        while new_flashed_coords:
            for coords in new_flashed_coords:
                octopuses = handle_flashed_octopuse(*coords, octopuses)
            new_flashed_coords = get_flashed_coords(octopuses) - flashed_coords
            flashed_coords.update(new_flashed_coords)
        if len(flashed_coords) == octopuses_count:
            return i + 1
        for y, x in flashed_coords:
            octopuses[y][x] = 0
    return None


if __name__ == '__main__':
    test_input_lines = get_test_input()
    print('Answer 0,  test data:', main0(test_input_lines))
    print('Answer 1,  test data:', main1(test_input_lines))

    real_input = get_input(__file__)
    print('Answer 0, input data:', main0(real_input))
    print('Answer 1, input data:', main1(real_input))

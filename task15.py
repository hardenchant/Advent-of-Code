import itertools
import time
from datetime import datetime

from utils import get_input


def get_test_input():
    a = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''
    return [i.strip() for i in a.split('\n')]


coords_getters = (
    lambda y, x: (y + 1, x),
    lambda y, x: (y, x + 1),
)


def get_matr_plus(matr, num):
    return [[9 if i + num == 9 else (i + num) % 9 for i in line] for line in matr]


def main0(input_lines: list):
    max_len_y = len(input_lines)
    max_len_x = len(input_lines[0])
    path_matr = [[int(i) for i in line] for line in input_lines]

    nodes = tuple(i for i in range(max_len_y * max_len_x))
    distances = {}

    for y, x in itertools.product(range(max_len_y), range(max_len_x)):
        for coords_getter in coords_getters:
            y1, x1 = coords_getter(y, x)
            if y1 > max_len_y - 1 or x1 > max_len_x - 1:
                continue
            cur_point = max_len_x * y + x
            neib_point = max_len_x * y1 + x1
            distances[cur_point] = {**distances.get(cur_point, {}), neib_point: path_matr[y1][x1]}
            distances[neib_point] = {**distances.get(neib_point, {}), cur_point: path_matr[y][x]}

    # dijkstra
    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = 0
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    return visited[max_len_y * max_len_x - 1]


def main1(input_lines: list):
    max_len_y = len(input_lines) * 5
    max_len_x = len(input_lines[0]) * 5
    path_matr = [[int(i) for i in line] for line in input_lines]
    matrs = [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
    ]
    matrs_inc = [[get_matr_plus(path_matr, num) for num in line] for line in matrs]
    final_matr = []
    for line_matrs in matrs_inc:
        for i in range(len(line_matrs[0])):
            final_line = []
            for matr in line_matrs:
                final_line.extend(matr[i])
            final_matr.append(final_line)
    path_matr = final_matr

    nodes = tuple(i for i in range(max_len_y * max_len_x))
    distances = {}

    for y, x in itertools.product(range(max_len_y), range(max_len_x)):
        for coords_getter in coords_getters:
            y1, x1 = coords_getter(y, x)
            if y1 > max_len_y - 1 or x1 > max_len_x - 1:
                continue
            cur_point = max_len_x * y + x
            neib_point = max_len_x * y1 + x1
            distances[cur_point] = {**distances.get(cur_point, {}), neib_point: path_matr[y1][x1]}
            distances[neib_point] = {**distances.get(neib_point, {}), cur_point: path_matr[y][x]}

    # dijkstra
    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = 0
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    return visited[max_len_y * max_len_x - 1]


if __name__ == '__main__':
    test_input_lines = get_test_input()
    n = datetime.now()
    # print('Answer 0, test:', main0(test_input_lines))
    print('Answer 1, test:', main1(test_input_lines))
    print(datetime.now() - n)

    real_input = get_input(__file__)
    n = datetime.now()
    # print('Answer 0, real:', main0(real_input))
    print('Answer 1, real:', main1(real_input))
    print(datetime.now() - n)

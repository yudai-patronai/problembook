#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def get_map(cell_cost):
    N = len(cell_cost)
    to_cost = [[10 ** 6] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j == 0:
                to_cost[i][j] = cell_cost[i][j]
            elif j == 0:
                to_cost[i][j] = to_cost[i - 1][j]
            elif i == 0:
                to_cost[i][j] = to_cost[i][j - 1]
            else:
                to_cost[i][j] = min(to_cost[i - 1][j], to_cost[i][j - 1])
            to_cost[i][j] += cell_cost[i][j]

    i = j = N - 1
    path = []
    while True:
        path.insert(0, (i, j))
        if i == j == 0:
            break
        if i == 0 or to_cost[i][j - 1] < to_cost[i - 1][j]:
            j = j - 1
            continue
        i = i - 1
        continue

    res = [["." for _ in range(N)] for _ in range(N)]
    for i, j in path:
        res[i][j] = "#"

    return res


def write_test(name, a, res_map):
    with open(name, "w") as f:
        f.write(str(len(a))+"\n")
        f.write("\n".join(["".join(map(str, x)) for x in a]))
    with open(name+".a", "w") as f:
        f.write("\n".join(["".join(map(str, x)) for x in res_map]))


def generate_test(name, n=None):
    n = random.randint(1, 100) if n is None else n
    a = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    res_map = get_map(a)

    write_test(name, a, res_map)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(
        os.path.join(test_folder, "01"),
        [
            [9, 4, 3],
            [2, 1, 6],
            [0, 9, 1]
        ],
        [
            ["#", ".", "."],
            ["#", "#", "#"],
            [".", ".", "#"]
        ]
    )
    generate_test(os.path.join(test_folder, "02"), 3)
    generate_test(os.path.join(test_folder, "03"), 4)
    generate_test(os.path.join(test_folder, "05"), 4)
    generate_test(os.path.join(test_folder, "06"))
    generate_test(os.path.join(test_folder, "07"))
    generate_test(os.path.join(test_folder, "08"))

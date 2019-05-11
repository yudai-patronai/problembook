#!/usr/bin/env python3

import os
import shutil
import random

random.seed(42)


def solve(x, y):
    d = [[0] * 8 for _ in range(8)]
    d[y][x] = 1
    for i in range(y + 1, 8):
        for j in range(8):
            if j - 1 >= 0:
                d[i][j] += d[i - 1][j - 1]
            if j + 1 < 8:
                d[i][j] += d[i - 1][j + 1]
    return sum(d[7])


def generate_test(name):
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    with open(name, "w") as f:
        f.write(' '.join(map(str, [x, y])) + "\n")
    with open(name + ".a", "w") as f:
        f.write(str(solve(x-1, y-1)) + "\n")


def write_manual_test(name, x, y):
    with open(name, "w") as f:
        f.write(' '.join(map(str, [x, y])) + "\n")
    with open(name + ".a", "w") as f:
        f.write(str(solve(x - 1, y - 1)) + "\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    generate_test(os.path.join(test_folder, "01"))
    generate_test(os.path.join(test_folder, "02"))
    generate_test(os.path.join(test_folder, "03"))
    generate_test(os.path.join(test_folder, "04"))
    generate_test(os.path.join(test_folder, "05"))
    write_manual_test(os.path.join(test_folder, "06"), 4, 8)
    write_manual_test(os.path.join(test_folder, "07"), 7, 8)
    write_manual_test(os.path.join(test_folder, "08"), 8, 5)
    write_manual_test(os.path.join(test_folder, "09"), 8, 1)

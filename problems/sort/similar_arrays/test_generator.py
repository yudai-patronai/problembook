#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def generate_test(test_file):
    n = random.randint(1, 1000)
    m = random.randint(1, 1000)
    a = [random.randint(-1000000, 100000) for _ in range(n)]
    b = [random.randint(-1000000, 100000) for _ in range(m)]
    with open(test_file, 'w') as f:
        f.write(' '.join(map(str, [len(a), len(b)])) + '\n')
        f.write(' '.join(map(str, a)) + '\n')
        f.write(' '.join(map(str, b)) + '\n')
    with open(test_file + '.a', 'w') as f:
        f.write(['No', 'Yes'][set(a) == set(b)] + '\n')


def write_test(test_file, a, b):
    p = set(a)
    q = set(b)
    with open(test_file, 'w') as f:
        f.write(' '.join(map(str, [len(a), len(b)])) + '\n')
        f.write(' '.join(map(str, a)) + '\n')
        f.write(' '.join(map(str, b)) + '\n')
    with open(test_file + '.a', 'w') as f:
        f.write(['No', 'Yes'][p == q] + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(os.path.join(test_folder, "01"), [1], [1, 1, 1])
    write_test(os.path.join(test_folder, "02"), [5, 7, 6, 1], [1, 1, 1, 1, 5, 7, 6, 7, 6, 5])
    write_test(os.path.join(test_folder, "03"), [4, 7, 2, 2, 1], [4, 7, 2, 1, 8])
    write_test(os.path.join(test_folder, "04"), [1, 2, 3], [2, 3])
    write_test(os.path.join(test_folder, "05"), [random.randint(-1000000, 100000) for _ in range(1000)],
               [random.randint(-1000000, 100000) for _ in range(1000)])

    for test in range(6, 10):
        generate_test(os.path.join(test_folder, "0{}".format(test)))

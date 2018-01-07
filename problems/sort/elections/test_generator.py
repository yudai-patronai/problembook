#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def generate_test(test_file):
    n = random.randint(1, 10000)
    a = [random.randint(1, 100000) for _ in range(n)]
    b = sorted(a)
    s = 0
    for i in range(n // 2 + 1):
        s += b[i] // 2 + 1
    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, a)))
    with open(test_file + '.a', 'w') as f:
        f.write(str(s) + '\n')


def write_test(test_file, a):
    n = len(a)
    b = sorted(a)
    s = 0
    for i in range(n // 2 + 1):
        s += b[i] // 2 + 1
    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, a)))
    with open(test_file + '.a', 'w') as f:
        f.write(str(s) + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(os.path.join(test_folder, "01"), [1])
    write_test(os.path.join(test_folder, "02"), [158])
    write_test(os.path.join(test_folder, "03"), [1, 1, 1, 1, 1, 1, 1])
    write_test(os.path.join(test_folder, "04"), [2, 45, 7, 6, 33])
    write_test(os.path.join(test_folder, "05"), [random.randint(1, 100000) for _ in range(10000)])

    for test in range(6, 10):
        generate_test(os.path.join(test_folder, "0{}".format(test)))

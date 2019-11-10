#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)

RANDOM_TEST_MAX_LEN = 1000

def generate_test(test_file):
    n = random.randint(1, RANDOM_TEST_MAX_LEN) & (~1)
    a = [random.randint(1, 1000000) for _ in range(n)]
    b = sorted(a)
    s = 0
    for i in b[:n//2]:
        s -= i
    for i in b[n//2:]:
        s += i
    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, a)))
    with open(test_file + '.a', 'w') as f:
        f.write(str(s) + '\n')


def write_test(test_file, a):
    n = len(a)
    b = sorted(a)
    s = 0
    for i in b[:n//2]:
        s -= i
    for i in b[n//2:]:
        s += i
    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, a)))
    with open(test_file + '.a', 'w') as f:
        f.write(str(s) + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    write_test(os.path.join(test_folder, "01"), [1, 1])
    write_test(os.path.join(test_folder, "02"), [158, 5])
    write_test(os.path.join(test_folder, "03"), [2, 45, 7, 6, 33, 15])
    write_test(os.path.join(test_folder, "04"), [random.randint(1, 1000000) for _ in range(RANDOM_TEST_MAX_LEN)])

    for test in range(5, 10):
        generate_test(os.path.join(test_folder, "0{}".format(test)))

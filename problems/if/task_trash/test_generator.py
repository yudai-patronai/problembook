#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
    (1024, 32, 'BINGO'),
    (1, 2, 'NO'),
    (3, 5, 'ZZ'),
    (3, 9, 'ZZ'),
    (4, 16, 'NO'),
    (1, 1024, 'BINGO'),
    (1024, 1025, 'BINGO'),
    (25, 5, '125'),
    (100, 10, '1000'),
    (25, 7, 'NORM_SMALL'),
    (25, 9, 'NORM_SMALL'),
    (25, 10, 'NORMAL'),
    (1025, 1024, 'BINGO'),
    (1048576, 1024, 'BINGO'),
    (1, 1, 'UNKNOWN'),
    (2, 2, 'UNKNOWN'),
    (25, 25, 'UNKNOWN'),
    (1024, 1024, 'BINGO')
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(data[0]) + '\n' + str(data[1]) + '\n')

    with open(ans, 'w') as f:
        f.write(data[2] + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i + 1, t)


write_tests(tests_dir)

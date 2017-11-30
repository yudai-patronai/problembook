#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
    # a b c d x ans
    (2, 4, 2, 4, 2, 5),
    (1, 1, 1, 1, 1024, 3),
    (2, 4, 20, 4, 2, 4),
    (10, 4, 4, 16, 4, 4),
    (100, 1124, 10, 10240, 1024, 5),
    (200, 1224, 10, 10, 1024, 4),
    (0, 1125, -1, -1024, 1024, 4),
    (1, 1, 1, 2, 1, 2)
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write('\n'.join(map(str, data[0:-1])) + '\n')

    with open(ans, 'w') as f:
        f.write(str(data[-1]) + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i + 1, t)


write_tests(tests_dir)

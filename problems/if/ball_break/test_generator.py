#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
    # n m k x answer
    (10, 7, 5, 1, 'NO'),
    (10, 14, 10, 2, 'YES'),
    (10, 7, 5, 2, 'NO'),
    (10, 7, 5, 3, 'NO'),
    (10, 7, 10, 1, 'NO'),
    (10, 7, 10, 3, 'NO'),
    (10, 7, 10, 100, 'NO'),
    (10, 11, 10, 1, 'NO'),
    (10, 50, 10, 100, 'NO'),
    (10, 11, 12, 1, 'YES'),
    (10, 14, 15, 2, 'YES'),
    (10, 50, 100, 100, 'YES'),
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write('\n'.join(map(str, data[0:-1])) + '\n')

    with open(ans, 'w') as f:
        f.write(data[-1] + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i + 1, t)


write_tests(tests_dir)

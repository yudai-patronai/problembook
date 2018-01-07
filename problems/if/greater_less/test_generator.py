#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
    ('1 < 2', 'YES'),
    ('10 > 100', 'NO'),
    ('1 > 53', 'NO'),
    ('100 < 1000', 'YES'),
    ('10050 < 1000', 'NO')
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(data[0].replace(' ', '\n') + '\n')

    with open(ans, 'w') as f:
        f.write(data[1] + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i + 1, t)


write_tests(tests_dir)

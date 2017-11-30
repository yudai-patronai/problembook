#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
    ('200', 'monkey', '2'),
    ('200', 'elephant', '1'),
    ('200', 'parrot', '20'),
    ('8500', 'monkey', '94'),
    ('8500', 'elephant', '28'),
    ('8500', 'parrot', '850'),
    ('50', 'elephant', '1'),
    ('50', 'parrot', '5'),
    ('50', 'monkey', '1')
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(data[0] + '\n' + data[1] + '\n')

    with open(ans, 'w') as f:
        f.write(data[2] + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i + 1, t)


write_tests(tests_dir)

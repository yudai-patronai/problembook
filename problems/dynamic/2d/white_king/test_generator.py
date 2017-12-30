#!/usr/bin/env python3
import os
import shutil

tests = ['b2', 'e5', 'b8', 'b1', 'h8', 'g6', 'd3']

def write_test(fname, test):
    with open(fname, 'w') as f:
        f.write(test + '\n')

    os.system('python3 solution.py < ' + fname + ' > ' + fname + '.a')


def write_tests(tests_dir, tests):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(os.path.join(tests_dir, '%.2d' % (i + 1)), t)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
write_tests(tests_dir, tests)

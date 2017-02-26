#!/usr/bin/python3

import random
import sys
import os
import shutil
import subprocess

random.seed(42)

prob_dir = os.path.dirname(__file__)
tests_dir = os.path.join(prob_dir, 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

simple_tests = [
    (
        random.randint(10, 50),
        [0, 0, random.randint(10, 20), random.randint(30, 40)],
        [1, 4]
    ),
    (
        random.randint(10, 50),
        [0, 0, random.randint(-20, -10), random.randint(10, 20), random.randint(10, 100)],
        [1, 4]
    ),
    (
        random.randint(10, 50),
        [0, 1000, random.randint(10, 20), random.randint(30, 40)],
        [1, 4]
    ),
    (
        random.randint(10, 50),
        [0, 0] + [random.randint(-100, -1) for i in range(10)],
        [1]
    )
]

for i in range(50):
    if i < len(simple_tests):
        m, _in, _out = simple_tests[i]
    else:
        m = random.randint(10, 50)
        _in = [random.randint(-100, 1000) for i in range(random.randint(5, 50))]

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write('{}\n{}'.format(m, ' '.join(map(str, _in))))

    if i >= len(simple_tests):
        with open(os.path.join(tests_dir, '{0:0>2}'.format(i))) as fin:
            output = subprocess.check_output([sys.executable, os.path.join(prob_dir, 'solution.py')], stdin=fin).decode('utf-8')
            _out = list(map(int, output.strip().split()))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write(' '.join(map(str, _out)))
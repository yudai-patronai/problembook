#!/usr/bin/python3

import os
import shutil

from lib import random

N = 50
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


for i in range(1, N + 1):
    l = random.randint(1, 100)
    input = [random.randint(l//3) for i in range(l)]

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n{1}\n".format(l, ' '.join(map(str, input))))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        m = min(input)
        c = input.count(m)
        f.write('{} {}'.format(m, c))

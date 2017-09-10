#!/usr/bin/python3

import os
import shutil
from lib import random
from math import sqrt

N = 50;
random.seed(20000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    x = random.randrange(2,20000)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n".format(x))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(format(int(all(x % i for i in range(2, int(sqrt(x)))))))

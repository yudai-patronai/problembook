#!/usr/bin/python3

import os
import shutil
from lib import random

N = 50;
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    x1 = random.randrange(-10000,10000)
    x2 = random.randrange(-10000,10000)

    if x1 > x2:
        ret = 1
    elif x1 < x2:
        ret = 2
    else:
        ret = 0

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0} {1}\n".format(x1, x2))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(format(ret))

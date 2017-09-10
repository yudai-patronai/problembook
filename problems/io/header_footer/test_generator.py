#!/usr/bin/python3

import os
import shutil
from lib import random

N = 50;
random.seed(2000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    x1 = random.randrange(-1000,1000)
    x2 = random.randrange(-1000,1000)
    x3 = random.randrange(-1000,1000)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0} {1} {2}\n".format(x1, x2, x3))

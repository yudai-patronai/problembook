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
    x = random.randint(1,1000)
    out = []
    for j in range(1, x + 1):
        out.append(random.randint(-100,100))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n{1}\n".format(x, ' '.join(str(cell) for cell in out)))

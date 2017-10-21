#!/usr/bin/python3

import os
import shutil
from lib import random
from math import sqrt

N = 50;
random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N):
    x = random.randint(1,30000)

    out = []
    for num in range(2, x + 1):
        if all(num % j for j in range(2, int(sqrt(num)) + 1)):
            out.append(num)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n".format(x))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write('{}\n'.format(' '.join(str(val) for val in out)))
            
#custom test
with open(os.path.join(tests_dir, '{0:0>2}'.format(N)), 'w') as f:
        f.write("1\n".format(x))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(N)), 'w') as f:
        f.write('0\n')
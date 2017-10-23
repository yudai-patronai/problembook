#!/usr/bin/python3

import os
import shutil
from lib import random

NUM_TEST = 50
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 1000)
    array = []
    for j in range(n):
        array.append(random.randint(1, 1000))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n{1}\n'.forman(n, ' '.join(str(val) for val in array)))

    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write('{0}\n'.format(sorted(array))
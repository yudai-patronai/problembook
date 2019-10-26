#!/usr/bin/python3

import os
import shutil
from lib import random

NUM_TEST = 10
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 10)
    array = [random.randint(-1000, 1000) for _ in range(n)]

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n'.format(' '.join(str(val) for val in array)))

    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        mi = 0
        while mi < len(array) - 1:
            if array[mi] > array[mi + 1]:
                array[mi], array[mi + 1] = array[mi + 1], array[mi]
                f.write('{0}\n'.format(' '.join(map(str, array))))
                mi = 0
            else:
                mi += 1


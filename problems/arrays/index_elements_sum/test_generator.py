#!/usr/bin/python3

import os
import shutil
from lib import random

NUM_TEST = 15
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 1000)
    array = []
    answer_sum = 0
    temp = 0
    for j in range(n):
        temp = random.randint(1, 1000)
        array.append(temp)
        if ((j % 3 == 0) and (j % 7 == 0)):
            answer_sum += temp

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n{1}\n'.format(n, ' '.join(str(val) for val in array)))
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write('{0}\n'.format(answer_sum))

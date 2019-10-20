#!/usr/bin/python3

import os
import shutil
from lib import random

NUM_TEST = 10
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

def selection_sort(a):
    outputs = []
    for i in range(0, len(a) - 1):
        min_j = i
        for j in range(i, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
        outputs.append(' '.join(map(str, a)))
        return outputs



for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 10)
    array = [random.randint(-1000, 1000) for _ in range(n)]

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n'.format(' '.join(str(val) for val in array)))

    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        outputs = selection_sort(array)
        for el in outputs:
            f.write('{0}\n'.format(el))

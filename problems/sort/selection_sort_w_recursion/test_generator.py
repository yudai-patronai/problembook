#!/usr/bin/python3

import os
import shutil
from lib import random

NUM_TEST = 10
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

def recursive_selection_sort(a):
    outputs = []
    selection_sort(a, 0, outputs)
    return outputs

def selection_sort(a, index, outputs):
    if index < len(a) - 1:
        str_a  = ' '.join(map(str, a))
        min_ = find_min(a, index)
        a[index], a[min_] = a[min_], a[index]
        str_a_new = ' '.join(map(str, a))
        if str_a_new != str_a:
            str_a = str_a_new
            outputs.append(str_a)
        selection_sort(a, index + 1, outputs)


def find_min(a, index):
    min_ = index - 1
    if index < len(a) - 1:
        min_ = find_min(a, index + 1)
    if a[min_] > a[index]:
        min_ = index
    return min_


for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 10)
    array = [random.randint(-1000, 1000) for _ in range(n)]

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n'.format(' '.join(str(val) for val in array)))

    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        outputs = recursive_selection_sort(array)
        for el in outputs:
            f.write('{0}\n'.format(el))

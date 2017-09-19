#!/usr/bin/python3

import os
from lib import random
import shutil
import subprocess
import sys

NUM_TEST = 50

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, NUM_TEST + 1):
    count = i**2
    shift = random.randint(1, 2*count)

    # build array of random numbers
    array = []

    for j in range(count):
        array.append(random.randint(-10000,10000))

    # store it as task input
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write('{0} {1}\n{2}\n'.format(count, shift, ' '.join(str(val) for val in array)))

    # print expected output
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write('{} '.format(' '.join(str(val) for val in array[shift % count:])))
        fout.write('{}\n'.format(' '.join(str(val) for val in array[:shift % count])))

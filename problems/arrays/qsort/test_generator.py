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

# number of elements grows as i**3 so for 50th test 125000 elements to sort
for i in range(1, NUM_TEST + 1):
    # build array of random numbers
    array = []

    for j in range(i**3):
        array.append(random.randint(-10000,10000))

    # store it as task input
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write('{0}\n{1}\n'.format(i**3, ' '.join(str(val) for val in array)))

    # sort and save it as expected output
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write('{}\n'.format(' '.join(str(val) for val in sorted(array))))

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

	n = random.randint(1, 1000)
	array = []
	for j in range(n):
		array.append(random.randint(1, 1000))

	with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
		f.write('{0}\n{1}\n'.format(n, ' '.join(str(val) for val in array)))
	with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
		f.write('{}\n'.format(' '.join(str(val) for val in reversed(array))))

#!/usr/bin/python3

import random
import sys
import os
import shutil
import subprocess

NUM_TEST = 50

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, NUM_TEST+1):
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write('{}'.format(random.randint(1,10000)))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i))) as fin:
        output = subprocess.check_output([sys.executable,
                                             os.path.join(os.path.dirname(__file__),
                                             'solution.py')], stdin=fin).decode('utf-8')
        __output_data = int(output.strip())

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write('{}'.format(__output_data))

#!/usr/bin/env python3

import os
import shutil
from queue import Queue
from solution import solve

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

# simple tests
with open(os.path.join(tests_dir, '{0:0>2}'.format(1)), 'w') as f:
    f.write("{0} {1}\n".format(2, 2))
    f.write("0 0\n")
    f.write("0 2\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(1)), 'w') as f:
    f.write("2\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(2)), 'w') as f:
    f.write("{0} {1}\n".format(3, 3))
    f.write("0 1 2\n")
    f.write("0 0 0\n")
    f.write("0 0 0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(2)), 'w') as f:
    f.write("3\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(3)), 'w') as f:
    f.write("{0} {1}\n".format(4, 5))
    f.write("0 0 0 0 1\n")
    f.write("0 1 1 0 2\n")
    f.write("0 2 1 0 0\n")
    f.write("0 0 1 0 0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(3)), 'w') as f:
    f.write("3\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(4)), 'w') as f:
    f.write("{0} {1}\n".format(3, 4))
    f.write("0 0 0 1\n")
    f.write("0 1 2 0\n")
    f.write("0 0 0 0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(4)), 'w') as f:
    f.write("2\n")

# hard tests
with open(os.path.join(tests_dir, '{0:0>2}'.format(5)), 'w') as f:
    f.write("{0} {1}\n".format(98, 98))
    f.write("0 1")
    for i in range(95):
        f.write(" 0")
    f.write(" 2")
    f.write("\n")
    for i in range(97):
        for j in range(97):
            f.write("0 ")
        f.write("0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(5)), 'w') as f:
    f.write("3\n")

# hard tests
with open(os.path.join(tests_dir, '{0:0>2}'.format(6)), 'w') as f:
    f.write("{0} {1}\n".format(50, 50))
    f.write("0 0")
    for i in range(47):
        f.write(" 0")
    f.write(" 2")
    f.write("\n")
    for i in range(49):
        for j in range(49):
            f.write("0 ")
        f.write("0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(6)), 'w') as f:
    f.write("2\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(7)), 'w') as f:
    f.write("{0} {1}\n".format(7, 7))
    f.write("0 0 0 0 1 0 0\n")
    f.write("0 0 0 1 2 0 0\n")
    f.write("0 0 0 0 0 0 0\n")
    f.write("0 0 1 2 0 0 0\n")
    f.write("0 0 0 0 0 1 0\n")
    f.write("0 0 0 1 0 0 0\n")
    f.write("0 0 0 0 0 0 0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(7)), 'w') as f:
    f.write("6\n")

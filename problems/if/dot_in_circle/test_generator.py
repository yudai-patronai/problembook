#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

tests = [(0,  0, 1, "YES"),
         (-1, 3, 1, "NO"),
         (2,  2, 4, "YES"),
         (-3,-5, 2, "NO"),
         (2, -7, 7, "NO"),
         (2, -7, 8, "YES"),
         ]

def generate_test(name, task):
    with open(name, "w") as f:
        f.write(" ".join(map(str, task[:-1])) + '\n')
    with open("%s.a" % name, 'w') as f:
        f.write(task[-1] + '\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test, task in enumerate(tests):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, task)

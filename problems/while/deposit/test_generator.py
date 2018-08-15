#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

tests = [(100, 10, 200, 8),
         (1, 1, 2, 100),
         (50, 30, 20, 0),
         (10, 50, 50, 4),
         (51, 32, 224, 6),
         ]

def generate_test(name, task):
    with open(name, "w") as f:
        f.write(" ".join(map(str, task[:-1])) + '\n')
    with open("%s.a" % name, 'w') as f:
        f.write(str(task[-1]) + '\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test, task in enumerate(tests):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, task)

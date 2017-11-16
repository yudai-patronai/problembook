#!/usr/bin/env python3

import os
from lib import random
import shutil
from solution import solve

random.seed(42)
MAX_N = 50

def generate_test(name, n):
    with open(name, "w") as f:
        f.write(str(n) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(solve(n)))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    questions = random.sample(range(1, MAX_N), 15)
    if MAX_N not in questions:
        questions[-1] = MAX_N

    for test, n in enumerate(questions):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, n)

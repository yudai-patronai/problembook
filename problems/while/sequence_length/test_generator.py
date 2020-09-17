#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

TEST_N = 10


def generate_answer(name, l):
    with open("%s.a" % name, 'w') as f:
        f.write(str(l))


def generate_test(name):
    length = random.randint(1, 100)
    seq = [random.randint(1, 100) for i in range(length)]
    tail = [0] + [random.randint(1, 100) for i in range(random.randint(0, 3))]
    seq += tail
    with open(name, "w") as f:
        for i in seq:
            f.write(str(i) + '\n')
    generate_answer(name, length)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, TEST_N+1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

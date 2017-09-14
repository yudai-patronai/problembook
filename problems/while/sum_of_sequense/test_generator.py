#!/usr/bin/env python3

import os
import random
import shutil

import solution

random.seed(42)


def generate_answer(name, seq):
    with open("%s.a" % name, 'w') as f:
        f.write(str(solution.solve(seq)))


def generate_test(name):
    seq_len = random.randint(1, 1000)
    seq_max = random.randint(5, 1000)
    seq = [random.randint(1, seq_max) for _ in range(seq_len)] + [0]
    with open(name, "w") as f:
        for i in seq:
            f.write(str(i) + '\n')
    generate_answer(name, seq)


if __name__ == "__main__":
    print(111)
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 71):
        print(test)
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

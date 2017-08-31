#!/usr/bin/env python3

import os
import shutil

import solution


def generate_answer(name, n):
    with open("%s.a" % name, 'w') as f:
        f.write(solution.solve(n))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 51):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        with open(test_name, "w") as f:
            f.write(str(test))
        generate_answer(test_name, test)

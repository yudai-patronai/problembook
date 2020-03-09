#!/usr/bin/env python3

import os
from lib import random
import shutil
import heapq

random.seed(42)


def generate_test(name, testn):
    n = random.randint(1, 1000000)
    a = [random.randint(-1000000, 1000000) for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in a:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        heapq.heapify(a)
        f.write(" ".join(map(str, a)))


def write_manual_test(name, n, a):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for i in a:
            f.write(str(i)+"\n")
    with open(name+".a", "w") as f:
        heapq.heapify(a)
        f.write(" ".join(map(str, a)))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    write_manual_test(os.path.join(test_folder, "01"), 5, [8, 6, 1, 5, 2])
    write_manual_test(os.path.join(test_folder, "02"), 3, [6, 7, 3])
    write_manual_test(os.path.join(test_folder, "03"), 7,
                      [18, 1, 8, 0, -1, 7, 6])
    write_manual_test(os.path.join(test_folder, "04"), 1, [5])
    write_manual_test(os.path.join(test_folder, "05"), 7, [-3]*7)
    for test in range(6, 11):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
    write_manual_test(os.path.join(test_folder, "11"), 1000000,
                      [random.randint(-1000000, 1000000)
                       for _ in range(1000000)])
    write_manual_test(os.path.join(test_folder, "12"), 1000000,
                      sorted([random.randint(-1000000, 1000000) for _
                              in range(1000000)]))

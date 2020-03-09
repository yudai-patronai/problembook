#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):
    n = random.randint(1, 100000)
    a = [random.randint(-1000000, 1000000) for _ in range(n)]
    if random.randint(100000) % 2:
        a.sort(reverse=True)
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(" ".join(map(str, a)))
    with open(name+".a", "w") as f:
        for i in reversed(range(1, n)):
            if a[(i-1)//2] < a[i]:
                f.write("NO")
                return
        f.write("YES")


def write_manual_test(name, n, a):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(" ".join(map(str, a)))
    with open(name+".a", "w") as f:
        for i in reversed(range(1, n)):
            if a[(i-1)//2] < a[i]:
                f.write("NO")
                return
        f.write("YES")


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
    write_manual_test(os.path.join(test_folder, "11"), 100000,
                      [random.randint(-1000000, 1000000)
                       for _ in range(100000)])
    write_manual_test(os.path.join(test_folder, "12"), 100000,
                      sorted([random.randint(-1000000, 1000000) for _
                              in range(100000)]))

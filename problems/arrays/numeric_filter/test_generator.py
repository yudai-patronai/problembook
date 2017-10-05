#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)


def generate_test(name, testn):
    n = random.randint(1, 100)
    x = random.randint(1, 1000000)
    seq = [random.randint(1, 1000000) for _ in range(n)]
    ans = []
    for i in range(n):
        if seq[i] % x == 0:
            ans.append(str(i))
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for elem in seq:
            f.write(str(elem)+"\n")
        f.write(str(x))
    with open(name+".a", "w") as f:
        if len(ans):
            f.write(' '.join(ans))
        else:
            f.write("-1")
            

def write_manual_test(name, n, seq, x, ans=[]):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for elem in seq:
            f.write(str(elem)+"\n")
        f.write(str(x))
    with open(name+".a", "w") as f:
        if len(ans):
            f.write(' '.join(ans))
        else:
            f.write("-1")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), 0, [], 12)
    write_manual_test(os.path.join(test_folder, "07"), 100, [random.randint(1, 1000000) for _ in range(100)], 1, [str(i) for i in range(100)])
    write_manual_test(os.path.join(test_folder, "08"), 100, [random.randint(1, 1000000) % 90000 for _ in range(100)], 90000)

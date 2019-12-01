#!/usr/bin/env python3

import os
import shutil
import random

random.seed(42)


def count(s):
    d = [-1 for _ in range(len(s))]
    for i in range(len(s)):
        m = 0
        for j in range(i):
            if s[i] > s[j]:
                m = max(d[j], m)
        d[i] = m + 1
    return max(d)


def generate_test(name, possible=True):
    n = random.randint(1, 100)
    s = [random.randint(0, 1000) for _ in range(n)]
    with open(name, "w") as f:
        f.write(' '.join(map(str, s))+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(s))+"\n")
            

def write_manual_test(name, s):
    with open(name, "w") as f:
        f.write(' '.join(map(str, s))+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(s))+"\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)       
    write_manual_test(os.path.join(test_folder, "01"), [12])
    write_manual_test(os.path.join(test_folder, "02"), [1, 5, 7, 8, 9, 13])
    write_manual_test(os.path.join(test_folder, "03"), [17, 15, 9, 6, 5, 3, 0])
    write_manual_test(os.path.join(test_folder, "04"), [random.randint(0, 1000) for _ in range(100)])
    generate_test(os.path.join(test_folder, "05"))
    generate_test(os.path.join(test_folder, "06"))
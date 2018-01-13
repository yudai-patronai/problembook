#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def count(n, s, w, p, d=None):
    if d is None:
        d = [[-1]*(s+1) for _ in range(n+1)]
    if d[n][s] != -1:
        return d[n][s]
    if not n or not s:
        d[n][s] = 0
        return 0
    if s < w[n-1]:
        d[n][s] = count(n-1, s, w, p, d)
    else:
        d[n][s] = max(count(n-1, s, w, p, d), count(n-1, s-w[n-1], w, p, d) + p[n-1])
    return d[n][s]


def generate_test(name):
    n = random.randint(1, 100)
    s = random.randint(1, 100)
    w = [random.randint(1, 100) for _ in range(n)]
    p = [random.randint(1, 1000) for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(s)+"\n")
        for i in range(n):
            f.write(str(w[i])+"\n")
            f.write(str(p[i])+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(n, s, w, p))+"\n")
            

def write_manual_test(name, n, s, w, p):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(s)+"\n")
        for i in range(n):
            f.write(str(w[i])+"\n")
            f.write(str(p[i])+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(n, s, w, p))+"\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(4, 7):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)    
    write_manual_test(os.path.join(test_folder, "01"), 1, 8, [8], [15])
    write_manual_test(os.path.join(test_folder, "02"), 5, 7, [8, 15, 11, 10, 26], [15, 7, 6, 7, 3])
    write_manual_test(os.path.join(test_folder, "03"), 100, 100, [random.randint(0, 100) for _ in range(100)],
                      [random.randint(0, 1000) for _ in range(100)])
#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def count(n, m, a, d=None):
    if d is None:
        d = [[-1]*(m+1) for _ in range(n+1)]
    if n < 0 or m < 0:
        return 0
    if d[n][m] != -1:
        return d[n][m]
    if a[n][m] == 0:
        d[n][m] = 0
        return 0
    if n == m == 0:
        d[n][m] = 1
        return 1
    d[n][m] = count(n-1, m, a, d) + count(n, m-1, a, d)
    return d[n][m]


def generate_test(name):
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    a = [[[0, 1][random.randint(5)>0] for _ in range(m)] for _ in range(n)]
    a[0][0] = 1
    c = count(n-1, m-1, a)
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in a:
            for j in i:
                f.write(str(j)+"\n")
    with open(name+".a", "w") as f:
        if c > 0:
            f.write(str(c)+"\n")
        else:
            f.write("Impossible\n")
            

def write_manual_test(name, n, m, a):
    a[0][0] = 1
    c = count(n-1, m-1, a)
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in a:
            for j in i:
                f.write(str(j)+"\n")
    with open(name+".a", "w") as f:
        if c > 0:
            f.write(str(c)+"\n")
        else:
            f.write("Impossible\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    """for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)"""        
    write_manual_test(os.path.join(test_folder, "01"), 1, 1, [[1]])
    write_manual_test(os.path.join(test_folder, "02"), 1, 5, [[1, 1, 1, 1, 0]])
    write_manual_test(os.path.join(test_folder, "03"), 4, 5, [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ])
    write_manual_test(os.path.join(test_folder, "04"), 6, 5, [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ])
    write_manual_test(os.path.join(test_folder, "05"), 100, 100, [
        [[0, 1][random.randint(5)>0] for _ in range(100)] for _ in range(100)])
    generate_test(os.path.join(test_folder, "06"))
    generate_test(os.path.join(test_folder, "07"))
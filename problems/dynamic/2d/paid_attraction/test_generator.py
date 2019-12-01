#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def count(n, m, a, d=None):
    if d is None:
        d = [[1000000]*(m+1) for _ in range(n+1)]
    if n < 0 or m < 0:
        return 1000000
    if d[n][m] != 1000000:
        return d[n][m]
    if n == 0 and m == 0:
        d[n][m] = 0
        return 0
    d[n][m] = min(count(n-1, m, a, d), count(n, m-1, a, d)) + a[n][m]
    return d[n][m]


def generate_test(name, possible=True):
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    a = [[random.randint(0, 1000) for _ in range(m)] for _ in range(n)]
    a[0][0] = 0
    c = count(n-1, m-1, a)
    lim = 0
    if possible:
        lim = c + random.randint(50)
    else:
        lim = max(0, c - random.randint(1, 50))
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in a:
            for j in i:
                f.write(str(j)+"\n")
        f.write(str(lim)+"\n")
    with open(name+".a", "w") as f:
        if possible:
            f.write(str(lim-c)+"\n")
        else:
            f.write("Impossible\n")
            

def write_manual_test(name, n, m, a, lim):
    a[0][0] = 0
    c = count(n-1, m-1, a)
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in a:
            for j in i:
                f.write(str(j)+"\n")
        f.write(str(lim)+"\n")
    with open(name+".a", "w") as f:
        if lim >= c:
            f.write(str(lim-c)+"\n")
        else:
            f.write("Impossible\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
            
    write_manual_test(os.path.join(test_folder, "01"), 1, 1, [[0]], 0)
    write_manual_test(os.path.join(test_folder, "02"), 1, 1, [[0]], 12)
    write_manual_test(os.path.join(test_folder, "03"), 4, 5, [
        [0, 5, 2, 4, 1],
        [0, 5, 2, 4, 1],
        [0, 0, 0, 4, 1],
        [0, 5, 0, 0, 0]
    ], 0)
    write_manual_test(os.path.join(test_folder, "04"), 5, 5, [
        [0, 8, 2, 4, 1],
        [8, 8, 0, 4, 1],
        [5, 8, 0, 4, 1],
        [6, 5, 0, 0, 0],
        [6, 5, 4, 5, 0]
    ], 7)
    write_manual_test(os.path.join(test_folder, "05"), 100, 100, [
        [random.randint(1, 100) for _ in range(100)] for _ in range(100)], random.randint(100000))
    generate_test(os.path.join(test_folder, "06"))
    generate_test(os.path.join(test_folder, "07"), False)
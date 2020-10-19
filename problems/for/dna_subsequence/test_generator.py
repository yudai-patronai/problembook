#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def count(s1, s2, d=None):
    if d is None:
        d = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
    if d[len(s1)][len(s2)] != -1:
        return d[len(s1)][len(s2)]
    if not s1 or not s2:
        d[len(s1)][len(s2)] = 0
        return 0
    if s1[-1] == s2[-1]:
        d[len(s1)][len(s2)] = count(s1[:-1], s2[:-1], d) + 1
    else:
        d[len(s1)][len(s2)] = max(count(s1[:-1], s2, d), count(s1, s2[:-1], d))
    if d[len(s1)][len(s2)] == len(s1):
        return "YES"
    else:
        return "NO"


def generate_test(name, possible=True):
    n = random.randint(1, 10000)
    m = random.randint(1, 10000)
    s1 = [random.choice("ACGT") for _ in range(n)]
    s2 = [random.choice("ACGT") for _ in range(m)]
    with open(name, "w") as f:
        f.write(' '.join(s1)+"\n")
        f.write(' '.join(s2)+"\n")
    with open(name+".a", "w") as f:
        f.write(count(s1, s2)+"\n")


def write_manual_test(name, s1, s2):
    with open(name, "w") as f:
        f.write(s1+"\n")
        f.write(s2+"\n")
    with open(name+".a", "w") as f:
        f.write(str(count(s1, s2))+"\n")


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    write_manual_test(os.path.join(test_folder, "01"), "GTA", "AGCTA")
    write_manual_test(os.path.join(test_folder, "02"), "AAAG", "GAAAAAT")
    write_manual_test(os.path.join(test_folder, "03"), "CGT", "ACGT")
    write_manual_test(os.path.join(test_folder, "04"), "GGGG", "GGG")
    write_manual_test(os.path.join(test_folder, "05"), "ACAC", "ACAC")
    for i in range(6, 11):
        generate_test(os.path.join(test_folder, "{:02}".format(i)))

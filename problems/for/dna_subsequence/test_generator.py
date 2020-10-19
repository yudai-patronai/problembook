#!/usr/bin/env python3

import os
import shutil
from lib import random

random.seed(42)


def lcs(A, B):
    N, M = len(A), len(B)
    F = [[0]*(M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                F[i+1][j+1] = F[i][j] + 1
            else:
                F[i+1][j+1] = max(F[i][j+1], F[i+1][j])

    if F[N][M] == N:
        return "YES"
    else:
        return "NO"


def generate_test(name, possible=True):
    n = random.randint(1, 10000)
    m = random.randint(1, 10000)
    s1 = [random.choice("ACGT") for _ in range(n)]
    s2 = [random.choice("ACGT") for _ in range(m)]
    with open(name, "w") as f:
        f.write(''.join(s1)+"\n")
        f.write(''.join(s2)+"\n")
    with open(name+".a", "w") as f:
        f.write(lcs(s1, s2)+"\n")


def write_manual_test(name, s1, s2):
    with open(name, "w") as f:
        f.write(s1+"\n")
        f.write(s2+"\n")
    with open(name+".a", "w") as f:
        f.write(lcs(s1, s2)+"\n")


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
    a = [random.choice("ACGT") for _ in range(9000)]
    b = a.copy()
    for _ in range(500):
        c = random.choice("ACGT")
        p = random.randint(0, len(a) - 1)
        a.insert(p, c)
    write_manual_test(os.path.join(test_folder, "11"), "".join(a), "".join(b))

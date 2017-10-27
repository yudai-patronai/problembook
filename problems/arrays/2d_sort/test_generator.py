#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

def gen_answer(arr):
    replace = -1
    N = len(arr)
    M = len(arr[0])
    while replace != 0:
        replace = 0
        for i in range(N*M-1):
            if arr[i // M][i % M] > arr[(i + 1) // M][(i + 1) % M]:
                arr[i // M][i % M], arr[(i + 1) // M][(i + 1) % M] = arr[(i + 1) // M][(i + 1) % M],
                                                                     arr[i // M][i % M]
                replace += 1

def generate_test(name, testn): 
    n = random.randint(1, 50)
    m = random.randint(1, 50)
    a = [[random.randint(-1000,1000) for k in range(m)] for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in range(n):
            for j in range(m):
                f.write(str(a[i][j]) + '\n')
    with open(name+".a", "w") as f:
        gen_answer(a)
        for i in range(n):
            f.write(' '.join(list(map(str, a[i])))+'\n')

def write_manual_test(name, n, m, a):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        for i in range(n):
            for j in range(m):
                f.write(str(a[i][j]) + '\n')
    with open(name+".a", "w") as f:
        gen_answer(a)
        for i in range(n):
            f.write(' '.join(list(map(str, a[i])))+'\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    write_manual_test(os.path.join(test_folder, "01"), 1, 1, [[5]])
    write_manual_test(os.path.join(test_folder, "02"), 3, 1, [[3],[1],[2]])
    write_manual_test(os.path.join(test_folder, "03"), 1, 3, [[3,1,2]])
    write_manual_test(os.path.join(test_folder, "04"), 3, 3,  [[3,7,1],[5,9,2],[8,4,6]])
    write_manual_test(os.path.join(test_folder, "05"), 3, 1, [[2],[2],[2]])
    write_manual_test(os.path.join(test_folder, "06"), 1, 3, [[2,2,2]])
    
    for test in range(7, 11):
        test_name = os.path.join(test_folder, "%02d" % test)
        generate_test(test_name, test)
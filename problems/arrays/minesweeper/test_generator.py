#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

def place_mine(a, x, y, n, m):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    a[x][y] = -1
    for k in range(8):
        i, j = x+dx[k], y+dy[k]
        if 0 <= i < n and 0 <= j < m and a[i][j] != -1:
            a[i][j] += 1


def generate_test(name, testn): 
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    a = [[0]*m for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            if random.randint(0, 10) == 1:
                k += 1
                place_mine(a, i, j, n, m)
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        f.write(str(k)+"\n")
        for i in range(n):
            for j in range(m):
                if a[i][j] == -1:
                    f.write(str(i+1)+"\n")
                    f.write(str(j+1)+"\n")
    with open(name+".a", "w") as f:
        for i in range(n):
            f.write(' '.join(list(map(str, a[i])))+'\n')
            

def write_manual_test(name, n, m, k, a):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        f.write(str(m)+"\n")
        f.write(str(k)+"\n")
        for i in range(n):
            for j in range(m):
                if a[i][j] == -1:
                    f.write(str(i+1)+"\n")
                    f.write(str(j+1)+"\n")
    with open(name+".a", "w") as f:
        for i in range(n):
            f.write(' '.join(list(map(str, a[i])))+'\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        generate_test(test_name, test)
        
    write_manual_test(os.path.join(test_folder, "06"), 1, 1, 1, [[-1]])
    write_manual_test(os.path.join(test_folder, "07"), 100, 100, 10000, [[-1]*100]*100)
    write_manual_test(os.path.join(test_folder, "08"), 85, 43, 0, [[0]*43]*85)
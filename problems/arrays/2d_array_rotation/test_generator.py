#!/usr/bin/env python3

import os
import shutil
import random

random.seed(42)

def solve(n, seq):
    res = [int((seq[i - 1] + seq[i] + seq[(i + 1) % n]) / 3) for i in range(len(seq))]
    return ' '.join(map(str, res))

def solve(matrix):
    n = len(matrix)
    solution = matrix.copy()
    for i in range(n):
        for j in range(n):
            solution[j][n-i-1] = matrix[i][j]
    return solution

def write_matrix(f, matrix):
    for row in matrix:
        f.write(' '.join([str(elem) for elem in row]))
        f.write('\n')

def generate_answer(name, matrix):
    with open("%s.a" % name, 'w') as f:
        solution = solve(matrix)
        write_matrix(f, solution)

def write_test(name, matrix):
    with open(name, "w") as f:
        n = len(matrix)
        f.write('{}\n'.format(n))
        write_matrix(f, matrix)
    generate_answer(name, matrix)

def generate_test(name, minn=100, maxn=1000):
    n = random.randint(minn, maxn)
    matrix = [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]
    write_test(name, matrix)

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    test_name = os.path.join(test_folder, "%02d" % 1)
    print("generating %s..." % test_name)
    generate_test(test_name, minn=2, maxn=2)

    test_name = os.path.join(test_folder, "%02d" % 2)
    print("generating %s..." % test_name)
    generate_test(test_name, minn=3, maxn=3)

    for test_idx in range(3, 5):
        test_name = os.path.join(test_folder, "%02d" % test_idx)
        print("generating %s..." % test_name)
        generate_test(test_name)


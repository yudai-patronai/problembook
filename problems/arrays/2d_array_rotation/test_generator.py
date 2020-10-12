#!/usr/bin/env python3

from lib.testgen import TestSet
from lib.random import randint, seed


NUM_BYTE_COUNT = 4
MAX_NUMBER = 2 ** (NUM_BYTE_COUNT * 8 - 1) - 1
MIN_NUMBER = -MAX_NUMBER - 1

seed(42)

tests = TestSet()

def solve(matrix):
    n = len(matrix)
    solution = [line[:] for line in matrix]
    for i in range(n):
        for j in range(n):
            solution[j][n-i-1] = matrix[i][j]
    return solution

def print_m(m):
    return '\n'.join(' '.join(map(str, r)) for r in m)

def add(m):
    tests.add('{}\n{}'.format(len(m), print_m(m)), print_m(solve(m)))

def gen_m(size, min_n=MIN_NUMBER, max_n=MAX_NUMBER):
    return [[randint(min_n, max_n) for i in range(size)] for j in range(size)]


gen_m(1)
gen_m(15)
gen_m(15)
gen_m(randint(100, 1000), -1000, 1000)
gen_m(randint(100, 1000), -1000, 1000)
gen_m(20)
gen_m(1024, -1000, 1000)

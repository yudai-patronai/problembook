#!/usr/bin/env python3

import sys
import time

def find_distance(first, second):
    matrix = [[0]*len(second) for i in range(len(first))]
    for i in range(len(first)):
        matrix[i][0] = i
    for j in range(len(second)):
        matrix[0][j] = j

    for i in range(1, len(first)):
        for j in range(1, len(second)):
            matrix[i][j] = min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1, matrix[i - 1][j - 1] + (0 if first[i] == second[j] else 1))
    return matrix[-1][-1]


if __name__ == "__main__":
    start = time.time()
    first = input()
    second = input()
    print(find_distance(first, second))
    end = time.time()
    print(end-start, file=sys.stderr)

#!/usr/bin/env python3
def count_edges(matrix):
    n = len(matrix)
    n_edge = 0
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] == 1:
                n_edge += 1
    return n_edge


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(count_edges(matrix))

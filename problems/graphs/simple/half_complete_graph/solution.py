#!/usr/bin/env python3

def check_halp_complete(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] + matrix[j][i] == 0:
                return False 
    return True


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    for i in range(m):
        v1, v2 = map(int, input().split())
        matrix[v1][v2] = 1
    if check_halp_complete(matrix):
        print('YES')
    else:
        print('NO')


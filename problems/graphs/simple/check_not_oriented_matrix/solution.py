#!/usr/bin/env python3
def check_correct(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    if check_correct(matrix):
        print('YES')
    else:
        print('NO')


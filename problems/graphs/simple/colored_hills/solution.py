#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    _ = input()
    colors = list(map(int, input().split()))

    bad = 0
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == 1 and colors[i] != colors[j]:
                bad += 1

    print(bad)

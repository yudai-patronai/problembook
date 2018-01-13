#!/usr/bin/env python3


def solve(n):
    if n == 0:
        return 1
    arr = [[0] * 3 for _ in range(n+1)]
    arr[1][0] = 1
    arr[1][1] = 1
    arr[1][2] = 1

    for i in range(2, n+1):
        arr[i][0] = arr[i][1] = arr[i - 1][0] + arr[i - 1][1] + arr[i - 1][2]
        arr[i][2] = arr[i - 1][0] + arr[i - 1][1]
    return sum(arr[n])

if __name__ == "__main__":
    n = int(input())
    print(solve(n))

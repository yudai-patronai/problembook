#!/usr/bin/env python3


def solve(n):
    if n % 2 != 0:
        return 0

    a = [0] * n
    b = [0] * n

    a[1] = 3
    b[1] = 1

    for i in range(2, n):
        b[i] = a[i - 2] + b[i - 2]
        a[i] = a[i - 2] * 2 + b[i - 2] + b[i]

    return a[n - 1]


print(solve(int(input())))

#!/usr/bin/env python3


def solve(k, p):
    if k == 0 or k == 1:
        return 0
    arr = [0] * (k+1)
    arr[2] = 1

    for i in range(3, k+1):
        if not i % 2:
            arr[i] = (arr[i - 1] + arr[i//2]) % p
        else:
            arr[i] = arr[i-1] % p
    return arr[k]


if __name__ == "__main__":
    k = int(input())
    p = int(input())
    print(solve(k, p))

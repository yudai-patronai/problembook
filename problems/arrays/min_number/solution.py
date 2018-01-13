#!/usr/bin/env python3


def solve(n):
    arr = [0] * 10
    while n:
        arr[n % 10] += 1
        n //= 10

    res = ''

    for j in range(sum(arr)):
        for i in range(10):
            if j == 0 and i == 0:
                continue
            if arr[i]:
                res += str(i)
                arr[i] -= 1
                break

    return int(res)


if __name__ == "__main__":
    print(solve(int(input())))

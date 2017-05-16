#!/usr/bin/env python3


def solve(N,K):
    A = [i + 1 for i in range(N)]
    last = 0
    while len(A) > 1:
        last = (last + K - 1) % len(A)
        A.pop(last)
    return(A[0])


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(solve(x, y))

#!/usr/bin/env python3


def solve(n):
    triangle = '1\n'
    A = []
    for _ in range(n):
        B = [1] + [A[i - 1] + A[i] for i in range(1, len(A))] + [1]
        triangle += " ".join(map(str, B)) + "\n"
        A = B
    return triangle


if __name__ == "__main__":
    print(solve(int(input())))

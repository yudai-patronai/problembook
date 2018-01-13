#!/usr/bin/env python3

def solve(n):
    turtles = []

    for i in range(n):
        a, b = map(int, input().split())
        if (a >= 0 or b >= 0) and a + b == n - 1 and (abs(a) < n and abs(b) < n) and a not in turtles:
            turtles.append(a)

    return len(turtles)


if __name__ == "__main__":
    n = int(input())

    print(solve(n))

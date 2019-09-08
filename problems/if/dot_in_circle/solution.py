#!/usr/bin/env python3


def solve(x, y, r):
    return "YES" if (x*x + y*y)**0.5 <= r else "NO"


if __name__ == "__main__":
    x, y, r = map(int, input().split())
    print(solve(x, y, r))

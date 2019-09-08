#!/usr/bin/env python3


def solve(x, p, y):
    years = 0
    while x < y:
        x += x * p / 100
        x = (x * 100) // 1 / 100
        years += 1

    return years


if __name__ == "__main__":
    x, p, y = map(int, input().split())
    print(solve(x, p, y))

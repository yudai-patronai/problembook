#!/usr/bin/env python3

import sys
import time


def compute_z_function(s):
    z = [0]
    left = right = 0
    for i in range(1, len(s)):
        x = min(z[i - left], right - i + 1) if i <= right else 0
        while i + x < len(s) and s[x] == s[i + x]:
            x += 1
        if i + x - 1 > right:
            left, right = i, i + x - 1
        z.append(x)
    return z


def check(first, second):
    z = compute_z_function(second + "#" + first + first)
    for i, v in enumerate(z):
        if v == len(second):
            return i - len(second) - 1
    return -1


if __name__ == "__main__":
    start = time.time()
    first = input()
    second = input()
    print(check(first, second))
    end = time.time()

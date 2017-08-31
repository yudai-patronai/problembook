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


if __name__ == "__main__":
    start = time.time()
    pattern = input()
    text = input()
    z = compute_z_function(pattern + "#" + text)
    meets = []
    for i, v in enumerate(z):
        if v == len(pattern):
            meets.append(i - len(pattern) - 1)
    if meets:
        print(" ".join(map(str, meets)))
    else:
        print("-1")
    end = time.time()
    print(end - start, file=sys.stderr)

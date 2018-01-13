#!/usr/bin/env python3

import sys


def prefix_function(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        common = p[i - 1]
        while common != 0 and s[common] != s[i]:
            common = p[common - 1]
        if s[common] == s[i]:
            common += 1
        p[i] = common
    return p


if __name__ == "__main__":
    print(" ".join(map(str, prefix_function(input()))))

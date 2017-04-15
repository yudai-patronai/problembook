#!/usr/bin/env python3

import sys


def compute_prefix_function(s):
    prefix_function = [0] * len(s)
    for i in range(1, len(s)):
        common = prefix_function[i - 1]
        while common != 0 and s[common] != s[i]:
            common = prefix_function[common - 1]
        if s[common] == s[i]:
            common += 1
        prefix_function[i] = common
    return prefix_function


def check_prefix(s, prefix_function):
    assert len(prefix_function) == len(s)
    if len(s) > 0:
        assert prefix_function[0] == 0
    for i in range(len(s)):
        assert prefix_function[i] <= i
        assert s[i - prefix_function[i] + 1: i+1] == s[0:prefix_function[i]]


if __name__ == "__main__":
    s = input()
    prefix = compute_prefix_function(s)
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        check_prefix(s, prefix)
    print(" ".join(map(str, prefix)))

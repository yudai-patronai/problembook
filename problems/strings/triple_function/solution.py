#!/usr/bin/env python3


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


def compute_b_function(s):
    p = compute_prefix_function(s)
    b = []
    m = 0
    for i in p:
        if m >= i:
            b.append(i)
        else:
            b.append(p[i - 1])
        m = max(i, m)
    return b


if __name__ == "__main__":
    s = input()
    print(" ".join(map(str, compute_b_function(s))))

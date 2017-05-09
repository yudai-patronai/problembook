#!/usr/bin/env python3

def compute_z_function(s):
    z = [0] * len(s)
    for i in range(1, len(s)):
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z


def find_a_function(s):
    x = s + "#" + s[::-1]
    z = compute_z_function(x)
    return z[:-len(s) - 1:-1]


if __name__ == "__main__":
    x = input()
    s = input()
    print(" ".join(map(str, find_a_function(s))))

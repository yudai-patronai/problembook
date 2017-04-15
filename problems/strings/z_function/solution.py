#!/usr/bin/env python3

import sys

def compute_z_function(s):
    z = [0]
    left = right = 0
    for i in range(1, len(s)):
        x = min(z[i-left], right - i + 1) if i <= right else 0
        while i+x < len(s) and s[x] == s[i+x]:
            x += 1
        if i + x - 1 > right:
            left, right = i, i + x - 1
        z.append(x)
    return z

def slow_z_function(s):
    z = [0] * len(s)
    for i in range(1, len(s)):
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z


if __name__ == "__main__":
    string = input()
    z = compute_z_function(string)
    if len(sys.argv) >= 2 and sys.argv[1] == "test" and len(string) <= 1000:
        slow_z = slow_z_function(string)
        assert z == slow_z, "%s : %s != %s" % (string, z, slow_z)
    print(" ".join(map(str, z)))

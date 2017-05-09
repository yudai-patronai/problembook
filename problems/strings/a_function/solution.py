#!/usr/bin/env python3

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


def find_a_function(s):
    x = s + "#" + s[::-1]
    z = compute_z_function(x)
    return z[:-len(s) - 1:-1]


if __name__ == "__main__":
    x = input()
    s = input()
    print(" ".join(map(str, find_a_function(s))))

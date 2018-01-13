#!/usr/bin/env python3


def z_function(s):
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
    print(*z_function(input()))

#!/usr/bin/env python3


def find_palindroms(string):
    left = right = 0
    n = len(string)
    p = [0] * n
    for i in range(1, n):
        if i <= right:
            p[i] = min(right - i, p[left + right - i])
        while p[i] < i and i + p[i] + 1 < n and\
                string[i - p[i] - 1] == string[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > right:
            left = i - p[i]
            right = i + p[i]
    for i in range(n):
        p[i] = p[i] * 2 + 1
    return p


if __name__ == "__main__":
    string = input()
    print(" ".join(map(str, find_palindroms(string))))

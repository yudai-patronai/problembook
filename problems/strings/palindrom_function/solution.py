#!/usr/bin/env python3

def find_palindroms(string):
    l = 0
    r = 0
    p = [0] * len(string)
    for i in range(1, len(string)):
        if r < i:
            p[i] = 0
        else:
            j = l + r - i
            p[i] = min(r - i, p[j])
        while p[i] < i and i + p[i] + 1 < len(string) and string[i - p[i] - 1] == string[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > r:
            l = i - p[i]
            r = i + p[i]
    for i in range(len(p)):
        p[i] = p[i] * 2 + 1
    return p


if __name__ == "__main__":
    string = input()
    print(" ".join(map(str, find_palindroms(string))))

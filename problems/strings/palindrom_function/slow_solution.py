#!/usr/bin/env python3

def find_palindroms(s):
    p = []
    for i in range(len(s)):
        q = 0
        while q < i and i + q + 1 < len(s) and s[i - q - 1] == s[i + q + 1]:
            q += 1
        p.append(q * 2 + 1)
    return p


if __name__ == "__main__":
    string = input()
    print(" ".join(map(str, find_palindroms(string))))

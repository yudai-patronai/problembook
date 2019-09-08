#!/usr/bin/env python3


def solve(word):
    vowel = 'aeiouy'
    pal = ''
    for c in word:
        if c not in vowel:
            pal += c

    return 'YES' if pal == pal[::-1] else 'NO'


if __name__ == "__main__":
    print(solve(input()))

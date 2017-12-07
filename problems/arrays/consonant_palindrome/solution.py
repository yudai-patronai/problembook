#!/usr/bin/env python3

def solve(word):
    vowel = 'aeiouy'
    pal = ''
    for c in word:
        if c not in vowel:
            pal += c

    if pal == pal[::-1]:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    print(solve(input()))

#!/usr/bin/env python3

from lib import random
import string
from lib.testgen import TestSet

ALPHABET = list(string.ascii_letters)


def compute_z_function(s):
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


def find_a_function(s):
    x = s + "#" + s[::-1]
    z = compute_z_function(x)
    return z[:-len(s) - 1:-1]


def generate_simple(pal, letters, l):
    s = []
    step = 1
    pal = list(pal)
    status = 0
    while len(s) < l:
        s += pal
        if status == 0:
            step = 1
        if status + 1 == len(letters):
            step = -1
        s.append(letters[status])
        status += step
    return ''.join(s[:l])


def question(t):
    return t[0]


def answer(t):
    res = find_a_function(t[0])
    assert len(t) != 0 or res != t[1], 'Answers {} and {} do not match'.format(res, t[1])
    return '{}\n'.format(' '.join(map(str, res)))


TESTS = TestSet()
def add_test(t):
    TESTS.add(question(t), answer(t))


if __name__ == "__main__":
    random.seed(42)
    tests = [
        ("abcd", [1, 0, 0, 0]),
        ("aba", [1, 0, 3]),
        ("ababa", [1, 0, 3, 0, 5]),
        ("abcbacba", [1, 0, 0, 0, 5, 0, 0, 3]),
        ("abcb" * 10 + "a",),
        ("abcb" * 10 + "abc",),
        ("hellolloh" + "abracad" * 14 + "olloh",),
        ("a" * 97,),
        ("abcb" * 20,),
        ("abababcb" * 17,),
        ("gurugugu" * 13,),
        (generate_simple("a", "xyz", 100),),
        (generate_simple("abcba", "xyzyxyz", 534),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "kixyzki", 16543),),
        ("a" * 20000,),
        ("abracadabr" * 23,),
        ("abracadabracad" * 23,),
        ("ab" * 10000,),
        ("abcb" * 2000,),
        ("abababcb" * 2240,),
        ("gurugugu" * 2000,),
        (generate_simple("a", "xyz", 2000),),
        (generate_simple("aba", "xyz", 18000),),
        (generate_simple("abcba", "xyzyxyz", 18000),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "kixyzki", 18000),),
        (generate_simple(generate_simple(generate_simple("aba", "abcdef", 16 + 17 * 3), "xyz", 5 + 6 * (16 + 17 * 3)),
                         "kixyzki", 18000),),
    ]

    for t in tests:
        add_test(t)

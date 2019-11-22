#!/usr/bin/env python3

from lib import random
import string
from lib.testgen import TestSet

ALPHABET = list(string.ascii_lowercase)


def compute_z_function(s):
    z = [0] * len(s)
    left = right = 0
    for i in range(1, len(s)):
        x = min(z[i - left], right - i + 1) if i <= right else 0
        while i + x < len(s) and s[x] == s[i + x]:
            x += 1
        if i + x - 1 > right:
            left, right = i, i + x - 1
        z[i] = x
    return z


def kmp(pattern, text):
    z = compute_z_function(pattern + "#" + text)
    meets = []
    for i, v in enumerate(z):
        if v == len(pattern):
            meets.append(i - len(pattern) - 1)
    return meets


def generate_random_string(n, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(n))


def question(t):
    return '\n'.join(t)


def answer(t):
    res = kmp(*t)
    return '{}\n'.format(-1 if not res else ' '.join(map(str, res)))


TESTS = TestSet()
def add_test(t):
    TESTS.add(question(t), answer(t))


def generate_random_test(p, n, a, seed):
    alphabet = random.sample(ALPHABET, a)
    random.seed(seed + "_random")
    return (
        generate_random_string(p, alphabet),
        generate_random_string(n, alphabet)
    )


def generate_at_least_once_test(p, n, a, seed):
    alphabet = random.sample(ALPHABET, a)
    random.seed(seed + "at_least")
    x = generate_random_string(n, alphabet)
    a = random.randint(0, n - p)
    b = a + p
    return (x[a:b], x)


if __name__ == "__main__":
    tests = [
        ["aaa", "aaaaa"],
        ["abc", "abdcab"],
        ["ababa", "abababababa"]
    ]
    for n in [10, 50, 1000, 10000]:
        ps = [3, 5, 9]
        if n > 1000:
            ps += [100, 1000]
        if n > 10000:
            ps += [20000, 100000]
        for p in ps:
            for a in [26]:
                seed = "%d_%d_%d" % (p, n, a)
                tests.append(generate_random_test(p, n, a, seed))
                tests.append(generate_at_least_once_test(p, n, a, seed))
    tests += [
        generate_random_test(10, 100, 1, "abc"),
        generate_random_test(5, 100, 3, "asdf"),
        generate_random_test(10, 10000, 2, "fdst"),
        generate_random_test(1, 10000, 3, "gf234d"),
        generate_random_test(5, 10000, 3, "gfsd"),
        generate_random_test(1, 10000, 1, "asdfgsdf"),
    ]
    for t in tests:
        add_test(t)

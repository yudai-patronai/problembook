#!/usr/bin/env python3

import os
from lib import random
import shutil
import string
import subprocess as sp

ALPHABET = list(string.ascii_lowercase)


def generate_random_string(n, alphabet):
    s = []
    for i in range(n):
        s.append(random.choice(alphabet))

    return "".join(s)


def find_shift_slow(s, t):
    n = len(s)
    for i in range(n):
        if s == t:
            return i
        s = s[1:] + s[0]
    return -1


def prepare_test(i, t, folder):
    filename = os.path.join(folder, "%02d" % i)
    with open(filename, "w") as f:
        print(t[0], file=f)
        print(t[1], file=f)

    with open(filename) as f:
        with open("%s.a" % filename, "w") as g:
            g.write("%d\n" % find_shift_slow(*t))


def generate_random_test(n, a, seed):
    alphabet = random.sample(ALPHABET, a)
    random.seed(seed + "_random")
    return (
        generate_random_string(n, alphabet),
        generate_random_string(n, alphabet)
    )


def generate_simple_test(n, a, seed):
    alphabet = random.sample(ALPHABET, a)
    random.seed(seed + "single")
    x = generate_random_string(n, alphabet)
    n = random.randint(0, n - 1)
    y = x[n:] + x[:n]
    return (x, y)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    tests = [
        ["aaaaa", "aaaaa"],
        ["abcdef", "cdefab"],
        ["abcdea", "bcdeab"]
    ]
    for n in [10, 10000, 150000]:
        for s in [2, 15]:
            seed = "%d_%d" % (n, s)
            tests.append(generate_random_test(n, s, seed))
        for s in [2, 3, 5, 10]:
            seed = "%d_%d" % (n, s)
            tests.append(generate_simple_test(n, s, seed))

    for i, t in enumerate(tests):
        prepare_test(i + 1, t, test_folder)

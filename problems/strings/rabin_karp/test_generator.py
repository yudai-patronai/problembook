#!/usr/bin/env python3

import os
from lib import random
import shutil
import string
import subprocess as sp

ALPHABET = list(string.ascii_letters)


def generate_random_string(n, alphabet):
    s = []
    for i in range(n):
        s.append(random.choice(alphabet))

    return "".join(s)


def prepare_test(i, t, folder):
    filename = os.path.join(folder, "%02d" % i)
    with open(filename, "w") as f:
        print(t[0], file=f)
        print(t[1], file=f)

    with open(filename) as f:
        with open("%s.a" % filename, "w") as g:
            sp.check_call(["./kmp_solution.py", "test"], stdin=f, stdout=g)


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
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

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
        generate_random_test(10, 100000, 2, "fdst"),
        generate_random_test(1, 100000, 3, "gf234d"),
        generate_random_test(5, 100000, 3, "gfsd"),
        generate_random_test(1, 100000, 1, "asdfgsdf"),
    ]
    for i, t in enumerate(tests):
        prepare_test(i + 1, t, test_folder)

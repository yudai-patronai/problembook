#!/usr/bin/env python3

import os
import random
import shutil
import string
import subprocess as sp

ALPHABET = list(string.ascii_lowercase)


# it could be not best prefix!
# sometimes it could broke
def get_random_almost_prefix_function(b, l, p, seed):
    random.seed(seed)
    prefix = [0] * b
    for i in range(b, l):
        if random.random() < p:
            prefix.append(0)
        else:
            if random.random() < 0.5:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(random.randint(1, prefix[-1] + 1))
    return prefix


def find_appropriate_string(prefix, seed):
    alphabet = ALPHABET[:]
    random.seed(seed)
    random.shuffle(alphabet)
    s = [alphabet[0]]
    next_char = 1
    for i in range(1, len(prefix)):
        if prefix[i] == 0:
            s.append(alphabet[next_char])
            next_char += 1
        else:
            s.append(s[prefix[i] - 1])
    assert len(s) == len(prefix)
    return "".join(s)


def generate_test(i, t, folder):
    filename = os.path.join(folder, "%02d" % i)
    with open(filename, "w") as f:
        print(t[0], file=f)

    with open(filename) as f:
        with open("%s.a" % filename, "w") as g:
            sp.check_call(["./solution.py", "test"], stdin=f, stdout=g)
            # with open("%s.a" % filename) as f:
            #     answer = list(map(int, f.readline().split()))
            # assert t[1] == answer, "%s: %s != %s" % (t[0], t[1], answer)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    tests = [
        ["aaaa", [0, 1, 2, 3]],
        ["ababcabd", [0, 0, 1, 2, 0, 1, 2, 0]],
        ["abcdddabce", [0, 0, 0, 0, 0, 0, 1, 2, 3, 0]]
    ]
    for l in [10, 50]:
        for s in [5, 10]:
            for b in [1, 3, 5]:
                prefix = get_random_almost_prefix_function(b, l, s * 1.0 / l, "%d_%d_%d_prefix" % (b, l, s))
                string = find_appropriate_string(prefix, "%d_%d_%d_shuffle" % (b, l, s))
                tests.append([string, prefix])

    for l in [100, 500, 1000, 10000, 100000, 100000, 100000, 100000]:
        s = 10
        for b in [5, 7, 12]:
            prefix = get_random_almost_prefix_function(b, l, s * 1.0 / l, "%d_%d_%d_prefix" % (b, l, s))
            string = find_appropriate_string(prefix, "%d_%d_%d_shuffle" % (b, l, s))
            tests.append([string, prefix])

    for i, t in enumerate(tests):
        generate_test(i + 1, t, test_folder)

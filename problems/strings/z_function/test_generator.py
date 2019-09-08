#!/usr/bin/env python3

# copy pasted from prefix_function :-)

import os
from lib import random
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

    with open("%s.a" % filename, "w") as f:
        print(*t[1], file=f)    


def slow_z_function(s):
    z = [0]
    for i in range(1, len(s)):
        x = 0
        while i + x < len(s) and s[x] == s[i + x]:
            x += 1
        z.append(x)
    return z


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    tests = [
        ["aaaa", slow_z_function("aaaa")],
        ["ababcabd", slow_z_function("ababcabd")],
        ["abcdddabce", slow_z_function("abcdddabce")]
    ]
    for l in [10, 50]:
        for s in [5, 10]:
            for b in [1, 3, 5]:
                prefix = get_random_almost_prefix_function(b, l, s * 1.0 / l, "%d_%d_%d_prefix_" % (b, l, s))
                string = find_appropriate_string(prefix, "%d_%d_%d_shuffle_" % (b, l, s))
                z = slow_z_function(string)
                tests.append([string, z])

    for l in [1000, 10000, 100000]:
        s = 10
        for b in [5, 7, 12]:
            prefix = get_random_almost_prefix_function(b, l, s * 1.0 / l, "%d_%d_%d_prefix_" % (b, l, s))
            string = find_appropriate_string(prefix, "%d_%d_%d_shuffle_" % (b, l, s))
            z = slow_z_function(string)
            tests.append([string, z])

    s = "a" * (100000 - 10) + "z" + "a" * 9
    z = [0] + [i for i in range(100000 - 11, 0, -1)] + [0] + [i for i in range(9, 0, -1)]
    tests.append([s, z])

    for i, t in enumerate(tests):
        generate_test(i + 1, t, test_folder)

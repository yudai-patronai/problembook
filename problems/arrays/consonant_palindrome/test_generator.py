#!/usr/bin/env python3

import os
from lib import random
import shutil
import string

vowel = 'aeiouy'
consonant = [c for c in string.ascii_lowercase if c not in vowel]

random.seed(42)

manual_tests = [
    ('tennete', 'YES'),
    ('sos', 'YES'),
    ('student', 'NO'),
    ('w', 'YES'),
    ('a', 'YES'),
]

def generate_manual_test(name, task):
    word = task[0]
    ans = task[1]
    with open(name, "w") as f:
        f.write(word + '\n')
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(ans + '\n')


def makePalindrome(n):
    half = [random.choice(consonant) for _ in range(n // 2)]
    p = half + ([random.choice(consonant)] if n % 2 else []) + half[::-1]
    return p


def insert_vowel(p):
    nv = random.randint(0, len(p))
    for _ in range(nv):
        p.insert(random.randint(0, len(p)-1), random.choice(vowel))


def generate_test(name, n=None, ans=None):
    if not n:
        n = random.randint(10, 40)
    p = makePalindrome(n)
    if not ans:
        ans = "YES" if random.random() > 0.5 else "NO"

    if ans == 'NO':
        p = p[:-random.randint(2, n // 3)]
    insert_vowel(p)
    with open(name, "w") as f:
        f.write(''.join(p) + '\n')
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(ans + '\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual_tests) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test-1])

    #random tests
    for test in range(len(manual_tests) + 1, len(manual_tests) + 7):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

    # big tests
    test_name = os.path.join(test_folder, "%02d" % (test + 1))
    print("generating %s..." % test_name)
    generate_test(test_name, 90, "YES")

    test_name = os.path.join(test_folder, "%02d" % (test + 2))
    print("generating %s..." % test_name)
    generate_test(test_name, 100, "NO")

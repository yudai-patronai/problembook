#!/usr/bin/env python3

import os
import random
import shutil
import string

import solution

random.seed(42)

manual_tests = [("aaaaa", 5),
                ("abcabcabc", 3),
                ("abab", 2),
                ("asd", 1)]

def generate_manual_test(name, t):
    with open(name, "w") as f:
        f.write(t[0] + '\n')
    with open("%s.a" % name, 'w') as f:
        f.write(str(t[1]))

def generate_test(name, big = False):
    l = random.randint(5, 10)
    if big:
        l = 10**6
    small_letters = string.ascii_lowercase
    s = ""
    for i in range(l):
        s += random.choice(small_letters)

    if not big and random.random() < 0.5:
        s = s*random.randint(2, 20)

    with open(name, "w") as f:
        f.write(s + '\n')
    with open("%s.a" % name, 'w') as f:
        f.write(str(solution.solve(s)))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual_tests)):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test - 1])

    for test in range(len(manual_tests), len(manual_tests) + 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

    test += 1
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    generate_test(test_name, True)

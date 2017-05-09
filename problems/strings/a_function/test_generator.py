#!/usr/bin/env python3

import shutil
import string
import os
import random
import solution
import slow_solution

ALPHABET = list(string.ascii_letters)


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
    return "".join(s[:l])


def generate_test(n, t, folder):
    src = os.path.join(folder, "%02d" % n)
    dst = os.path.join(folder, "%02d.a" % n)
    with open(src, "w") as f:
        f.write(t[0])
    answer = solution.find_a_function(t[0])
    if len(t) >= 2:
        assert answer == t[1], n
    if len(t[0]) < 1000:
        assert answer == slow_solution.find_a_function(t[0]), n
    with open(dst, "w") as g:
        print(" ".join(map(str, answer)), file=g)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    random.seed(42)
    tests = [
        ("aabaa", [1, 2, 0, 1, 5]),
        ("abcd", [1, 0, 0, 0]),
        ("aba", [1, 0, 3]),
        ("ababa", [1, 0, 3, 0, 5]),
        ("abcbacba", [1, 0, 0, 0, 5, 0, 0, 3]),
        ("abcb" * 10 + "a",),
        ("abcb" * 10 + "ab",),
        ("abcb" * 10 + "abc",),
        ("abracad" * 14,),
        ("hellolloh" + "abracad" * 14 + "olloh",),
        ("a" * 97,),
        ("ab" * 50,),
        ("abcb" * 20,),
        ("abababcb" * 17,),
        ("gurugugu" * 13,),
        (generate_simple("a", "xyz", 100),),
        (generate_simple("abcba", "xyzyxyz", 534),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "xyzyxyz", 1450),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "kixyzki", 16543),),
        ("a" * 10000,),
        ("abracadabr" * 23,),
        ("abracadabracad" * 23,),
        ("a" * 200000,),
        ("ab" * 50000,),
        ("abcb" * 20000,),
        ("abababcb" * 22400,),
        ("gurugugu" * 20000,),
        (generate_simple("a", "xyz", 2000),),
        (generate_simple("aba", "xyz", 20000),),
        (generate_simple("abcba", "xyzyxyz", 200000),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "xyzyxyz", 200000),),
        (generate_simple(generate_simple("iki", "xyz", 5 + 6 * 3), "kixyzki", 200000),),
        (generate_simple(generate_simple(generate_simple("aba", "abcdef", 16 + 17 * 3), "xyz", 5 + 6 * (16 + 17 * 3)), "kixyzki", 200000),),
    ]

    for i, t in enumerate(tests):
        generate_test(i + 1, t, test_folder)

#!/usr/bin/env python3


import os
from lib import random
import shutil
from string import ascii_lowercase
from lib.testgen import TestSet


NUM_RAND_TESTS = 10
MAX_STR_LEN = 500
random.seed(100)

def find_distance(first, second):
    matrix = [[0] * (len(second) + 1) for i in range(len(first) + 1)]
    for i in range(len(first) + 1):
        matrix[i][0] = i
    for j in range(len(second) + 1):
        matrix[0][j] = j

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            matrix[i][j] = min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1,
                               matrix[i - 1][j - 1] + (0 if first[i - 1] == second[j - 1] else 1))
    return matrix[-1][-1]


def get_case(str1, str2):
    return '{}\n{}'.format(str1, str2), str(find_distance(str1, str2))


tests = TestSet()

tests.add(*get_case("aaaaa", "aaaaa"))
tests.add(*get_case("abcdef", "cdefab"))
tests.add(*get_case("abcdea", "bcdeab"))

for _ in range(NUM_RAND_TESTS):
    # use random.choice instead of random.smaple cause MAX_STR_LEN > len(ascii_lowercase)
    str1 = ''.join([random.choice(ascii_lowercase) for _ in range(random.randint(1, MAX_STR_LEN))])
    str2 = ''.join([random.choice(ascii_lowercase) for _ in range(random.randint(1, MAX_STR_LEN))])

    tests.add(*get_case(str1, str2))

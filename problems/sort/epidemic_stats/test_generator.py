#!/usr/bin/python3

from lib.testgen import TestSet
from lib import random

tests = TestSet()

# Some basic tests
tests.add(
"""40 1
32 2
32 1
50 2
32 0
60 0
0 3""",
"""32 50
50 100
60 0"""
)

tests.add(
"""50 2
0 3""",
"""50 100"""
)

tests.add(
"""99 0
33 1
1 2
0 3""",
"""1 100
99 0"""
)

# Some random tests
def gen_random_set(N):
    d = [0] * 100
    r = [0] * 100
    strin = ""
    strout = ""

    for i in range(N):
        row = (random.randint(1, 99), random.randint(0, 2))
        strin = strin + "{} {}\n".format(row[0], row[1])
        if row[1] == 0:
            d[row[0]] += 1
        elif row[1] == 2:
            r[row[0]] += 1

    strin = strin + "0 3\n"

    for i in range(100):
        if d[i]!=0 or r[i]!=0:
            strout = strout + "{} {}\n".format(i, round(100.0 * r[i] / (d[i] + r[i])))

    tests.add(strin, strout)

gen_random_set(30)
gen_random_set(500)
gen_random_set(1000)
gen_random_set(3000)
gen_random_set(10000)


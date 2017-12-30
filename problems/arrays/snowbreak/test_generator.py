#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

manual_tests = [
    {"task": [-20, 30, -40, 50, 10, -10],
     "ans": 2},

    {"task": [10, 20, 30, 1, -10, 1, 2, 3],
     "ans": 4},

    {"task": [-10, 0, -10, 0, -10],
     "ans": 0},

    {"task": [10, 5, 3, 20],
     "ans": 4},

    {"task": [-20, 0, -1, -2, -23],
     "ans": 0},

    {"task": [30],
     "ans": 1},
]

def generate_manual_test(name, task):
    n = len(task["task"])
    temp = task["task"]
    ans = task["ans"]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, temp)) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))

def generate_test(name, n=None, maxStreakLen=None):
    if not n:
        n = random.randint(20, 30)

    num_pos_streaks = random.randint(1, 5)

    if not maxStreakLen:
        maxStreakLen = n // (num_pos_streaks * 2)

    len_pos_streaks = [random.randint(1, maxStreakLen) for _ in range(num_pos_streaks)]
    len_neg_streaks = [random.randint(1, maxStreakLen) for _ in range(num_pos_streaks-1)]

    temps = []
    #first is negative
    if random.random() > 0.5:
        temps.extend([random.randint(-50, 0) for _ in range(random.randint(1, maxStreakLen))])

    neg = lambda: random.randint(-50, 0)
    pos = lambda: random.randint(1, 50)

    for i in range(num_pos_streaks-1):
        temps.extend([pos() for _ in range(len_pos_streaks[i])])
        temps.extend([neg() for _ in range(len_neg_streaks[i])])

    temps.extend([pos() for _ in range(len_pos_streaks[-1])])
    temps.extend([neg() for _ in range(n - len(temps))])

    with open(name, "w") as f:
        f.write(str(n) + '\n')
        f.write(' '.join(map(str, temps)) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(max(len_pos_streaks)))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, len(manual_tests) + 1):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_manual_test(test_name, manual_tests[test-1])

    #random tests
    for test in range(len(manual_tests) + 1, len(manual_tests) + 4):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

    #big tests
    test_name = os.path.join(test_folder, "%02d" % (test + 1))
    print("generating %s..." % test_name)
    generate_test(test_name, 90)

    test_name = os.path.join(test_folder, "%02d" % (test + 2))
    print("generating %s..." % test_name)
    generate_test(test_name, 100, 20)

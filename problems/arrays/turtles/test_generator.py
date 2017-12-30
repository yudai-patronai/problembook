#!/usr/bin/env python3

import os
from lib import random
import shutil

random.seed(42)

manual_tests = [
    {"task": [(2, 0), (0, 2), (2, 2)],
     "ans": 2},

    {"task": [(2, 2), (1, 2)],
     "ans": 0},

    {"task": [(0, 1), (1, 0)],
     "ans": 2},
]

def generate_manual_test(name, task):
    turtles = task["task"]
    n = len(turtles)
    ans = task["ans"]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for pair in turtles:
            f.write(' '.join(map(str, pair)) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))

def generate_test(name, n=None):
    if not n:
        n = random.randint(5, 50)

    ans = random.randint(0, n)

    #don't lie
    infront = random.sample(range(0, n), ans)
    turtles = [(a, n - 1 - a) for a in infront]

    #those, who lie
    for _ in range(n - ans):
        if random.random() > 0.5 and ans:
            rnd = random.choice(turtles)
            turtles.append(rnd)
        else:
            a = random.randint(-n, n)
            b = n - 1 - a + random.randint(1, n)
            turtles.append((a, b))

    random.shuffle(turtles)
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for pair in turtles:
            f.write(' '.join(map(str, pair)) + '\n')
    # answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))


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

    #big tests
    test_name = os.path.join(test_folder, "%02d" % (test + 1))
    print("generating %s..." % test_name)
    generate_test(test_name, 900)

    test_name = os.path.join(test_folder, "%02d" % (test + 2))
    print("generating %s..." % test_name)
    generate_test(test_name, 1000)

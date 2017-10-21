import os
import shutil
from lib import random
from solution import solve

random.seed(42)

manual_tests = [
    {"task": [1, 1, 3],
     "ans": 2},

    {"task": [2, 1],
     "ans": 0},

    {"task": [1],
     "ans": 0},

    {"task": [1, 1, 1, 1],
     "ans": 3},

    {"task": [2, 3, -1, 1, 2, 2],
     "ans": 4},

    {"task": [1, -3, 1],
     "ans": 1},

    {"task": [-5],
     "ans": 0},
]

def generate_test(name):
    n = random.randint(3, 200)
    memory = [random.randint(1, n) for _ in range(n)]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for i in memory:
            f.write(str(i) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(solve(n, memory)))

def generate_manual_test(name, task):
    n = len(task["task"])
    memory = task["task"]
    ans = task["ans"]
    with open(name, "w") as f:
        f.write(str(n) + '\n')
        for i in memory:
            f.write(str(i) + '\n')
    #answer
    with open("%s.a" % name, 'w') as f:
        f.write(str(ans))

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    #manual tests
    for test, task in enumerate(manual_tests):
        test_name = os.path.join(test_folder, "%02d" % (test + 1))
        print("generating %s..." % test_name)
        generate_manual_test(test_name, task)

    #random tests
    for test in range(len(manual_tests) + 1, len(manual_tests) + 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name)

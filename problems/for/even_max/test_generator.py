import os
import shutil
from lib import random

random.seed(42)

manual_tests = [
    {"task": [1, 2, 4, 7, 4, 0],
     "ans": 4},

    {"task": [1, 3, 5, 0],
     "ans": 0},

    {"task": [0],
     "ans": 0},

    {"task": [1, 0],
     "ans": 0},

    {"task": [6, 6, 6, 0],
     "ans": 6},
]

def generate_manual_test(name, task):
    seq = task["task"]
    ans = task["ans"]
    with open(name, "w") as f:
        for el in seq:
            f.write(str(el) + '\n')
    with open('%s.a' % name, "w") as f:
        f.write(str(ans) + '\n')

def generate_test(name):
    n = random.randint(3, 200)
    ans = random.randint(20, 1000)
    if ans % 2:
        ans += 1
    seq = [random.randint(1, ans) for _ in range(n)]
    seq.insert(random.randint(0, n - 1), ans)
    seq.append(0)
    with open(name, "w") as f:
        for el in seq:
            f.write(str(el) + '\n')
    with open('%s.a' % name, "w") as f:
        f.write(str(ans) + '\n')


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    #manual tests
    for test, task in enumerate(manual_tests):
        test_name = os.path.join(test_folder, "%02d" % (test + 1))
        print("generating %s..." % test_name)
        generate_manual_test(test_name, task)

    for test in range(len(manual_tests) + 1, len(manual_tests) + 6):
        test_name = os.path.join(test_folder, "%02d" % (test + 1))
        print("generating %s..." % test_name)
        generate_test(test_name)

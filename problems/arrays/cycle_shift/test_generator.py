#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test": [
        [1],
        [1,-1],
        [1,1,1,1,1],
        [1,2,3,4,5],
        [1,2,3,2,1]
    ],
    "answer": [
        [1],
        [-1,1],
        [1,1,1,1,1],
        [2,3,4,5,1],
        [2,3,2,1,1]
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(arr):
    return arr[1:]+arr[:1]

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    # manual tests
    for idx, (test, answer) in enumerate(zip(manual["test"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx + 1,))
        with open(test_name, "w") as f:
            f.write("{}\n".format(len(test)))
            f.write(" ".join(map(str, test)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, answer)))
    # random tests
    for test in range(len(manual["test"])+1, len(manual["test"])+NUM_RANDOM_TESTS+1):
        test_name = os.path.join(test_folder, "%02d" % (test,))
        seq_len = random.randint(30, 100)
        N = random.randint(0, seq_len)
        seq = [random.randint(-100, 100) for _ in range(seq_len)]
        with open(test_name, "w") as f:
            f.write("{}\n".format(seq_len))
            f.write(" ".join(map(str, seq)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, gen_answer(seq))))
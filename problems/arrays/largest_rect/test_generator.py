#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test": [
        [1],
        [1,2,3,4,5],
        [1,2,3,2,1],
        [3,3,3,3,3],
        [5,3,1,4,5],
        [5,3,1,3,5],
        [5,3,2,4,5],
        [0],
        [3,0,3,5,0]
    ],
    "answer": [
        1,
        9,
        6,
        15,
        8,
        6,
        10,
        0,
        6
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(N, array):
    result = min(array) * N
    for w in range(1, N):
        for i in range(N - w + 1):
            result = max(result, min(array[i:i + w]) * w)
    return result

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    # manual tests
    for idx, (test, answer) in enumerate(zip(manual["test"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx + 1,))
        with open(test_name, "w") as f:
            f.write(" ".join(map(str, test)))
        with open(test_name + '.a', "w") as f:
            f.write(str(answer))
    # random tests
    for test in range(len(manual["test"])+1, len(manual["test"])+NUM_RANDOM_TESTS+1):
        test_name = os.path.join(test_folder, "%02d" % (test,))
        seq_len = random.randint(50, 100)
        seq = [random.randint(0, 1000) for _ in range(seq_len)]
        with open(test_name, "w") as f:
            f.write(" ".join(map(str, seq)))
        with open(test_name + '.a', "w") as f:
            f.write(str(gen_answer(len(seq), seq)))
#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test": [
        [1],
        [1,1,1,1,1],
        [1,2,3,4,5],
        [11,13,21,25,42]
    ],
    "answer": [
        [1],
        [1,1,1,1,1],
        [1,2,3,4,5],
        [11,21,13,42,25]
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(arr):
    arr = arr[:]
    def bubble_sort(arr, key = None):
        if key is None:
            key = lambda x: x
        reverse = -1
        while reverse != 0:
            reverse = 0
            for i in range(len(arr)-1):
                if key(arr[i]) > key(arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    reverse += 1

    def digit_sum(x):
        s = 0
        for i in x:
            s += int(i)
        return s

    bubble_sort(arr, digit_sum)
    return arr

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    # manual tests
    for idx, (test, answer) in enumerate(zip(manual["test"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx + 1,))
        with open(test_name, "w") as f:
            f.write('{}\n'.format(len(test)))
            f.write("\n".join(map(str, test)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, answer)))
    # random tests
    for test in range(len(manual["test"])+1, len(manual["test"])+NUM_RANDOM_TESTS+1):
        test_name = os.path.join(test_folder, "%02d" % (test,))
        seq_len = random.randint(30, 100)
        seq = [str(random.randint(0, 10000)) for _ in range(seq_len)]
        with open(test_name, "w") as f:
            f.write('{}\n'.format(seq_len))
            f.write("\n".join(map(str, seq)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(gen_answer(seq)))
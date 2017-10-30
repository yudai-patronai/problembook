#!/usr/bin/env python3

import os
import shutil
#from lib import random
import random

NUM_RANDOM_TESTS = 7
random.seed(42)

def gen_answer(arr1, arr2):
    arr = []
    if len(arr1) == 0:
        arr = arr2[:]
        return arr
    if len(arr2) == 0:
        arr = arr1[:]
        return arr
    i1, i2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    while i1 < n1 and i2 < n2:
        if arr1[i1] < arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1
    if i1 < n1:
        arr += arr1[i1:]
    if i2 < n2:
        arr += arr2[i2:]
    return arr


manual = {
    "arr1": [
        [1, 4],
        [2],
        [-10, 4, 6]
    ],
    "arr2": [
        [3, 5],
        [-10, 3],
        [1, 2, 3, 4, 5, 6]
    ],
    "answer": [
        [1, 3, 4, 5],
        [-10, 2, 3],
        [-10, 1, 2, 3, 4, 4, 5, 6, 6]
    ]
}



if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    # manual tests
    for idx, (arr1, arr2, answer) in enumerate(zip(manual["arr1"], manual["arr2"], manual["answer"])):
        test_name = os.path.join(test_folder, "%02d" % (idx + 1,))
        with open(test_name, "w") as f:
            f.write(" ".join(map(str, arr1)))
            f.write("\n")
            f.write(" ".join(map(str, arr2)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, answer)))
    # random tests
    for test in range(len(manual["arr1"])+1, len(manual["arr1"])+NUM_RANDOM_TESTS+1):
        test_name = os.path.join(test_folder, "%02d" % (test,))

        len1 = random.randint(0, 50)
        len2 = random.randint(0, 100)

        arr1 = [random.randint(-100, 100) for _ in range(len1)]
        arr2 = [random.randint(-100, 100) for _ in range(len2)]
        arr1.sort()
        arr2.sort()

        with open(test_name, "w") as f:
            f.write(" ".join(map(str, arr1)))
            f.write("\n")
            f.write(" ".join(map(str, arr2)))
        with open(test_name + '.a', "w") as f:
            f.write(' '.join(map(str, gen_answer(arr1, arr2))))
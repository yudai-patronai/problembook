#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test" : [
        [[1], [0]],
        [[4], [0]],
        [[1,2,3,4,2], [2]],
        [[3,3,3,3,3], [2]],
        [[0], [0]],
        [[1,2,3,4,5], [0]],
        [[1,2,3,4,5], [4]]
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(arr, base):
    return (lambda x: sum((i>x) for i in arr))(arr[base])

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    # manual tests
    for idx, test in enumerate(manual["test"]):
        test_name = os.path.join(test_folder, "%02d" % (idx+1,))

        with open(test_name, "w") as f:
            f.write('{}\n{}\n{}'.format(len(test[0]),
                                        "\n".join(map(str, test[0])),
                                        "\n".join(map(str, test[1])))
                                        )
        
        with open(test_name+'.a', "w") as f:
            f.write(str(gen_answer(test[0],test[1][0])))
    
    # random tests
    shift = len(manual["test"])
    for test in range(shift+1, NUM_RANDOM_TESTS+shift+1):
        
        test_name = os.path.join(test_folder, "%02d" % (test))
        
        seq_len = random.randint(100,100000)
        v1 = [random.randint(-1000,1000) for _ in range(seq_len)]
        M = [random.randint(0,seq_len-1)]

        with open(test_name, "w") as f:
            f.write('{}\n{}\n{}'.format(seq_len,
                                        "\n".join(map(str, v1)),
                                        "\n".join(map(str, M)))
                                        )
        
        with open(test_name+'.a', "w") as f:
            f.write(str(gen_answer(v1,M[0])))

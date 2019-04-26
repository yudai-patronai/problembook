#!/usr/bin/env python3

import os
import shutil
from lib import random

manual = {
    "test" : [
        [1, [1], [1]],
        [1, [4], [2]],
        [5, [1,2,3,4,2], [3,2,2,1,4]],
        [5, [3,3,3,3,3], [3,3,3,3,3]],
        [1, [0], [0]],
        [1, [0], [100025212]]
    ]
}

NUM_RANDOM_TESTS = 5
random.seed(42)

def gen_answer(v1,v2):
    return sum(x*y for x,y in zip(v1,v2))

if __name__ == "__main__":
    # clear test directory
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    # manual tests
    for idx, test in enumerate(manual["test"]):
        test_name = os.path.join(test_folder, "%02d" % (idx+1,))

        with open(test_name, "w") as f:
            f.write('{}\n{}\n{}'.format(test[0],
                                        " ".join(map(str, test[1])),
                                        " ".join(map(str, test[2]))))
        
        with open(test_name+'.a', "w") as f:
            f.write(str(gen_answer(test[1],test[2])))
    
    # random tests
    shift = len(manual["test"])
    for test in range(shift+1, NUM_RANDOM_TESTS+shift+1):
        
        test_name = os.path.join(test_folder, "%02d" % (test))
        
        seq_len = random.randint(10, 100)
        v1 = [random.randint(-1000,1000) for _ in range(seq_len)]
        v2 = [random.randint(-1000,1000) for _ in range(seq_len)]

        with open(test_name, "w") as f:
            f.write('{}\n'.format(seq_len))
            f.write('{}\n{}'.format(" ".join(map(str, v1)),
                                    " ".join(map(str, v2))))
        
        with open(test_name+'.a', "w") as f:
            f.write(str(gen_answer(v1,v2)))

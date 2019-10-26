#!/usr/bin/env python3

NEG_BASE = -10

import os
from lib import random
import shutil

random.seed(42)

def generate_input(decimal):
    result = ""
    remainder = decimal

    while remainder != 0:
        next_character = remainder % -NEG_BASE

        remainder //= -NEG_BASE
        remainder *= -1
        result = str(next_character) + result 

    return result


def generate_test(name, answer):
    with open(name, "w") as f:
        f.write(generate_input(answer))
    
    with open("%s.a" % name, 'w') as f:
        f.write(str(answer))


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    for test in range(1, 100):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)

        answer = random.randint(-999999, 999999)
        generate_test(test_name, answer)


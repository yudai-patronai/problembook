import os
from lib import random
import shutil
import string
import re
import json


def generate_random_string(n, alphabet):
    s = []
    for i in range(n):
        s.append(random.choice(alphabet))
    return "".join(s)

if __name__ == "__main__":

    N = 20
    random.seed(42)

    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    with open("python_table.txt") as f:
        table = json.load(f)

    tests = ["ACA", "LPK", "EIR"]
    for i in [1, 2, 3]:
        input_str = tests[i - 1]
        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{0}\n".format(input_str))

        mass = 0.0
        for c in input_str:
            mass += table[c]

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}'.format(mass))

    for i in range(4, N + 1):
        input_size = random.randint(10, 1000)
        input_str = generate_random_string(input_size, table.keys())

        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{0}\n".format(input_str))

        mass = 0.0
        for c in input_str:
            mass += table[c]

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}'.format(mass))

import os
from lib import random
import shutil
import string
import re

ALPHABET = list(string.ascii_lowercase + string.digits + ' ')

def generate_random_string(n, alphabet):
    s = []
    for i in range(n):
        s.append(random.choice(alphabet))
    return "".join(s)

if __name__ == "__main__":

    N = 50
    random.seed(42)

    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i in range(1, N + 1):
        input_size = random.randint(10, 255)
        input_str = generate_random_string(input_size, ALPHABET)

        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{0}\n".format(input_str))

        result = [e for e in re.split("[^0-9]", input_str) if e != '']
        result = max(map(int, result))

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}'.format(result))

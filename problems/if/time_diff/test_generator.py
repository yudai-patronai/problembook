import os
# from lib import random
import random
import shutil
import string
import re

def solve(t1, t2):
    s1 = 3600*int(t1[:2]) + 60*int(t1[3:5]) + int(t1[7:])
    s2 = 3600*int(t2[:2]) + 60*int(t2[3:5]) + int(t2[7:])
    if s1 <= s2:
        return s2 - s1
    return 24*60*60 - s1 + s2

def generate_random_time():
    h, m, s = random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

if __name__ == "__main__":

    N = 20
    random.seed(42)

    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i in range(1, N + 1):
        t1 = generate_random_time()
        t2 = generate_random_time()

        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{}\n{}\n".format(t1, t2))

        result = solve(t1, t2)

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}'.format(result))
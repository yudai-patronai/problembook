import os
from lib import random
import shutil
import string
import re


def generate_random_string(n):
    s = []
    for i in range(n):
        s.append(random.choice("ACGT"))
    return "".join(s)

def check(s, t, u):
    if t and s[0] == t[0] and check(s[1:], t[1:], u):
        return True
    if u and s[0] == u[0] and check(s[1:], t, u[1:]):
        return True
    return False

if __name__ == "__main__":

    N = 20
    random.seed(42)

    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)


    # tests = ["ACA", "LPK", "EIR"]
    for i in [1, 2, 3]:
        input_str = tests[i - 1]
        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{0}\n".format(input_str))

        mass = 0.0
        for c in input_str:
            mass += table[c]

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{:.5f}'.format(mass))

    for i in range(4, N + 1):
        n = random.randint(20, 1000)
        m = random.randint(3, 10)
        k = random.randint(3, 10)
        s = generate_random_string(n)
        t = ""
        u = ""
        if random.randint(0, 1):
            pos = random.randint(0, n - m - k)
            delta = random.randint(0, 3)
            sub = s[pos:pos + m + k - delta]
            for c in sub:
                if m and k:
                    to = random.randint(0, 2)
                    if to == 0:
                        t += c
                    elif to == 1:
                        u += c
                    else:
                        t += c
                        u += c
        else:
            pos = random.randint(0, n - m - k)
            sub = s[pos:pos + m + k - delta]
            for c in sub:
                if m and k:
                    to = random.randint(0, 2)
                    if to == 0:
                        t += c
                    elif to == 1:
                        u += c

        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{}\n{}\n{}\n".format(s, t, u))

        n = len(s)
        m = len(t)
        k = len(u)
        res = "No"
        for i in range(n - m - k + 1):
            if set(s[i:i + m + k]) != set(t) + set(u):
                continue
            if check(s[i:i + m + k], t, u):
                res = "Yes"
                break

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}\n'.format(res))

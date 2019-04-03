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
    if t == u == "":
        return True
    result = False
    if t and s[0] == t[0]:
        result |= check(s[1:], t[1:], u)
    if not result and u and s[0] == u[0]:
        result |= check(s[1:], t, u[1:])
    return result

if __name__ == "__main__":

    N = 20
    random.seed(42)

    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)


    tests = [
        ("GACCACGGTT", "ACAG", "CCG", "Yes"),
        ("GACCACAAAAGGTT", "ACAG", "CCG", "No"),
        ("GACACGGTT", "ACAG", "CCG", "No")
    ]
    for i in [1, 2, 3]:
        s, t, u, res = tests[i - 1]
        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{}\n{}\n{}\n".format(s, t, u))
        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}\n'.format(res))

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
                        m -= 1
                    elif to == 1:
                        u += c
                        k -= 1
                    else:
                        t += c
                        u += c
                        m -= 1
                        k -= 1
                elif m:
                    t += c
                    m -= 1
                elif k:
                    u += c
                    k -= 1 
        else:
            pos = random.randint(0, n - m - k)
            sub = s[pos:pos + m + k]
            for c in sub:
                if m and k:
                    if random.randint(0, 1):
                        t += c
                        m -= 1
                    else:
                        u += c
                        k -= 1
                elif m:
                    t += c
                    m -= 1
                elif k:
                    u += c
                    k -= 1    

        with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
            f.write("{}\n{}\n{}\n".format(s, t, u))

        n = len(s)
        m = len(t)
        k = len(u)
        res = "No"
        for j in range(n - m - k + 1):
            if set(s[j:j + m + k]) != set(t) | set(u):
                continue
            if check(s[j:j + m + k], t, u):
                res = "Yes"
                break

        with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
            f.write('{}\n'.format(res))

    s = "".join([random.choice(["C", "G"]) for _ in range(10000 - 20)])
    s += "AAAAAAAAATAAAAAAAAAA"
    t = "A" * 10
    u = "A" * 9 + "T"
    with open(os.path.join(tests_dir, '{0:0>2}'.format(N + 1)), 'w') as f:
            f.write("{}\n{}\n{}\n".format(s, t, u))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(N + 1)), 'w') as f:
            f.write('{}\n'.format("Yes"))

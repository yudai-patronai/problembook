from time import time
import sys


with open("{}.py".format('solution' if input() == 'good' else '__solution_bad_left'), 'r') as f:
    with open('tests/{:02d}'.format(int(input())), 'r') as stdin:
        old_stdin = sys.stdin
        sys.stdin = stdin
        t0 = time()
        exec(f.read())
        print(time() - t0)
        sys.stdin = old_stdin

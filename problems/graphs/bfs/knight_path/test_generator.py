#!/usr/bin/env python3

import os
import shutil
import subprocess as sp


def generate_answer(test):
    with open(test) as f:
        with open("%s.a" % test, "w") as g:
            sp.check_call(["./solution.py"], stdin=f, stdout=g)
    with open("%s.a" % test) as f:
        answer = f.readlines()
    return answer


def dump_input(input_, name):
    with open(name, "w") as f:
        f.write(input_)


if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    tests_input = [('a1', 'a2'), ('a1', 'a3'), ('a1', 'h7'), ('e2', 'e4'), ('c3', 'd4'), ('b2', 'c4'), ('e7', 'd7'),
                   ('h1', 'a2')]
    for i, inp in enumerate(tests_input):
        test_name = os.path.join(test_folder, "%02d" % i)
        print("generated input: %s, %s" % (inp, test_name))
        dump_input('\n'.join(inp), test_name)
        answer = generate_answer(test_name)
        print("generated: %s, %s" % (answer, test_name))

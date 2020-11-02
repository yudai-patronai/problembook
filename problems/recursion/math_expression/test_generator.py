#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, case, ans):
    with open(test_file, 'w') as f:
        f.write(case + "\n")
    with open(test_file + '.a', 'w') as f:
        f.write(str(ans))


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = [
        ("2+5", 7),
        ("3-9", -6),
        ("2*(2+2)", 8),
        ("-(15+3)*9^2", -1458),
        ("-5^2", -25),
        ("(3+6)^(15/5)", 729),
        ("15^3*15/3", 16875),
        ("6*-6", -36),
        ("0*(-5+6^2)", 0),
        ("16*(-5+0^2)", -80),
    ]

    for key, value in enumerate(boards_ans, start=1):
        make_test(os.path.join(test_folder, f"{key:02}"), value[0], value[1])

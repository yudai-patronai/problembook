#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


s1 = "abcdefgh"
s2 = "12345678"


def is_correct_step(p1, p2):
    ix_1 = s1.index(p1[0])
    ix_2 = s1.index(p2[0])

    iy_1 = s2.index(p1[1])
    iy_2 = s2.index(p2[1])

    if abs(ix_1 - ix_2) + abs(iy_1 - iy_2) == 3:
        return True
    return False


def is_correct_path(path):
    # check points in board
    for p in path:
        if "a" <= p[0] <= "h" and "1" <= p[1] <= "8":
            pass
        else:
            return False
    # check steps
    for i, p in enumerate(path[:-2]):
        if not is_correct_step(p, path[i + 1]):
            return False
    return True


# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 4:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

correct_len = 0
correct_lines = []

with open(answer_file) as f:
    lines = [l.rstrip() for l in f.readlines()]
    correct_len = len(lines)
    correct_lines = lines

try:
    with open(output_file) as f:
        lines = [l.rstrip() for l in f.readlines()]
        if len(lines) != correct_len:
            print('FAIL1')
            sys.exit(CheckerResult.WA)
        if lines[0] != correct_lines[0] or lines[-1] != correct_lines[-1]:
            print('FAIL2')
            sys.exit(CheckerResult.WA)
        if not is_correct_path(lines):
            print('FAIL3')
            sys.exit(CheckerResult.WA)
except (IOError, ValueError):
    print('FAIL4')
    sys.exit(CheckerResult.PE)

print('OK')
sys.exit(CheckerResult.OK)

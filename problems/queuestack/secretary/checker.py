#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


# checker <input_file> <output_file> <answer_file>
if len(sys.argv) < 3:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

with open(answer_file) as f:
    answer = float(f.read().strip())

try:
    with open(output_file) as f:
        out = float(f.read().strip())
except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if answer != out:
    print('Incorrect answer')
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

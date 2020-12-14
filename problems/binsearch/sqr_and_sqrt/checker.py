#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 3:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

with open(answer_file) as f:
    ans = float(f.read().strip())

try:
    with open(output_file) as f:
        x = float(f.read().strip())
except (IOError, ValueError):
    print('Output does not contain a float number')
    sys.exit(CheckerResult.PE)

if abs(ans - x) > 1e-6:
    print('Incorrect answer')
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 4:
    sys.exit(3)

output_file = sys.argv[2]
answer_file = sys.argv[3]

try:
    with open(output_file) as f:
        o_weight = int(f.readline().strip())
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

with open(answer_file) as f:
    a_weight = int(f.readline().strip())

if o_weight != a_weight:
    print('FAIL')
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

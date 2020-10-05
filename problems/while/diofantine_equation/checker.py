#!/usr/bin/python3
import bisect
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

with open(input_file) as f:
    a, b, c = map(int, f.read().strip().split())

with open(answer_file) as f:
    ans = f.read().strip()

try:
    with open(output_file) as f:
        outp = f.read().strip()
except (IOError, ValueError):
    print('Read fail')
    sys.exit(CheckerResult.PE)

if outp == "No solution":
    if ans == "No solution":
        print('OK')
        sys.exit(CheckerResult.OK)
    else:
        print("The equation is solvable")
        sys.exit(CheckerResult.WA)

try:
    x, y = map(int, ans.split())
except ValueError as e:
    print(e)
    sys.exit(CheckerResult.PE)

if c != a * x + b * y:
    print("Wrong solution")
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

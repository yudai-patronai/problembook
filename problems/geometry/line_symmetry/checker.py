#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


# checker <input_file> <output_file> <answer_file>
if len(sys.argv) < 4:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

with open(answer_file) as f:
    data = f.readline().strip().split()
    answer = [float(val) for val in data]

try:
    with open(output_file) as f:
        data = f.readline().strip().split()
        oanswer = [float(val) for val in data]

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if len(oanswer) != 2:
    print("Output should have 2 numbers, not {}".format(len(oanswer)))
    sys.exit(CheckerResult.PE)

eps = 1e-5
for i in range(2):
    a = answer[i]
    b = oanswer[i]
    if abs(a - b) > 1e-5:
        print("expected ({:.5f}; {:.5f}), "
              "but got ({:.5f}; {:.5f})".format(answer[0], answer[1],
                                                oanswer[0], oanswer[1]))
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

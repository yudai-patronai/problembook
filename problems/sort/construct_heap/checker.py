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
    data = f.readline().strip()
    answer = list(map(int, data.split()))

try:
    with open(output_file) as f:
        data = f.readline().strip()
        oanswer = list(map(int, data.split()))

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if len(answer) != len(oanswer):
    print("Output should have {} numbers, not {}".format(len(answer),
                                                         len(oanswer)))
    sys.exit(CheckerResult.PE)

n = len(answer)
for i in range(1, n):
    if oanswer[(i-1) // 2] > oanswer[i]:
        print("Heap is incorrect")
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

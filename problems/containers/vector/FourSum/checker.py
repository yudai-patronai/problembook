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

#with open(input_file) as f:
#    n = int(f.readline()[:-1])
#    m = int(f.readline()[:-1])

with open(answer_file) as f:
    answer = " ".join(f.readlines())
    answer = answer.split()
    answer = list(answer[i:i+4] for i in range(0,len(answer), 4))
    answer.sort()

try:
    with open(output_file) as f:
        output = " ".join(f.readlines())
        output = output.split()
        output = list(output[i:i+4] for i in range(0,len(output), 4))
        output.sort()

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if answer != output:
    print('Wrong answer'.format(answer, output))
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

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
    data = f.readlines()
    answers = [float(line.strip()) for line in data]

try:
    with open(output_file) as f:
        data = f.readlines()
        oanswers = [float(line.strip()) for line in data]

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if len(answers) != len(oanswers):
    print("Output should have {} answers, not {}".format(len(answers),
                                                         len(oanswers)))
    sys.exit(CheckerResult.PE)

eps = 1e-5
for i in range(len(answers)):
    a = answers[i]
    b = oanswers[i]
    if abs(a - b) > 1e-5:
        print("answers #{} are different".format(i))
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

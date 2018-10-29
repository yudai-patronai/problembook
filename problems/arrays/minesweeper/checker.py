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

with open(input_file) as f:
    n = int(f.readline()[:-1])
    m = int(f.readline()[:-1])

with open(answer_file) as f:
    answer = []
    for i in range(n):
        line = list(map(int, f.readline().split()))
        answer.append(line)

try:
    with open(output_file) as f:
        output = []
        for i in range(n):
            line = list(map(int, f.readline().split()))
            output.append(line)

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

for i in range(n):
    for j in range(m):
        if answer[i][j] != output[i][j]:
            print('There should be {}, but {} is found'.format(answer[i][j], output[i][j]))
            sys.exit(CheckerResult.WA)    
print('OK')
sys.exit(CheckerResult.OK)

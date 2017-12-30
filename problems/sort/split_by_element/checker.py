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
answer_file = sys.argv[2]

with open(input_file) as f:
    array = [int(x) for x in f.readline().split(" ")]
    x = int(f.readline()[:-1])

with open(answer_file) as f:
    ans_array = [int(x) for x in f.readline().split(" ")]

try:
    with open(output_file) as f:
        out_array = [int(x) for x in f.readline().split(" ")]

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if len(out_array) != len(array):
    print('Wrong array length')
    sys.exit(CheckerResult.PE)

for i, j in zip(sorted(array), sorted(out_array)):
    if i != j:
        print('Output array contains incorrect set of elements')
        sys.exit(CheckerResult.PE) 

i = 0
n = len(array)
for i in range(n):
    if ans_array[i] < x and out_array[i] >= x:
        print('Incorrect spliting')
        sys.exit(CheckerResult.WA)
    elif ans_array[i] == x and out_array[i] != x:
        print('Incorrect spliting')
        sys.exit(CheckerResult.WA)
    elif ans_array[i] > x and out_array[i] <= x:
        print('Incorrect spliting')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)
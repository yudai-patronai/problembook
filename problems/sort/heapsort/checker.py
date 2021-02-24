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
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split(' ')))

with open(answer_file) as f:
    ans = f.readlines()

try:
    with open(output_file) as f:
        out = list(map(int, f.readlines()))
    for i in range(len(out)):
        out[i] = list(map(int, out[i].split()))

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

if len(ans) != len(out):
    print("Not enough iterations")
    sys.exit(CheckerResult.WA)

for m in range(len(out)):
    line = out[m]
    for i in range(n-m):
        if 2*i+1 < n-m and line[i] < line[2*i+1]:
            print("Incorrect heap")
            sys.exit(CheckerResult.WA)
        if 2*i+2 < n-m and line[i] < line[2*i+2]:
            print("Incorrect heap")
            sys.exit(CheckerResult.WA)
    for i in range(n-m, n-1):
        if line[i] > line[i+1]:
            print("Incorrect sort result")
            sys.exit(CheckerResult.WA)

if (line[-1] != sorted(arr)):
    print("Incorrect output array")
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

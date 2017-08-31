#!/usr/bin/python3
import sys


class CheckerResult:
    OK = 0  # OK, правильный ответ
    WA = 1  # WA, wrong answer, неправильный ответ
    PE = 2  # PE, presentation error, ошибка неправильного формата результата


# checker <input_file> <output_file> <answer_file> [<report_file> [<-appes>]]
if len(sys.argv) < 4:
    sys.exit(3)

input_file = sys.argv[1]
output_file = sys.argv[2]
answer_file = sys.argv[3]

o_yes = True
try:
    with open(output_file) as f:
        line = f.readline().strip()
        if 'NO' == line:
            o_yes = False
        else:
            o_group = set(map(int, line.split()))
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

a_yes = True
with open(answer_file) as f:
    if 'NO' == f.readline().strip():
        a_yes = False

edges = set()
with open(input_file) as f:
    n, m = map(int, f.readline().split())
    for l in f.readlines():
        a, b = map(int, l.split())
        if a > b:
            a, b = b, a
        edges.add((a, b))

if o_yes:
    for e in edges:
        if len(set(e) & o_group) != 1:
            print('FAIL')
            sys.exit(CheckerResult.WA)
elif o_yes != a_yes:
    print('FAIL')
    sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

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

no_cycle = False
min_len = -1
with open(answer_file) as f:
    s = f.readline().rstrip()
    if s == 'NO CYCLES':
        no_cycle = True
    else:
        min_len = len(s.split())

o_no_cycle = False
o_cycle = []
try:
    with open(output_file) as f:
        s = f.readline().rstrip()
        if s == 'NO CYCLES':
            o_no_cycle = True
        else:
            o_cycle = list(map(int, s.split()))
except (IOError, ValueError):
    ts_directedrint('FAIL')
    sys.exit(CheckerResult.PE)

if no_cycle != o_no_cycle:
    print('FAIL')
    sys.exit(CheckerResult.WA)
elif no_cycle:
    print('OK')
    sys.exit(CheckerResult.OK)

if min_len != len(o_cycle):
    print('FAIL')
    sys.exit(CheckerResult.WA)

edges = set()
with open(input_file) as f:
    n, m = map(int, f.readline().split())
    for l in f.readlines():
        edges.add(tuple(map(int, l.split())))

for i in range(-1, len(o_cycle) - 1):
    if (o_cycle[i], o_cycle[i + 1]) not in edges:
        print('FAIL')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

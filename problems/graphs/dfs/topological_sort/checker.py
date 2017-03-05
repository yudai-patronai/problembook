#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath('../..'))

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

no_toposort = False
with open(answer_file) as f:
    s = f.readline().rstrip()
    if s == 'NO':
        no_toposort = True

o_no_toposort = False
o_toposort = []
try:
    with open(output_file) as f:
        s = f.readline().rstrip()
        if s == 'NO':
            o_no_toposort = True
        else:
            o_toposort = list(map(int, s.split()))
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

if no_toposort != o_no_toposort:
    print('FAIL')
    sys.exit(CheckerResult.PE)
elif no_toposort:
    print('OK')
    sys.exit(CheckerResult.OK)

edges = []
with open(input_file) as f:
    n, m = map(int, f.readline().split())
    for l in f.readlines():
        edges.append(tuple(map(int, l.split())))

if len(o_toposort) != n:
    print('FAIL')
    sys.exit(CheckerResult.PE)

o_toposort_set = set(o_toposort)
for i in range(n):
    if i not in o_toposort_set:
        print('FAIL')
        sys.exit(CheckerResult.PE)

time = {o_toposort[i]: i for i in range(n)}
for a, b in edges:
    if time[a] > time[b]:
        print('FAIL')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

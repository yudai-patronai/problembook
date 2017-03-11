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

try:
    with open(output_file) as f:
        o_weight = int(f.readline().strip())
        o_hamiltonian_cycle = list(map(int, f.readline().rstrip().split()))
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

edges = {}
with open(input_file) as f:
    n, m = map(int, f.readline().split())
    for l in f.readlines():
        a, b, w = map(int, l.split())
        if a > b:
            a, b = b, a
        edges[(a, b)] = w

with open(answer_file) as f:
        a_weight = int(f.readline().strip())

if len(o_hamiltonian_cycle) != n or \
        set(o_hamiltonian_cycle) != set(range(n)):
    print('FAIL')
    sys.exit(CheckerResult.WA)

weight = 0
for i in range(-1, len(o_hamiltonian_cycle) - 1):
    a, b = o_hamiltonian_cycle[i], o_hamiltonian_cycle[i + 1]
    if a > b:
        a, b = b, a
    if (a, b) not in edges:
        print('FAIL')
        sys.exit(CheckerResult.WA)
    weight += edges[(a, b)]

if weight != o_weight > a_weight:
        print('FAIL')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

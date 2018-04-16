#!/usr/bin/python3
import sys


def possible_move(u, v):
    if u-1 == v:
        return True
    if u+1000 == v:
        return True
    if u % 1000 * 10 + u // 1000 == v:
        return True
    if u // 10 + u % 10 * 1000 == v:
        return True
    return False


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

with open(input_file) as f:
    s, t = map(lambda x: int(x.strip()), f.readlines())

with open(answer_file) as f:
    path_len = int(f.readline().strip())

try:
    with open(output_file) as f:
        path = list(map(lambda x: int(x.strip()), f.readlines()))
except (IOError, ValueError):
    print('FAIL')
    sys.exit(CheckerResult.PE)

if len(path) != path_len:
    print('FAIL')
    sys.exit(CheckerResult.WA)

if path[0] != s or path[-1] != t:
    print('FAIL')
    sys.exit(CheckerResult.WA)

for i in range(path_len-1):
    if not possible_move(path[i], path[i+1]):
        print('FAIL')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

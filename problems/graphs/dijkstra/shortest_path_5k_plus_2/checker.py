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
    n, m = map(int, f.readline().split())
    graph = [{} for i in range(n)]
    for i in range(m):
        a, b, w = list(map(int, f.readline().split()))
        graph[a][b] = w
        graph[b][a] = w
    k = int(f.readline().strip())
    pairs = []
    for i in range(k):
        a, b = list(map(int, f.readline().split()))
        pairs.append((a, b))

with open(answer_file) as f:
    answers = []
    for i in range(k):
        ans = list(map(int, f.readline().split()))
        answers.append(ans)

try:
    with open(output_file) as f:
        oanswers = []
        for i in range(k):
            oans = list(map(int, f.readline().split()))
            oanswers.append(oans)

except (IOError, ValueError):
    print('Wrong formating')
    sys.exit(CheckerResult.PE)

for i in range(k):
    ans, oans = answers[i], oanswers[i]
    if ans[0] == -1:
        if oans[0] == -1:
            continue
        print('Should be -1 for pair', i)
        sys.exit(CheckerResult.WA)

    for i in range(len(oans)):
        if ans[i] < 0 or ans[i] >= n:
            print('Vertex does not exist in graph')
            sys.exit(CheckerResult.WA)

    for i in range(len(oans) - 1):
        if ans[i + 1] not in graph[ans[i]]:
            print('Edge does not exist in graph')
            sys.exit(CheckerResult.WA)

    if (len(oans) - 1) % 5 != 2:
        print('Number of edges in path is wrong')
        sys.exit(CheckerResult.WA)

    weight = sum([graph[ans[i]][ans[i + 1]] for i in range(len(ans) - 1)])
    oweight = sum([graph[oans[i]][oans[i + 1]] for i in range(len(oans) - 1)])
    if oweight != weight:
        print('There is shorter path in graph')
        sys.exit(CheckerResult.WA)

print('OK')
sys.exit(CheckerResult.OK)

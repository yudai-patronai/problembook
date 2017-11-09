from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 10
MAX_GRAPH_SIZE = 10

def floyd_warshall(graph, first, second):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] > 0 and graph[k][j] > 0:
                    if graph[i][j] > 0:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    else:
                        graph[i][j] = graph[i][k] + graph[k][j]
    return graph[first][second]


def get_case(graph, first, second):
    n = len(graph)
    q_str = '{}\n{} {}\n'.format(n, first, second)
    q_str += '\n'.join([' '.join([str(d) for d in row]) for row in graph])
    a_str = str(floyd_warshall(graph, first - 1, second - 1))
    return q_str, a_str

def gen_rand_graph(size):
    graph = [[-1] * size for _ in range(size)]
    for i in range(size):
        graph[i][i] = 0
        for j in range(i + 1, size):
            val = -1 if randint(0, 3) == 0 else randint(1, 10)
            graph[i][j] = graph[j][i] = val
    return graph


tests = TestSet()

tests.add(*get_case([[0, -1],
                     [-1, 0]],
                    1, 2))

tests.add(*get_case([[0, 1, 5],
                     [1, 0, 1],
                     [5, 1, 0]],
                    1, 3))

tests.add(*get_case([[0, 1, -1, 4],
                     [1, 0, 2, 8],
                     [-1, 2, 0, 3],
                     [4, 8, 3, 0]],
                    2, 4))

for _ in range(MAX_RAND_TESTS):
    size = randint(4, MAX_GRAPH_SIZE)
    tests.add(*get_case(gen_rand_graph(size), 1, size))

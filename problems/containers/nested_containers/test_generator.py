from lib.testgen import TestSet
from lib.random import randint
from lib.random import shuffle

MAX_RAND_TESTS = 10
MAX_GRAPH_SIZE = 30

def get_case(size):
    edges = []
    vertices = []
    for i in range(size):
        count = 0
        weight = 0
        for j in range(size):
            val = -1 if randint(0, 3) == 0 else randint(1, 10)
            if i != j and val != -1:
                edges.append((i, j, val))
                count += 1
                weight += val
        if count != 0:
            vertices.append((i, count, weight))

    shuffle(edges)

    edge_str = str(len(edges)) + '\n' + '\n'.join([' '.join([str(x) for x in edge]) for edge in edges]) + '\n'
    vertex_str = '\n'.join([' '.join([str(x) for x in vertex]) for vertex in vertices]) + '\n'

    return edge_str, vertex_str

tests = TestSet()
tests.add(*get_case(2))
tests.add(*get_case(3))
tests.add(*get_case(4))
tests.add(*get_case(5))

for _ in range(MAX_RAND_TESTS):
    size = randint(5, MAX_GRAPH_SIZE)
    tests.add(*get_case(size))


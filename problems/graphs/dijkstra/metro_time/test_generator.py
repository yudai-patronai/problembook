from lib.testgen import TestSet
from lib.random import choice


def metro_vertexes_edges(input_file):
    vertexes = set()
    edges = []
    with open(input_file) as file:
        for line in file:
            if line.startswith('#'):
                continue
            else:
                u, v, w = line.split()
                w = int(w)
                edges.append((u, v, w))
                vertexes.add(u)
                vertexes.add(v)
    return vertexes, edges


def edges_footer(edges):
    S = ''
    for e in edges:
        S += '{} {} {}\n'.format(*e)
    return S

def question(vertexes, edges, start, end):
    return '{V} {E} {start} {end}\n{edges}'.format(
        V=len(vertexes),
        E=len(edges),
        start=str(start),
        end=str(end),
        edges=edges_footer(edges)
    )


vertexes, edges = metro_vertexes_edges('metro.txt')

testset = TestSet()

# manual tests
testset.add(question(vertexes, edges, 'mendeleevskaya', 'serpukhovskaya'), '17')
testset.add(question(vertexes, edges, 'mendeleevskaya', 'taganskaya_circle'), '16')
testset.add(question(vertexes, edges, 'polyanka', 'lubyanka'), '15')
testset.add(question(vertexes, edges, 'lubyanka', 'polyanka'), '15')
testset.add(question(vertexes, edges, 'mendeleevskaya', 'kitay_gorod'), '17')
testset.add(question(vertexes, edges, 'park_kultury_circle', 'tsvetnoy_bulvar'), '20')
testset.add(question(vertexes, edges, 'krasnopresnenskaya', 'novoslobodskaya'), '6')

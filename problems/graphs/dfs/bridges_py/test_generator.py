from lib.testgen import TestSet
from lib import random


class Graph:
    def __init__(self, n=0):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def merge(self, rhs):
        offset = self.n
        new = rhs.n

        for _ in range(new):
            self.edges.append([[to[0] + offset, to[1]] for to in rhs.edges[_]])

        self.n += new

    def add_node(self):
        self.n += 1
        self.edges.append([])

    def add_edge(self, fr, to, w):
        self.edges[fr].append([to,w])

    def shuffle(self):
        new_numbers = list(range(self.n))
        random.shuffle(new_numbers)

        new_edges = [None for _ in range(self.n)]
        for i in range(self.n):
            new_edges[new_numbers[i]] = [(new_numbers[j[0]], j[1]) for j in self.edges[i]]

        self.edges = new_edges
        return new_numbers

    def to_string(self):
        edges = list(f"{i + 1} {j[0] + 1} {j[1]}" for i in range(self.n) for j in self.edges[i] if i < j[0])
        random.shuffle(edges)
        return f"{self.n} {sum(len(_) for _ in self.edges) // 2}\n" + \
            "\n".join(edges)



def make_full_graph(n):
    g = Graph(n)

    for f in range(n-1):
        for t in range(f+1, n):
            w = random.randrange(1, 100)
            g.add_edge(f,t,w)
            g.add_edge(t,f,w)

    return g

def make_loop(n):
    g = Graph(n)

    for f in range(n-1):
        w = random.randrange(1, 100)
        g.add_edge(f, f+1, w)
        g.add_edge(f+1, f, w)

    w = random.randrange(1, 100)
    g.add_edge(n-1, 0, w)
    g.add_edge(0, n-1, w)

    return g

def merge_and_bridge_many(*graphs, shuffle=True):
    graph = graphs[0]

    n = graph.n
    ans = set()
    for g in graphs[1:]:
        graph.merge(g)
        f = random.randrange(n)
        t = random.randrange(g.n) + n
        w = random.randrange(1, 100)
        graph.add_edge(f, t, w)
        graph.add_edge(t, f, w)
        ans.add(w)
        n = graph.n

    if shuffle:
        new_nums = graph.shuffle()

    return ans


tests = TestSet()

# Public tests - no fun
tests.add("""3 2
1 2 1
2 3 2""", "2")

tests.add("""2 1
1 2 1""", "1")
tests.add("""3 3
1 2 1
2 3 1
3 1 1""", "-1")

# Private tests

# Simple - just one node
tests.add("1 0", "-1")

# Simple - short line
tests.add("5 4\n1 2 1\n2 3 2\n3 4 3\n4 5 4", "4")

# Simple - two cycles with one link
tests.add("6 7\n1 2 1\n2 3 2\n1 3 3\n4 5 4\n5 6 5\n4 6 6\n3 5 4", "4")

# Cycle of cycles
tests.add("""9 12
1 2 1\n2 3 2\n1 3 3
4 5 4\n5 6 5\n4 6 6
7 8 7\n7 9 8\n8 9 9
3 5 1\n5 7 2\n3 7 3""", "-1")

# Contacting cycles
tests.add("""9 10
1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 1 5
3 9 2\n9 8 3\n8 7 4\n7 6 5\n6 3 6""", "-1")

# Long line
N = 10000
tests.add(f"{N} {N-1}\n" + "\n".join(f"{i} {i+1} {i}" for i in range(1, N)), "{}\n".format(N-1))

# Just many cycles
cs = [make_loop(100) for _ in range(50)]
c0 = make_loop(100)
ans = merge_and_bridge_many(c0, *cs)
tests.add(c0.to_string(), str(max(ans)))

# Many edges
N = 300
g = make_full_graph(N)
g.add_node()
g.add_edge(0, N, 42)
g.add_edge(N, 0, 42)
new_order = g.shuffle()
tests.add(g.to_string(), "42")

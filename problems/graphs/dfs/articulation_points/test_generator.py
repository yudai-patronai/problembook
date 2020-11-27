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
            self.edges.append([to + offset for to in rhs.edges[_]])
        
        self.n += new
        
    def add_node(self):
        self.n += 1
        self.edges.append([])
        
    def add_edge(self, fr, to):
        self.edges[fr].append(to)
        
    def shuffle(self):
        new_numbers = list(range(self.n))
        random.shuffle(new_numbers)
        
        new_edges = [None for _ in range(self.n)]
        for i in range(self.n):
            new_edges[new_numbers[i]] = [new_numbers[j] for j in self.edges[i]]
        
        self.edges = new_edges
        return new_numbers
        
    def to_string(self):
        edges = list(f"{i + 1} {j + 1}" for i in range(self.n) for j in self.edges[i] if i < j)
        random.shuffle(edges)
        return f"{self.n} {sum(len(_) for _ in self.edges) // 2}\n" + \
            "\n".join(edges)
            
    

def make_full_graph(n):
    g = Graph(n)
    
    for f in range(n-1):
        for t in range(f+1, n):
            g.add_edge(f,t)
            g.add_edge(t,f)
            
    return g

def make_loop(n):
    g = Graph(n)
    
    for f in range(n-1):
        g.add_edge(f, f+1)
        g.add_edge(f+1, f)
    
    g.add_edge(n-1, 0)
    g.add_edge(0, n-1)
            
    return g

def merge_and_bridge(g1, g2):
    n1 = g1.n
    n2 = g2.n
    g1.merge(g2)
        
    g1.add_node()
    f = random.randrange(g1.n)
    t = random.randrange(g2.n) + g1.n
    g1.add_edge(f, t)
    g1.add_edge(t, f)
    
    news = g1.shuffle()
    return news[f], news[t]

def merge_and_bridge_many(*graphs, shuffle=True):
    graph = graphs[0]
    
    n = graph.n
    ans = set()
    for g in graphs[1:]:
        graph.merge(g)
        f = random.randrange(n)
        t = random.randrange(g.n) + n
        graph.add_edge(f, t)
        graph.add_edge(t, f)
        ans.add(f)
        ans.add(t)
        n = graph.n
    
    if shuffle:
        new_nums = graph.shuffle()
        return sorted([new_nums[i] for i in ans])
    else:
        return list(ans)
        


tests = TestSet()

# Public tests - no fun
tests.add("""3 2
1 2
2 3""", "2")

tests.add("""2 1 1 2""", "-1")
tests.add("""3 3 1 2 2 3 3 1""", "-1")


# Private tests

# Simple - just one node
tests.add("1 0", "-1")

# Simple - short line
tests.add("5 4 1 2 2 3 3 4 4 5", "2 3 4")

# Simple - two cycles with one link
tests.add("6 7 1 2 2 3 1 3 4 5 5 6 4 6 3 5", "3 5")

# Cycle of cycles
tests.add("""9 12
1 2   2 3   1 3
4 5   5 6   4 6
7 8   7 9   8 9
2 8   3 5   6 9""", "-1")

# Cycle of cycles - 2
tests.add("""9 12
1 2   2 3   1 3
4 5   5 6   4 6
7 8   7 9   8 9
3 5   5 7   3 7""", "3 5 7")

# Contacting cycles
tests.add("""9 10
1 2   2 3   3 4   4 5   5 1
3 9   9 8   8 7   7 6   6 3""", "3")

# Long line
N = 1000000
tests.add(f"{N} {N-1}\n" + "\n".join(f"{i} {i+1}" for i in range(1, N)), " ".join(map(str, range(2, N))))

# Just many cycles
cs = [make_loop(1000) for _ in range(1000)]
c0 = make_loop(1000)
ans = merge_and_bridge_many(c0, *cs)
tests.add(c0.to_string(), " ".join(map(lambda one: str(one + 1), ans)))

# Many edges
N = 3000
g = make_full_graph(N)
g.add_node()
g.add_edge(0, N)
new_order = g.shuffle()
tests.add(g.to_string(), str(new_order[0] + 1))

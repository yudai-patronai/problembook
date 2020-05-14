#!/usr/bin/env python3

from lib import random
from lib.testgen import TestSet
from lib.graphs import task

random.seed(42)


class GraphComponent(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.free_edges = set()


class GraphGen:
    def __init__(self):
        self.dsu = None
        self.sets = None

    @staticmethod
    def make_set(x):
        return {
            "parent": x,
            "rank": 1
        }

    def find_set(self, x):
        if self.dsu[x]["parent"] == x:
            return x
        self.dsu[x]["parent"] = self.find_set(self.dsu[x]["parent"])
        return self.dsu[x]["parent"]

    def union_sets(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)
        if x != y:
            if self.dsu[x]["rank"] < self.dsu[y]["rank"]:
                x, y = y, x
            self.dsu[y]["parent"] = x
            self.dsu[x]["rank"] += self.dsu[y]["rank"]
            self.sets[x] += self.sets[y]
            del self.sets[y]

    @staticmethod
    def random_weight():
        return random.randint(1, 1000)

    def __call__(self, n, comp_cnt):
        self.dsu = [self.make_set(i) for i in range(n)]
        self.sets = {i: GraphComponent({i}) for i in range(n)}
        edges = []
        adj_list = {{} for i in range(n)}
        while len(self.sets > comp_cnt):
            u, v = random.sample(self.sets.keys(), 2)
            w = self.random_weight()
            self.union_sets(u, v)
            if random.random() < 0.5:
                u, v = v, u
            adj_list[u].add(v)
            adj_list[v].add(u)
            edges.append((u, v, w))
        m_max = 0
        m_cur = 0
        for _, j in self.sets.items():
            set_len = len(j)
            m_cur += set_len
            m_max += set_len * (set_len - 1) / 2
            verticies = sorted(list(j))
            for i in range(len(verticies)):
                for j in range(i+1, len(verticies)):
                    u, v = verticies[i], verticies[j]
                    if v not in adj_list[u]:
                        j.free_edges.add((u, v))
        m = random.randint(m_cur, m_max)
        while m_cur < m:
            i = random.choice(self.sets.keys())
            j = self.sets[i]
            edge = random.choice(j.free_edges)
            j.free_edges.remove(edge)
            if len(j.free_edges) == 0:
                del self.sets[i]
            if random.random() < 0.5:
                u, v = edge[::-1]
            else:
                u, v = edge
            w = self.random_weight()
            edges.append((u, v, w))
            m_cur += 1
        return random.shuffle(edges)


class Solver:
    def __init__(self):
        self.adj_list = None
        self.used = None

    def __call__(self, n, edges):
        self.adj_list = {{} for i in range(n)}
        for u, v, w in edges:
            self.adj_list[u].add((v, w))
            self.adj_list[v].add((u, w))
        self.used = [False] * n
        ans = []
        for i in range(n):
            if not self.used[i]:
                comp = []
                self.dfs(i, comp)
                total = 0
                for u in comp:
                    for v, w in self.adj_list[u]:
                        if v > u:
                            total += w
                ans.append(total)
        return sorted(ans)

    def dfs(self, u, comp):
        self.used[u] = True
        comp.append(u)
        for v, _ in self.adj_list[u]:
            if not self.used[v]:
                self.dfs(v, comp)


def str_question(n, m, edges):
    res = "{} {}\n".format(n, m)
    for u, v, w in edges:
        res += "{} {} {}\n".format(u, v, w)
    return res


def str_answer(ans):
    res = ""
    for e in ans:
        res += "{}\n".format(e)
    return res


tests = TestSet()

manual_tests = [
    (  # N, M, edge list, ans
        3, 3,
        [
            (1, 0, 1),
            (0, 2, 6),
            (2, 1, 1),

        ],
        [8]
    ),
    (
        4, 2,
        [
            (0, 1, 15),
            (2, 3, 26)
        ],
        [15, 26]
    ),
    (
        7, 4,
        [
            (2, 4, 2),
            (5, 2, 9),
            (7, 0, 6),
            (1, 6, 1)
        ],
        [1, 6, 11]
    ),
    (
        1, 0,
        [],
        [0]
    ),
    (
        15, 0,
        [],
        [0] * 15
    ),
]

for A, S, ans in manual_tests:
    tests.add(str_question(A, S), str_answer(ans))

generator = GraphGen()
solver = Solver()

for _ in range(5, 16):
    n = random.randint(10, 40)
    comp_cnt = random.randint(1, n)
    edges = generator(n, comp_cnt)
    m = len(edges)
    ans = solver(n, edges)
    tests.add(str_question(n, m, edges), str_answer(ans))

for _ in range(16, 20):
    n = random.randint(40, 250)
    comp_cnt = random.randint(1, n)
    edges = generator(n, comp_cnt)
    m = len(edges)
    ans = solver(n, edges)
    tests.add(str_question(n, m, edges), str_answer(ans))

n = 1000
comp_cnt = random.randint(250, 500)
edges = generator(n, comp_cnt)
m = len(edges)
ans = solver(n, edges)
tests.add(str_question(n, m, edges), str_answer(ans))

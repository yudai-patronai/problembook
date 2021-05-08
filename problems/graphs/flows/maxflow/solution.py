from queue import SimpleQueue


class Edge:
    def __init__(self, i, u, v, c):
        self.i = i
        self.u = u
        self.v = v
        self.c = c
        self.f = 0


def bfs():
    d = [float("inf")] * n
    d[s] = 0
    q = SimpleQueue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for e in adj_list[u]:
            v = e.v
            if d[v] > d[u] + 1 and e.c-e.f > 0:
                d[v] = d[u] + 1
                q.put(v)
                p[v] = e.i
                if v == t:
                    return True
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    edges = []
    for i in range(m):
        u, v, c = map(int, input().split())
        e = Edge(2 * i, u, v, c)
        adj_list[u].add(e)
        edges.append(e)
        e = Edge(2 * i + 1, v, u, 0)
        adj_list[v].add(e)
        edges.append(e)
    s = 0
    t = n - 1

    max_flow = 0
    while True:
        p = [-1] * n
        if not bfs():
            break
        path = []
        cur = t
        while cur != 0:
            e = edges[p[cur]]
            path.append(e)
            cur = e.u
        path.reverse()
        f = float("inf")
        v = 0
        for e in path:
            u = v
            v = e.v
            if f > e.c - e.f:
                f = e.c - e.f
        for e in path:
            u = v
            v = e.v
            e.f += f
            edges[e.i ^ 1].f -= f
        max_flow += f

    print(max_flow)

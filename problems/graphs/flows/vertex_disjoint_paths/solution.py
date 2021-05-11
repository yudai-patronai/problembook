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
    n, m, k = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        if u != 0:
            u += n
        e = Edge(2 * i, u, v, 1)
        adj_list[u].add(e)
        edges.append(e)
        e = Edge(2 * i + 1, v, u, 0)
        adj_list[v].add(e)
        edges.append(e)
    i = 2 * m
    for u in range(1, n-1):
        v = u + n
        e = Edge(i, v, 1)
        i += 1
        adj_list[u].add(e)
        edges.append(e)
        e = Edge(i, u, 0)
        i += 1
        adj_list[v].add(e)
        edges.append(e)
    s = 0
    t = n-1

    while k:
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
        for e in path:
            u = v
            v = e.v
            e.f += 1
            edges[e.i ^ 1].f -= 1
        k -= 1

    if k:
        print("NO")
    else:
        print("YES")

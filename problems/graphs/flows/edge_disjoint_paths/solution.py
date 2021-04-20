class Edge:
    def __init__(self, i, v, c):
        self.i = i
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
                p[v] = u
                if v == t:
                    return True
    return False


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        e = Edge(2 * i, v, 1)
        adj_list[u].add(e)
        edges.append(e)
        e = Edge(2 * i + 1, u, 0)
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
        while cur != -1:
            path.append(cur)
            cur = p[cur]
        for i in range(1, len(path)):
            u = path[i]
            v = path[i-1]
            for e in adj_list[u]:
                if e.v == v:
                    e.f += 1
                    edges[e.i ^ 1].f -= 1
        k -= 1

    if k:
        print("NO")
    else:
        print("YES")

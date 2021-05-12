from queue import SimpleQueue


def bfs(adj_list):
    n = len(adj_list)
    used = [0] * n
    used[0] = 1
    q = SimpleQueue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in adj_list[u]:
            if not used[v]:
                used[v] = 1
                q.put(v)
    return sum(used) == n


def solve(adj_list):
    n = len(adj_list)
    for i in range(n):
        if len(adj_list[i]) % 2:
            return "NO"
    if bfs(adj_list):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    n, m = map(int, input().split())

    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)
        adj_list[v].add(u)
    print(solve(adj_list))

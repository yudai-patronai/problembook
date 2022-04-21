def dfs(u):
    used[u] = True
    to_win = 0
    for v in adj_list[u]:
        if not used[v]:
            dfs(v)
        if state[v] is None:
            pass
        elif not state[v]:
            state[u] = True
            break
        else:
            to_win += 1
    else:
        if to_win == len(adj_list[u]):
            state[u] = False


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)

    used = [False] * n
    state = [None] * n
    dfs(s)
    if state[s] is None:
        print("Draw")
    elif not state[s]:
        print("Lose")
    else:
        print("Win")

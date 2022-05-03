def dfs(u):
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            deg_in[v] -= 1
            if state[u] == False:
                state[v] = True
            elif deg_in[v] == 0:
                state[v] = False
            else:
                continue
            dfs(v)


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    deg_in = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[v].add(u)
        deg_in[u] += 1

    used = [False] * n
    state = [None] * n
    for i in range(n):
        if not used[i] and deg_in[i] == 0:
            state[i] = False
            dfs(i)
    if state[s] is None:
        print("Draw")
    elif not state[s]:
        print("Lose")
    else:
        print("Win")

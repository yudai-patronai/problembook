def dfs(st):
    visited[st] = True
    for i in range(N):
        if i != st and (a[st][i] == 1 or a[i][st] == 1) and not visited[i]:
            dfs(i)


N, S = map(int, input().split())
a = []
visited = [False] * N
for i in range(N):
    a.append(list(map(int, input().split())))
dfs(S)
print(sum(visited)-1)

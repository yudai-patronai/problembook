
def dfs(start):
    visited[start] = True
    for i in range(N):
        if i != start and (a[start][i] == 1 or a[i][start] == 1) and not visited[i]:
            dfs(i)


N, S = map (int, input().split())
a = []
visited = [False] * N
for i in range(N):
    a.append(list(map(int, input().split())))
dfs(S)
print(sum(visited)-1)


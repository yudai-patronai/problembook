N = int(input())
cell_cost = []
for i in range(N):
    cell_cost.append([])
    line = input()
    for j in range(N):
        cell_cost[i].append(int(line[j]))

to_cost = [[10**6] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j == 0:
            to_cost[i][j] = cell_cost[i][j]
        elif j == 0:
            to_cost[i][j] = to_cost[i - 1][j]
        elif i == 0:
            to_cost[i][j] = to_cost[i][j - 1]
        else:
            to_cost[i][j] = min(to_cost[i - 1][j], to_cost[i][j - 1])
        to_cost[i][j] += cell_cost[i][j]

i = j = N-1
path = []
while True:
    path.insert(0, (i, j))
    if i == j == 0:
        break
    if i == 0 or to_cost[i][j-1] < to_cost[i-1][j]:
        j = j - 1
        continue
    i = i - 1
    continue

res = [["." for _ in range(N)] for _ in range(N)]
for i, j in path:
    res[i][j] = "#"
print(*[" ".join(x) for x in res], sep="\n")

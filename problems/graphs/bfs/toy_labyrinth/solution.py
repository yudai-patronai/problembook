#!/usr/bin/env python3


def solve(N, M, field):
    graph = [[] for _ in range(N*M)]
    for i_n in range(N):
        for i_m in range(M):
            if field[i_n][i_m] > 0:
                continue
            conn_list = []
            # идем вверх
            for din in range(1, i_n+1):
                if field[i_n - din][i_m] == 1:
                    break
                if field[i_n - din][i_m] == 2:
                    conn_list.append((i_n - din)*M + i_m)
                    break
                if field[i_n - din][i_m] == 0 and i_n - din == 0:
                    conn_list.append((i_n - din)*M + i_m)
                    break
                if field[i_n - din][i_m] == 0 and \
                        field[i_n - din - 1][i_m] == 1:
                    conn_list.append((i_n - din)*M + i_m)
                    break

            # идем вниз
            for din in range(1, N-i_n):
                if field[i_n + din][i_m] == 1:
                    break
                if field[i_n + din][i_m] == 2:
                    conn_list.append((i_n + din)*M + i_m)
                    break
                if field[i_n + din][i_m] == 0 and i_n + din == N-1:
                    conn_list.append((i_n + din)*M + i_m)
                    break
                if field[i_n + din][i_m] == 0 and \
                        field[i_n + din + 1][i_m] == 1:
                    conn_list.append((i_n + din)*M + i_m)
                    break

            # идем влево
            for dim in range(1, i_m+1):
                if field[i_n][i_m - dim] == 1:
                    break
                if field[i_n][i_m - dim] == 2:
                    conn_list.append(i_n*M + i_m-dim)
                    break
                if field[i_n][i_m - dim] == 0 and i_m - dim == 0:
                    conn_list.append(i_n*M + i_m-dim)
                    break
                if field[i_n][i_m - dim] == 0 and \
                        field[i_n][i_m - dim - 1] == 1:
                    conn_list.append(i_n*M + i_m-dim)
                    break

            # идем вправо
            for dim in range(1, M-i_m):
                if field[i_n][i_m + dim] == 1:
                    break
                if field[i_n][i_m + dim] == 2:
                    conn_list.append(i_n*M + i_m+dim)
                    break
                if field[i_n][i_m + dim] == 0 and i_m + dim == M-1:
                    conn_list.append(i_n*M + i_m+dim)
                    break
                if field[i_n][i_m + dim] == 0 and \
                        field[i_n][i_m + dim + 1] == 1:
                    conn_list.append(i_n*M + i_m+dim)
                    break
            graph[i_n*M + i_m] = conn_list
    n = N*M
    end_vertexes = []
    for i_n in range(N):
        for i_m in range(M):
            if field[i_n][i_m] == 2:
                end_vertexes.append(i_n*M + i_m)
    start_vertex = 0
    distances = [None] * n
    distances[start_vertex] = 0
    queue = [start_vertex]
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                queue.append(v)
    dists = [distances[v] for v in end_vertexes]
    for i in range(len(dists)):
        if dists[i] is None:
            dists[i] = 10000000
    return min(dists)


if __name__ == "__main__":
    N, M = map(int, input().split())
    field = []
    for i in range(N):
        field.append(list(map(int, input().split())))
    print(solve(N, M, field))

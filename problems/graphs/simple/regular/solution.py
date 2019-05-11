if __name__ == "__main__":
    n, m = map(int, input().split())
    deg = [0]*n
    for _ in range(m):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    for i in range(1, n):
        if deg[i] != deg[i-1]:
            print('NO')
            exit(0)
    print('YES')

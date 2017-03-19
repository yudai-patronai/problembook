
def solve(n, edges):
    comp = [i for i in range(n)]
    n_comp = n
    components = [[i] for i in range(n)]
    for i, edge in enumerate(edges, start=1):
        start, end = edge
        a = comp[start]
        b = comp[end]
        if a != b:
            n_comp -= 1
            if n_comp == 1:
                break
            if len(components[a]) < len(components[b]):
                a, b = b, a

            for v in components[b]:
                comp[v] = a

            components[a].extend(components[b])
            components[b] = []

    return str(i) + '\n'

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        s, e = map(int, input().split())
        edges.append((s, e))
    print(solve(n, edges), end='')

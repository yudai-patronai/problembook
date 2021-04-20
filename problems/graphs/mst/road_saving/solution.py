# graphs/mst/prima fbd7fd6f-17da-4aed-b37f-a0146d242b6d

def find_min_edge(G, V_mst, V_bound):
    u_min, v_min, min_w = None, None, float('inf')
    for u in V_mst:
        for v, w in G[u]:
            if v in V_bound and w < min_w:
                u_min, v_min, min_w = u, v, w
    return u_min, v_min, min_w


def add_edge(G, u, v, w):
    if u not in G:
        G[u] = set()
    if v not in G:
        G[v] = set()
    G[u].add((v, w))
    G[v].add((u, w))


def mst_prim_naive(G):
    mst_weight = 0
    
    start = 0
    V_mst = set([start])
    V_bound = set([v for v, w in G[start]])
    V_unproc = set(G) - V_mst - V_bound

    while len(G) != len(V_mst):
        # u in mst, v in bound
        u_min, v_min, w_min = find_min_edge(G, V_mst, V_bound)

        mst_weight += w_min
        V_bound.remove(v_min)
        V_mst.add(v_min)

        for v, w in G[v_min]:
            if v in V_unproc:
                V_bound.add(v)
                V_unproc.remove(v)

    return mst_weight


district_road = int(input())
V, E = map(int, input().split())
G = {u: set() for u in range(V)}

town_road = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].add((v, w))
    G[v].add((u, w))
    town_road += w

mst_weight = mst_prim_naive(G)
if town_road - mst_weight >= district_road:
    print('YES')
else:
    print('NO')

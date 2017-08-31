#!/usr/bin/env python3
import networkx as nx

from lib.graphs import task


def solve(graph):
    edges = [(i, j, w) for i in range(len(graph)) for j, w in graph[i]]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    dijkstra_paths = nx.all_pairs_dijkstra_path_length(G)
    paths = [(i, j, dijkstra_paths[i][j]) for i in dijkstra_paths if G.degree(i) % 2
             for j in dijkstra_paths[i] if i != j and G.degree(j) % 2]
    max_shortest_path = max([t[2] for t in paths])
    paths_inv = [(a, b, 1 + max_shortest_path - w) for a, b, w in paths]
    G2 = nx.Graph()
    G2.add_weighted_edges_from(paths_inv)
    matches = nx.max_weight_matching(G2, maxcardinality=True)
    sum_weight = 0
    for e in G.edges(data=True):
        sum_weight += e[2]['weight']
    for e in G2.edges(data=True):
        if matches[e[0]] == e[1]:
            sum_weight += 1 + max_shortest_path - e[2]['weight']

    return str(sum_weight) + '\n'


if __name__ == "__main__":
    n, m, g = task.read_task_weight()
    print(solve(g), end='')

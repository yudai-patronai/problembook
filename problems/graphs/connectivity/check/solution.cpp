#include <iostream>

struct Edge {
    unsigned v1;
    unsigned v2;
};

unsigned visit(unsigned n, unsigned n_edges, bool* visited, Edge* edges) {
    unsigned n_visited = 1;
    visited[n] = true;
    for (unsigned i = 0; i < n_edges; ++i) {
        if (edges[i].v1 == n && !visited[edges[i].v2]) {
            n_visited += visit(edges[i].v2, n_edges, visited, edges);
        }
        if (edges[i].v2 == n && !visited[edges[i].v1]) {
            n_visited += visit(edges[i].v1, n_edges, visited, edges);
        }
    }

    return n_visited;
}

int main() {
    unsigned n_vertices, n_edges;

    std::cin >> n_vertices >> n_edges;

    Edge* edges = new Edge[n_edges];
    bool* visited = new bool[n_vertices];

    for (unsigned i = 0; i < n_edges; ++i) {
        std::cin >> edges[i].v1 >> edges[i].v2;
    }

    if (visit(0, n_edges, visited, edges) == n_vertices)
        std::cout << "YES" << std::endl;
    else
        std::cout << "NO" << std::endl;

    delete[] edges;
    delete[] visited;
    return 0;
}

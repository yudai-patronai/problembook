#include <iostream>
#include <vector>
#include <climits>
using std::vector;
using std::cin;
using std::cout;
using std::endl;

const int UNREACHABLE = INT_MAX;

void udf_dfs(vector<vector<int>> *graph, vector<vector<int>> *fb, int j) {
    (*fb)[(*fb).size() - 2][j] = UNREACHABLE;
    for (auto &edge : *graph) {
        if (edge[0] == j)
            if ((*fb)[(*fb).size() - 2][edge[1]] != UNREACHABLE)
                udf_dfs(graph, fb, edge[1]);
    }
}

int main() {
    int n_vertices, m_edges, start;
    cin >> n_vertices >> m_edges >> start;

    vector<vector<int>> graph;
    graph.resize(m_edges);
    for (auto &edge : graph)
        edge.resize(3);
    for (int i = 0; i < m_edges; i++) {
        int from, to, weight;
        cin >> from >> to >> weight;
        graph[i] = {from, to, weight};
    }

    vector<vector<int>> fordb;
    fordb.resize(m_edges + 2);
    for (auto &row : fordb)
        row.resize(n_vertices, UNREACHABLE);
    fordb[0][start] = 0;

    for (int i = 0; i < m_edges + 1; i++) {
        for (int j = 0; j < n_vertices; j++)
            fordb[i + 1][j] = fordb[i][j];
        for (auto edge : graph) {
            if (fordb[i][edge[0]] != UNREACHABLE)
                if (fordb[i][edge[0]] + edge[2] < fordb[i + 1][edge[1]])
                    fordb[i + 1][edge[1]] = fordb[i][edge[0]] + edge[2];
        }
    }

    for (int j = 0; j < n_vertices; j++) {
        if (fordb[m_edges][j] > fordb[m_edges + 1][j]) {
            udf_dfs(&graph, &fordb, j);
        }
    }

    for (auto length : fordb[m_edges])
        if (length == UNREACHABLE)
            cout << "UDF ";
        else
            cout << length << " ";
    cout << endl;

    return 0;
}

#include <iostream>

void floyd_warshall(int** graph, int n) {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][k] > 0 && graph[k][j] > 0) {
                    if (graph[i][j] > 0)
                        graph[i][j] = std::min(
                                        graph[i][j],
                                        graph[i][k] + graph[k][j]);
                    else
                        graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }
}

int main() {
    int n, first_v, second_v;
    std::cin >> n >> first_v >> second_v;

    int** graph = new int*[n];
    for (int i = 0; i < n; i++) {
        graph[i] = new int[n];
        for (int j = 0; j < n; j++)
            std::cin >> graph[i][j];
    }

    floyd_warshall(graph, n);

    std::cout << graph[first_v - 1][second_v - 1] << std::endl;

    for (int i = 0; i < n; i++)
        delete[] graph[i];

    delete[] graph;

    return 0;
}
